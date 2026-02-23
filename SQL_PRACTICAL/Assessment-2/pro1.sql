CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    marks INT
);
INSERT INTO students VALUES
(1, 'Amit', 'Computer', 85),
(2, 'Neha', 'Computer', 78),
(3, 'Raj', 'Mechanical', 65),
(4, 'Simran', 'Mechanical', 72),
(5, 'Karan', 'Electrical', 90),
(6, 'Pooja', 'Electrical', 60);
SELECT COUNT(*) AS Total_Students FROM students;
SELECT AVG(marks) AS Average_Marks FROM students;
SELECT 
    MAX(marks) AS Highest_Marks,
    MIN(marks) AS Lowest_Marks
FROM students;
SELECT department, AVG(marks) AS Dept_Average
FROM students
GROUP BY department;
SELECT department, AVG(marks) AS Dept_Average
FROM students
GROUP BY department
HAVING AVG(marks) > 70;
