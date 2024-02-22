-- Prepares a MySQL server for the project.


-- Create hbnb_dev_db database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create hbnb_dev user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grants all privileges to hbnb_dev on database
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';
