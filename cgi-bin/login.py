#!/usr/bin/env python3
import sqlite3
import cgi
import cgitb

cgitb.enable()

print("Content-Type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()
email = form.getfirst("email", "")
password = form.getfirst("password", "")

conn = sqlite3.connect("/Users/yesserkeydana/Desktop/sore-site/sore.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
user = cursor.fetchone()
conn.close()

if user:
    name = user[1]
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>sore — Profile</title>
    <link rel="stylesheet" href="../style.css">
    <style>
        .welcome-box {{
            margin-top: 20px;
            padding: 20px;
            border: 2px solid #003399;
            border-radius: 12px;
        }}
        .username {{
            font-size: 22px;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        .subtitle {{
            color: #555;
            font-size: 14px;
        }}
        a.button-link {{
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            background: #003399;
            color: white;
            border-radius: 8px;
            text-decoration: none;
            font-size: 16px;
        }}
        a.button-link:hover {{
            background: #002080;
        }}
    </style>
</head>
<body>
    <div class="container">
        <img src="../logo.jpg" class="logo" alt="sore">
        <h1 class="title">Welcome to sore</h1>

        <div class="welcome-box">
            <div class="username">Welcome, {name}!</div>
            <div class="subtitle">You are successfully logged in to your sɵre account.</div>
        </div>

        <a href="../index.html" class="button-link">Log out</a>
    </div>
</body>
</html>
"""
else:
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>sore — Login error</title>
    <link rel="stylesheet" href="../style.css">
    <style>
        .error-box {
            margin-top: 20px;
            padding: 20px;
            border: 2px solid #cc0000;
            border-radius: 12px;
            color: #cc0000;
        }
        a.button-link {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            background: #003399;
            color: white;
            border-radius: 8px;
            text-decoration: none;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="../logo.jpg" class="logo" alt="sore">
        <h1 class="title">Welcome to sore</h1>

        <div class="error-box">
            Incorrect email or password.
        </div>

        <a href="../index.html" class="button-link">Back to login</a>
    </div>
</body>
</html>
"""

print(html)