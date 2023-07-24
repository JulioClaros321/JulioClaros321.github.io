DROP DATABASE IF EXISTS PAYROLL_DB;
CREATE DATABASE PAYROLL_DB;
USE PAYROLL_DB;


DROP TABLE IF EXISTS employees; 
CREATE TABLE employees (
	employee_id INT PRIMARY KEY,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL, 
    street VARCHAR(40) NOT NULL,
    city VARCHAR(30) NOT NULL,
    state CHAR(3) NOT NULL,
    zip CHAR(10) NOT NULL
);

DROP TABLE IF EXISTS identification_codes;
CREATE TABLE identification_codes (
	employee_id INT PRIMARY KEY,
    job_id INT, 
    department_id INT
	
);

DROP TABLE IF EXISTS contact; 
CREATE TABLE contact (
	employee_id INT NOT NULL PRIMARY KEY, 
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL,
    website VARCHAR(50)
);

DROP TABLE IF EXISTS job_description; 
CREATE TABLE job_description (
	job_id INT NOT NULL, 
    job_title VARCHAR(50) NOT NULL, 
    job_description VARCHAR(400) NOT NULL
);

DROP TABLE IF EXISTS job_profile;
CREATE TABLE job_profile (
	employee_id INT NOT NULL PRIMARY KEY,
	start_date DATE NOT NULL,
    years_company INT NOT NULL,
    job_salary INT,
    benefits VARCHAR(20) NOT NULL,
    employment_status VARCHAR(20) NOT NULL
);

DROP TABLE IF EXISTS department; 
CREATE TABLE department (
	department_id INT,
	department VARCHAR(20) NOT NULL
);



