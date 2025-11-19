#!/usr/bin/env python3
import sqlite3

conn = sqlite3.connect("/Users/yesserkeydana/Desktop/sore-site/sore.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);
""")

conn.commit()
conn.close()

print("Content-Type: text/plain\n")
print("Database successfully created!")