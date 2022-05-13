-- prepares a MySQL server for the project
-- create database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create user test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all acccess for user test
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
-- grant select privileges
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
