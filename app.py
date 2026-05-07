import sqlite3

conn = sqlite3.connect("collage.db")

cursor = conn.cursor()

"""cursor.execute(CREATE TABLE collage 
(
    id INTEGER PRIMARY KEY,
    name TXT,
    subject TXT
)
)
"""
cursor.executemany(
    "INSERT INTO collage (name, subject) VALUES( ?, ?)",
    [
        ("Rahul", "Math"),
        ("Sneha", "Science"),
        ("Amit","English")
    ]
)

conn.commit()
cursor.execute("SELECT * FROM collage WHERE subject = 'Math'")
cursor.execute( "UPDATE collage SET subject = 'Physics' WHERE name = 'Rahul'")
cursor.execute("DELETE FROM students WHERE name = 'Amit'")
cursor.execute("SELECT * FROM collage")
print(cursor.fetchall())

conn.close()

