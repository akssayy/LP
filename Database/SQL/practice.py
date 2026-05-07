import sqlite3

conn = sqlite3.connect("collage.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE students 
(
    id INTEGER PRIMARY KEY,
    name TXT,
    subject TXT
)
""")
cursor.execute(
    "INSERT INTO collage (name, subject) VALUES( ?, ?)",
    ("Rahul", "Math"),
    ("Sneha", "Science"),
    ("Amit","English")
)

conn.commit()
cursor.execute("SELECT & FROM collage")
print(cursor.fetchall())

conn.close()

