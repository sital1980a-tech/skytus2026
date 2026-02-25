CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100) NOT NULL
);
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id INT,
    amount INT,
    order_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
CREATE INDEX idx_users_email
ON users(email);
INSERT INTO users (name, email, password) VALUES
('Amit','amit@gmail.com','123'),
('Riya','riya@gmail.com','456'),
('Karan','karan@gmail.com','789');

INSERT INTO orders (user_id, amount, order_date) VALUES
(1,5000,'2025-02-01'),
(1,3000,'2025-02-05'),
(2,7000,'2025-02-10');
CREATE VIEW user_order_summary AS
SELECT u.user_id, u.name, u.email,
       COUNT(o.order_id) AS total_orders,
       COALESCE(SUM(o.amount),0) AS total_amount
FROM users u
LEFT JOIN orders o
ON u.user_id = o.user_id
GROUP BY u.user_id, u.name, u.email;
SELECT *FROM user_order_summary;
