const express = require("express");
const path = require("path");
const cors = require("cors");
const { Pool } = require("pg");
const bcrypt = require("bcrypt");
const url = "http://localhost:5000/register";
const app = express();
app.use(cors());
app.use(express.json());

// PostgreSQL
const db = new Pool({
    user: "postgres",
    host: "localhost",
    database: "sore",
    password: "12345",
    port: 5432,
});

// STATIC
app.use(express.static(path.join(__dirname, "public")));

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "public", "index.html"));
});

// ----------------- REGISTER -----------------
app.post("/register", async (req, res) => {
    try {
        const { email, password } = req.body;

        const hash = await bcrypt.hash(password, 10);

        await db.query(
            "INSERT INTO users (email, password_hash) VALUES ($1, $2)",
            [email, hash]
        );

        res.json({ message: "Registered!" });
    } 
    catch (err) {
        console.error(err);
        res.status(400).json({ message: "Error" });
    }
});

// ----------------- LOGIN -----------------
app.post("/login", async (req, res) => {
    try {
        const { email, password } = req.body;

        const result = await db.query(
            "SELECT * FROM users WHERE email=$1",
            [email]
        );

        if (result.rows.length === 0)
            return res.json({ message: "User not found" });

        const user = result.rows[0];

        const ok = await bcrypt.compare(password, user.password_hash);
        if (!ok) return res.json({ message: "Wrong password" });

        res.json({ message: "Login ok!" });
    } 
    catch (err) {
        console.error(err);
        res.status(400).json({ message: "Error" });
    }
});

// SERVER START
app.listen(5000, () =>
    console.log("Server running on http://localhost:5000")
);

