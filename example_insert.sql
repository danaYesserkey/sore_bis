-- Example INSERT statements for testing the users table

-- Insert a verified user
INSERT INTO users (email, password_hash, username, is_verified)
VALUES ('user@example.com', '$2b$10$examplehashedpassword123456789012345678901234567890', 'exampleuser', TRUE);

-- Insert an unverified user
INSERT INTO users (email, password_hash, username)
VALUES ('newuser@example.com', '$2b$10$anotherhashedpassword123456789012345678901234567890', 'newuser');

-- Insert a user without username
INSERT INTO users (email, password_hash, is_verified)
VALUES ('admin@sore.com', '$2b$10$adminhashedpassword123456789012345678901234567890', TRUE);

-- Update last_login for a user (simulate login)
UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE email = 'user@example.com';
