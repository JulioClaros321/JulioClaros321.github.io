SET GLOBAL log_bin_trust_function_creators = 1;
USE lab; 

#INSERT FUNCTION
INSERT INTO lab.customers
VALUES 
	(1, "Julio", "Claros", 20),
    (2, "Ronald", "Hernandez", 21),
    (3, "Deisy", "Ketchum", 22); 

INSERT INTO lab.shipping_address
VALUES
	(1, 4322, "Wayne Ave", "MD", 20932),
    (2, 4655, "University blvd", "CA", 20343),
    (3, 2134, "Sun Ave", "CA", 20123);

INSERT INTO lab.order_items
VALUES 
	(20, 466, "A+ Student Kit", "2012-03-21", "Yes"),
    (21, 488, "F- Student Kit", "2012-03-22", "No"),
    (22, 466, "A+ Student Kit", "2013-04-23", "Yes"),
    (20, 488, "F- Student Kit", "2012-03-21", "Yes");

#Alter table
UPDATE lab.order_items
SET adult = "Yes"
WHERE order_id = 21;


#ALTER TABLE lab.order_items
#DROP adult;

#Select With JOIN
SELECT customers.id, first_name, last_name, item_number, zip_code
FROM lab.customers 
	INNER JOIN lab.order_items 
		ON customers.order_id = order_items.order_id
	INNER JOIN lab.shipping_address 
		ON customers.id = shipping_address.id;

#Union Operator
SELECT first_name FROM lab.customers
UNION
SELECT item_name FROM lab.order_items;

#View
DROP VIEW IF EXISTS cali_orders;
CREATE VIEW cali_orders AS
SELECT first_name, last_name, state
FROM lab.customers JOIN lab.shipping_address
	ON customers.id = shipping_address.id
WHERE state = "CA";

#FUNCTION 
DELIMITER //
DROP FUNCTION IF EXISTS total_orders//
CREATE FUNCTION total_orders (order_id_param INT) 
RETURNS INT
BEGIN
	DECLARE  order_count  INT;
    SELECT COUNT(*)
    INTO order_count
    FROM lab.order_items
    WHERE lab.order_items.order_id = order_id_param;
	RETURN order_count;
END //
DELIMITER ;


#DELETE STATMENT
DELETE FROM lab.order_items
WHERE order_id = 21;


