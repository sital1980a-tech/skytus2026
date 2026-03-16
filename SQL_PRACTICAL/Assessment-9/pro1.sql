import sqlite3
from datetime import datetime, timedelta

# Connect to the database
conn = sqlite3.connect('company_data.db')
cursor = conn.cursor()

cursor.execute('''delete from employees''')
# Tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY,
    emp_name VARCHAR(50),
    salary INTEGER,
    hire_date DATE
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS emp_dummy (
    project_id INTEGER PRIMARY KEY,
    emp_name VARCHAR(50)
)''')

# Data
emp_data = [
    (1, 'kunjal', 70000, '2025-11-01'),
    (2, 'jinal', 80000, '2025-01-15'),
    (3, 'priti', 80000, '2025-12-20'),
    (4, 'payal', 70000, '2024-05-10'),
    (5, 'kunjal', 90000, '2025-11-01'), # Duplicate record
    (6, 'sejal', 90000, '2026-01-05'),
    (7, 'sejal', 90000, '2026-01-05'),
    (8, 'payal', 90000, '2024-05-10')
]

cursor.executemany("INSERT OR IGNORE INTO employees VALUES (?, ?, ?, ?)", emp_data)
cursor.execute("INSERT OR IGNORE INTO emp_dummy VALUES (101, 'kunjal'), (102, 'jinal')")
conn.commit()

def execute_query(title, query, params=()):
    print(f"\n {title}")
    cursor.execute(query, params)
    for row in cursor.fetchall():
        print(row)

# Tasks 

# 1: Find Nth highest salary (Example: 2nd highest)
n = 3
execute_query(f"1: {n}th Highest Salary", 
             "SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET ?", (n-1,))

# 2: Remove duplicate records
print("\n2: Removing Duplicates")
cursor.execute("""
    DELETE FROM employees 
    WHERE emp_id NOT IN (
        SELECT MIN(emp_id) FROM employees GROUP BY emp_name, salary
    )""")

conn.commit()
print("Duplicates removed.")


# 3: Find records common in two tables (Employees and emp_dummy)
execute_query("3: Common Records (Employees in emp_dummy)", 
             "SELECT emp_name FROM employees INTERSECT SELECT emp_name FROM emp_dummy")

# 4: Find employees hired in last 6 months
six_months_ago = (datetime.now() - timedelta(days=180)).strftime('%Y-%m-%d')
execute_query("4: Hired in last 6 months", 
             "SELECT emp_name, hire_date FROM employees WHERE hire_date >= ?", (six_months_ago,))

# 5: Find continuous duplicate values
execute_query("5: Continuous Duplicate Salaries (Ordered by ID)", 
             """SELECT emp_id, emp_name, salary FROM 
             (SELECT emp_id,emp_name,salary,LAG(salary) 
                OVER (ORDER BY emp_id) 
                    AS prev_salary FROM employees) t
                        WHERE salary = prev_salary""")

conn.close()
