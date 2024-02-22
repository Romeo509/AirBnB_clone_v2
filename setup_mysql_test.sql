-- Prepares a MySQL Test server for the project.

-- Create hbnb_test_db database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create hbnb_test user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on database
GRANT ALL PRIVILEGES ON hbnb_test_db . * TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema . * TO 'hbnb_test'@'localhost';
