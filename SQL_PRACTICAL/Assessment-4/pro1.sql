SELECT emp_name , salary 
FROM employees 
WHERE salary > (SELECT AVG(salary)FROM employees);
SELECT d.dept_name, SUM(e.salary) AS total_salary
FROM employees e
JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name
ORDER BY total_salary DESC
LIMIT 1;
SELECT emp_name, salary
FROM employees
ORDER BY salary DESC
OFFSET 1 LIMIT 1;
SELECT emp_name
FROM employees
WHERE dept_id = (
    SELECT dept_id
    FROM employees
    WHERE emp_name = 'Amit'
);
