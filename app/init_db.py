import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

database_path = BASE_DIR / "database.db"
schema_path = BASE_DIR / "schema.sql"

connection = sqlite3.connect(database_path)

with open(schema_path, "r") as file:
    connection.executescript(file.read())

connection.commit()
connection.close()

print("Database Created Successfully")
