-- prepares a MySQL server for the project
-- creates the database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create a user only if the user doesn't exists
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant all privileges on the database hbnb_dev_db
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
-- grant SELECT privileges on performance_schema
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
