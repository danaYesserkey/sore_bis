# sɵre Database Schema

## Overview
This schema defines the database structure for user registration and authorization in the sɵre platform (a platform for buying, selling, and exchanging books).

## Database Choice
PostgreSQL was chosen over MySQL for:
- Better support for advanced data types and JSON
- Strong ACID compliance
- Built-in UUID support if needed later
- Superior handling of complex queries and transactions

## Tables

### Users Table
Stores user account information for registration and login.

#### Fields Explanation:
- `id`: Primary key, auto-incrementing integer for unique user identification
- `email`: User's email address, must be unique and required for login
- `password_hash`: Hashed password using bcrypt (recommended), required for security
- `username`: Optional unique username for display purposes
- `created_at`: Timestamp when the account was created (auto-set)
- `updated_at`: Timestamp of last account update (auto-updated via trigger)
- `last_login`: Timestamp of user's last successful login (updated on login)
- `is_verified`: Boolean flag for email verification status (default false)

#### Constraints and Indexes:
- PRIMARY KEY on `id`
- UNIQUE on `email` and `username`
- NOT NULL on `id`, `email`, `password_hash`, `created_at`, `updated_at`
- DEFAULT values for timestamps and `is_verified`
- Indexes on `email` and `username` for fast lookups

#### Triggers:
- `update_updated_at`: Automatically updates `updated_at` whenever a row is modified

## Usage
1. Run `schema.sql` to create the database and tables
2. Use `example_insert.sql` for testing data insertion
3. Connect your backend application to perform CRUD operations

## Security Notes
- Always hash passwords before storing (bcrypt recommended)
- Use prepared statements to prevent SQL injection
- Implement email verification for new accounts
- Log login attempts for security monitoring
