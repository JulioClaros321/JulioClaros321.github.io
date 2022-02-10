DROP DATABASE IF EXISTS lab; 
CREATE DATABASE lab; 
USE lab; 

DROP TABLE IF EXISTS customers; 
CREATE TABLE customers ( 
	id				INT,
    first_name 		VARCHAR(20), 
    last_name		VARCHAR(20), 
    order_id		INT,
	PRIMARY KEY(id),
    CONSTRAINT UNIQUE(order_id) 
); 

DROP TABLE IF EXISTS shipping_address; 
CREATE TABLE shipping_address (  
	id				INT,
    street_numb		INT,
    street			VARCHAR(30), 
    state			CHAR(2), 
    zip_code		INT,
	FOREIGN KEY(id) REFERENCES customers(id)
);

DROP TABLE IF EXISTS order_items;
CREATE TABLE order_items ( 
	order_id		INT, 
    item_number		INT, 
    item_name		VARCHAR(30), 
    order_date		DATE,
    adult			CHAR(3),
    FOREIGN KEY (order_id) REFERENCES customers(order_id) 
); 




    
    