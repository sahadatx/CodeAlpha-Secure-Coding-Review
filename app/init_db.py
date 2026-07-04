import sqlite3

DATABASE = "database.db"

connection = sqlite3.connect(DATABASE)

with open("schema.sql") as f:
    connection.executescript(f.read())

connection.commit()
connection.close()

print("Database Created Successfully")