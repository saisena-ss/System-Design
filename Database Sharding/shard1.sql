
CREATE SEQUENCE IF NOT EXISTS shard1_user_id_seq START WITH 1;


CREATE TABLE IF NOT EXISTS Users (
    user_id INT PRIMARY KEY DEFAULT nextval('shard1_user_id_seq'),
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS Accounts (
    account_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES Users(user_id),
    balance DECIMAL(10, 2) NOT NULL
);

INSERT INTO Users (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com'),
('Charlie', 'charlie@example.com');


INSERT INTO Accounts (user_id, balance) VALUES
(1, 1000.50),
(2, 500.75),
(3, 1500.00);
