from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

# Define User model
class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    accounts = db.relationship('Account', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.name}, {self.email}>"

# Define Account model
class Account(db.Model):
    __tablename__ = 'accounts'

    account_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    balance = db.Column(db.Numeric(10, 2), nullable=False)

    def __repr__(self):
        return f"<Account User ID: {self.user_id}, Balance: {self.balance}>"
