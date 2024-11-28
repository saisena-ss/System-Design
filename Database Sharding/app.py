from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from sharding import ShardingFactory

from models import db, User, Account


load_dotenv(dotenv_path='../')

app  = Flask(__name__)

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

sharding_strategy = ShardingFactory('range')

db.init_app(app)

def get_db_uri(user_id):

    db_shard = sharding_strategy(user_id)
    return f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{db_shard}"
    

@app.route('/add_user', methods = ['POST'])
def add_user():
    data = request.get_json()
    user_id = data.get(user_id) #ideally this should be generated through a distributed framework (unique id)
    user_name = data.get('user_name')
    email = data.get('email')

    app.config['SQLALCHEMY_DATABASE_URI'] = get_db_uri(user_id)
    db.create_scoped_session()

    new_user = User(user_id=user_id, name = user_name, email = email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message':'User added succesfully!'}),201

@app.route('/add_account',methods = ['POST'])
def add_account():
    data = request.get_json()
    user_id = data.get('user_id')
    balance = data.get('balance')

    app.config['SQLALCHEMY_DATABASE_URI'] = get_db_uri(user_id)
    db.create_scoped_session()

    new_account = Account(user_id=user_id, balance=balance)
    db.session.add(new_account)
    db.session.commit()

    return jsonify({'message': 'Account created successfully'}), 201

@app.route('/get_account',methods = ['GET'])
def get_account():
    user_id = request.args.get('user_id',type = int)

    app.config['SQLALCHEMY_DATABASE_URI'] = get_db_uri(user_id)

    account = Account.query.filter_by(user_id = user_id)

    return jsonify({'account_id': account.account_id, 'balance': str(account.balance)})

@app.route('/withdraw', methods = ['POST'])
def withdraw():
    data = request.get_json()
    user_id = data.get('user_id')
    account_id = data.get('account_id')
    amount = data.get('amount')

    # Select shard based on user_id
    app.config['SQLALCHEMY_DATABASE_URI'] = get_db_uri(user_id)
    db.create_scoped_session()

    account = Account.query.filter_by(account_id=account_id, user_id=user_id)
    if account is None:
        return jsonify({'error': 'Account not found'}), 404

    if account.balance < amount:
        return jsonify({'error': 'Insufficient funds'}), 400

    account.balance -= amount
    db.session.commit()

    return jsonify({'message': 'Withdrawal successful', 'remaining_balance': str(account.balance)}), 200


if __name__ == '__main__':
    app.run(debug=True)