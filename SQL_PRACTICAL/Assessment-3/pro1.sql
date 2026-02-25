CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT,
    salary INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
INSERT INTO departments VALUES
(1,'HR'),
(2,'IT'),
(3,'Sales');

INSERT INTO employees VALUES
(101,'Amit',1,40000),
(102,'Riya',2,60000),
(103,'Karan',2,75000),
(104,'Neha',3,50000),
(105,'Jay',NULL,45000),
(106,'Priya',2,80000);
SELECT e.emp_name, d.dept_name
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id;
SELECT emp_name, salary
FROM employees
WHERE salary > 50000;
SELECT d.dept_name, SUM(e.salary) AS total_salary
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name;
SELECT d.dept_name, COUNT(e.emp_id) AS total_employees
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name
HAVING COUNT(e.emp_id) > 2;
SELECT emp_name
FROM employees
WHERE dept_id IS NULL;
