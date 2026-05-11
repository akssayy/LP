import sqlite3

conn = sqlite3.connect("collage.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE emp
(
    id INTEGER PRIMARY KEY,
    name TXT,
    subject TXT
)
""")
cursor.executemany(
    "INSERT INTO emp (name, subject) VALUES( ?, ?)",
    ("Rahul", "Math"),
    ("Sneha", "Science"),
    ("Amit","English")
)

conn.commit()
cursor.execute("SELECT & FROM emp")
print(cursor.fetchall())

conn.close()

