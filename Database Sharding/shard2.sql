drop table if exists Users CASCADE;
drop table if exists Accounts;
drop SEQUENCE if exists shard2_user_id_seq;


CREATE SEQUENCE IF NOT EXISTS shard2_user_id_seq START WITH 1000; 


CREATE TABLE IF NOT EXISTS Users (
    user_id INT PRIMARY KEY DEFAULT nextval('shard2_user_id_seq'),
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS Accounts (
    account_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES Users(user_id),
    balance DECIMAL(10, 2) NOT NULL
);



INSERT INTO Users (name, email) VALUES
('David', 'david@example.com'),
('Eve', 'eve@example.com'),
('Frank', 'frank@example.com');


INSERT INTO Accounts (user_id, balance) VALUES
(1000, 1200.50),
(1001, 800.75),
(1002, 2000.00);


select * from Users;
select * from Accounts;
