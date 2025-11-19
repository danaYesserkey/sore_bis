#!/usr/bin/env python3
import sqlite3
import cgi
import cgitb; cgitb.enable()

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
name = form.getfirst("name", "")
email = form.getfirst("email", "")
password = form.getfirst("password", "")

if not name or not email or not password:
    print("<h1>Error: Fill all fields</h1>")
    exit()

conn = sqlite3.connect("/Users/yesserkeydana/Desktop/sore-site/sore.db")
cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                   (name, email, password))
    conn.commit()

    print("""
    <html>
    <head>
    <title>Registration Success</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
        }
        .box {
            width: 350px;
        }
        h1 {
            font-size: 28px;
            color: #003399;
            margin-bottom: 20px;
        }
        a {
            color: #003399;
            font-size: 18px;
            font-weight: bold;
            text-decoration: none;
        }
        a:hover { text-decoration: underline; }
    </style>
    </head>
    <body>
        <div class="box">
            <h1>Registration successful!</h1>
            <a href="../index.html">Go back</a>
        </div>
    </body>
    </html>
    """)

except sqlite3.IntegrityError:
    print("<h1>Error: Email already exists</h1><a href='../index.html'>Back</a>")

conn.close()