CREATE TABLE accounts (
    acc_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    balance INT
);
INSERT INTO accounts ( name , balance)
VALUES
('Amit',10000),('riya',5000);
SELECT *FROM accounts;
BEGIN;

INSERT INTO accounts (name, balance)
VALUES ('Karan',7000);

ROLLBACK;
BEGIN;

INSERT INTO accounts (name, balance)
VALUES ('Karan',7000);

COMMIT;
SELECT * FROM accounts;
BEGIN;

UPDATE accounts
SET balance = balance - 2000
WHERE name = 'Amit';

UPDATE accounts
SET balance = balance + 2000
WHERE name = 'Riya';

COMMIT;
SELECT * FROM accounts;
