import sqlite3
conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT, grade REAL)")
cursor.execute("INSERT INTO students VALUES (1, 'Alice', 85.5)")
cursor.execute("INSERT INTO students VALUES (2, 'Bob', 90.0)")
conn.commit()
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()
