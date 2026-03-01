CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10,2)
);
CREATE INDEX idx_customer_id 
ON orders(customer_id);
EXPLAIN SELECT * 
FROM orders 
WHERE customer_id = 101;
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
INSERT INTO customers (name, email) VALUES
('Rahul', 'rahul@gmail.com'),
('Priya', 'priya@gmail.com');
INSERT INTO orders (customer_id, order_date, amount) VALUES
(1, '2024-01-10', 500.00),
(1, '2024-02-15', 700.00),
(2, '2024-03-01', 300.00);
