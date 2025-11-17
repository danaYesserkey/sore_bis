const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const sqlite3 = require("sqlite3").verbose();
const app = express();
const PORT = 3000;

// Middlewares
app.use(cors());
app.use(bodyParser.json());
app.use(express.static("public"));

// Database
const db = new sqlite3.Database("./database.db", (err) => {
    if (err) console.error("DB Error:", err);
    else console.log("SQLite DB connected");
});

// Create table
db.run(`
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        password TEXT
    )
`);

// Register
app.post("/register", (req, res) => {
    const { email, password } = req.body;

    if (!email || !password)
        return res.status(400).send("Missing fields");

    db.run(
        "INSERT INTO users (email, password) VALUES (?, ?)",
        [email, password],
        (err) => {
            if (err) return res.status(400).send("User exists or DB error");
            res.send("User registered successfully");
        }
    );
});

// Login
app.post("/login", (req, res) => {
    const { email, password } = req.body;

    db.get(
        "SELECT * FROM users WHERE email = ? AND password = ?",
        [email, password],
        (err, row) => {
            if (err) return res.status(500).send("DB error");
            if (!row) return res.status(401).send("Incorrect login");

            res.send("Login successful");
        }
    );
});

app.listen(PORT, () =>
    console.log(`Server running on http://localhost:${PORT}`)
);
