#Julio Claros

#Question 1
DROP TABLE IF EXISTS address_copy;
DROP TABLE IF EXISTS order_copy;

CREATE TABLE address_copy AS
SELECT *
FROM my_guitar_shop.addresses;

CREATE TABLE order_copy AS
SELECT *
FROM my_guitar_shop.orders;




#Question 2
INSERT INTO my_guitar_shop.addresses VALUES
	(DEFAULT, 6, "12765 Jefferson Str", "Apt. 217", "College Park", "MD", "20742", "301-217-8888", 0);
    


#Question 3
INSERT INTO my_guitar_shop.orders
	(order_id, customer_id, order_date, ship_amount, tax_amount, ship_date,
    ship_address_id, card_type, card_number, card_expires, billing_address_id)
VALUES
	(DEFAULT, 6, "2017-09-25:11:35:18", 5, 0, NOW(), 13, "Visa", "1234567890123456", "06/2020", 8);


#Question 4
UPDATE my_guitar_shop.orders
SET tax_amount = 4.20, card_type = "Mastercard"
WHERE ship_address_id = 13;

#Question 5
UPDATE my_guitar_shop.addresses
SET disabled = 1
WHERE state = "CA";

#Question 6
DELETE FROM my_guitar_shop.orders
WHERE ship_address_id = 13;

DELETE FROM my_guitar_shop.addresses
WHERE address_id = 13;

