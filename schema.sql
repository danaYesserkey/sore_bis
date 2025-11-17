-- Database Schema for sɵre User Registration and Authorization
-- Using PostgreSQL for better data integrity and advanced features

-- Create the database (if not exists)


-- Use the database


-- Users Table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    is_verified BOOLEAN DEFAULT FALSE,
    last_login TIMESTAMP
);

-- Index on email for faster lookups (already unique, but index helps)
CREATE INDEX idx_users_email ON users(email);

-- Index on username if used
CREATE INDEX idx_users_username ON users(username);

-- Trigger to update updated_at on row changes
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();


SELECT * FROM users;


