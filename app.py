import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TXT,
    age INTEGER
)
""")

cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Akshay", 22))
print("Database created")

conn.commit()

cursor.execute("SELECT * FROM students")
print(cursor.fetchall())
conn.close()