CREATE TABLE IF NOT EXISTS students(
  student_id INT PRIMARY KEY,
  name VARCHAR(50),
  department VARCHAR(30),
  year INT,
  marks INT
);
INSERT INTO students VALUES
(1, 'Rahul', 'CSE', 2, 85),
(2, 'Priya', 'IT', 1, 72),
(3, 'Amit', 'CSE', 3, 90),
(4, 'Neha', 'ECE', 2, 68),
(5, 'Karan', 'CSE', 1, 78);
SELECT * FROM students;
SELECT name, department FROM students;
SELECT * FROM students WHERE marks > 75;
SELECT * FROM students WHERE department = 'CSE';
SELECT *FROM students ORDER BY marks DESC;
SELECT *FROM students ORDER BY marks DESC LIMIT 3;
