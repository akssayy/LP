import sqlite3

conn = sqlite3.connect("college.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS collage (
    id INTEGER PRIMARY KEY,
    name TEXT,
    subject TEXT
)
""")

cursor.executemany(
    "INSERT INTO collage (name, subject) VALUES (?, ?)",
    [
        ("Rahul", "Math"),
        ("Sneha", "Science"),
        ("Amit", "English")
    ]
)

conn.commit()

cursor.execute("SELECT * FROM collage WHERE subject = 'Math'")
print("Math students:", cursor.fetchall())

cursor.execute("UPDATE collage SET subject = 'Physics' WHERE name = 'Rahul'")
cursor.execute("DELETE FROM collage WHERE name = 'Amit'")

conn.commit()

cursor.execute("SELECT * FROM collage")
print("All students:", cursor.fetchall())

conn.close()