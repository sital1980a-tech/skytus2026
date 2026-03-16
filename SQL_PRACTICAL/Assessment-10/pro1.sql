import sqlite3

# Connect to database
conn = sqlite3.connect(':memory:') 
cursor = conn.cursor()

# 1. TABLES 
cursor.executescript("""
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    hostel_block TEXT
);

CREATE TABLE meal_plans (
    plan_id INTEGER PRIMARY KEY,
    plan_name TEXT,  -- Veg, Non-Veg, Special
    monthly_cost REAL
);

CREATE TABLE subscriptions (
    sub_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    plan_id INTEGER,
    start_date DATE,
    status TEXT, -- 'Active', 'Expired'
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (plan_id) REFERENCES meal_plans(plan_id)
);

CREATE TABLE attendance (
    att_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    meal_type TEXT, -- 'Breakfast', 'Lunch', 'Dinner'
    date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    amount REAL,
    payment_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
""")

# 2. SAMPLE DATA 
students = [(1, 'Kunjal', 'A-Block'), (2, 'Jinal', 'B-Block'), (3, 'Priti', 'A-Block'), (4, 'payal', 'C-Block')]
plans = [(10, 'Veg Standard', 3000), (11, 'Non-Veg Premium', 4500)]
subs = [(1, 1, 10, '2024-01-01', 'Active'), (2, 2, 11, '2024-01-05', 'Active'), (3, 3, 10, '2024-01-01', 'Active')]
attendance = [(1, 1, 'Breakfast', '2024-02-01'), (2, 1, 'Lunch', '2024-02-01'), (3, 2, 'Lunch', '2024-02-01')]
payments = [(1, 1, 3000, '2024-01-02'), (2, 2, 4500, '2024-01-06')]

cursor.executemany("INSERT INTO students VALUES (?,?,?)", students)
cursor.executemany("INSERT INTO meal_plans VALUES (?,?,?)", plans)
cursor.executemany("INSERT INTO subscriptions VALUES (?,?,?,?,?)", subs)
cursor.executemany("INSERT INTO attendance VALUES (?,?,?,?)", attendance)
cursor.executemany("INSERT INTO payments VALUES (?,?,?,?)", payments)

# 3. 15 BUSINESS QUERIES 
queries = [
    ("List all students", "SELECT * FROM students"),
    ("Count students per block", "SELECT hostel_block, COUNT(*) FROM students GROUP BY hostel_block"),
    ("Active subscriptions", "SELECT COUNT(*) FROM subscriptions WHERE status='Active'"),
    ("Student & their plan names", "SELECT s.name, m.plan_name FROM students s JOIN subscriptions sub ON s.student_id = sub.student_id JOIN meal_plans m ON sub.plan_id = m.plan_id"),
    ("Total revenue collected", "SELECT SUM(amount) FROM payments"),
    ("Students who haven't paid", "SELECT name FROM students WHERE student_id NOT IN (SELECT student_id FROM payments)"),
    ("Attendance count for today", "SELECT COUNT(*) FROM attendance WHERE date='2024-02-01'"),
    ("Most popular meal plan", "SELECT plan_id, COUNT(*) as cnt FROM subscriptions GROUP BY plan_id ORDER BY cnt DESC LIMIT 1"),
    ("Average payment amount", "SELECT AVG(amount) FROM payments"),
    ("List all 'Veg Standard' students", "SELECT s.name FROM students s JOIN subscriptions sub ON s.student_id = sub.student_id WHERE sub.plan_id=10"),
    ("Last 5 attendance records", "SELECT * FROM attendance ORDER BY date DESC LIMIT 5"),
    ("Total students in C-Block", "SELECT COUNT(*) FROM students WHERE hostel_block='C-Block'"),
    ("Total payments in January", "SELECT SUM(amount) FROM payments WHERE payment_date LIKE '2024-01%'"),
    ("Students id with multiple entries today", "SELECT student_id FROM attendance GROUP BY student_id HAVING COUNT(*) > 1"),
    ("All distinct meal types", "SELECT DISTINCT meal_type FROM attendance")
]

print("--- 15 Business Queries ---")
i=0
for desc, q in queries:
    cursor.execute(q)
    i=i+1
    print(f"{i} :- {desc} :- {cursor.fetchone()}")

# Optimization 1: Indexing for searching students by block
cursor.execute("CREATE INDEX idx_hostel_block ON students(hostel_block)")
print("\n1. Added index on hostel_block for faster filtering.")

# Optimization 2: Use EXPLAIN to analyze a Join Query
print("2. Analyzing Join Query Plan:")
cursor.execute("EXPLAIN QUERY PLAN SELECT s.name, p.amount FROM students s JOIN payments p ON s.student_id = p.student_id")
for row in cursor.fetchall():
    print(f"   Plan: {row[3]}")

# Optimization 3: Covering Index for Payments
cursor.execute("CREATE INDEX idx_pay_student_amt ON payments(student_id, amount)")
print("3. Created composite index on payments(student_id, amount) to speed up revenue-per-student queries.")

conn.close()
