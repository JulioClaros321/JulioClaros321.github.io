DROP DATABASE IF EXISTS assign_four; 
CREATE DATABASE assign_four; 
USE assign_four;

DROP TABLE IF EXISTS customers;
CREATE TABLE customers ( 
	name		VARCHAR(20),
    last_name	VARCHAR(20), 
    age			INT, 
    phone_numb	VARCHAR(12),
    email		VARCHAR(30),
    street_numb	INT,
    street		VARCHAR(20),
    city		VARCHAR(15),
    state		CHAR(2),
    zip_code	INT
); 

DROP TABLE IF EXISTS aggregateData;
CREATE TABLE aggregateData ( 
	theDate		DATE,
    theTime		TIME,
    totalCustomers		INT, 
    meanAge		INT
);

#INSERT INTO assign_four.customers
#VALUES
	#("Julio", "Claros", 21, "301-580-3642", "julio.claros321@gmail.com", 123, "Street", "Silver Spring", "MD", 20901),
    #("Ronald", "Hernandez", 18, "301-796-4040", "R.Hernandez@gmailcom", 4323, "Sligo Way", "Silver Spring", "MD", 20394), 
    #("David", "Yeezy", 31, "401-304-3020", "David.Y21@yahoo.com", 321, "Wayne Ave.", "Chevy Chase", "MD", 34031), 
    #("Fifa", "Champion", 30, "312-391-2121", "Chamption.F123@gmail.com", 432, "Give Me An A Strre", "Please", "MD", 20310),
    #("Ronny", "Lel", 16, "301-432-1313", "Lel_Ronny@gmail.com", 523, "Loft Lane", "Clarksburg", "CA", 23232)
    
    


DELIMITER //
DROP PROCEDURE IF EXISTS totalCustomers//
CREATE PROCEDURE totalCustomers()
BEGIN
	INSERT INTO assign_four.aggregateData (theDate, theTime, totalCustomers) 
    VALUES
		(CURDATE(), CURRENT_TIME(), (SELECT COUNT(*) 
									 FROM assign_four.customers));
END //


DELIMITER //
DROP TRIGGER IF EXISTS customer_update//
CREATE TRIGGER customer_update 
	AFTER INSERT ON assign_four.customers
    FOR EACH ROW
BEGIN
	INSERT INTO assign_four.aggregateData (theDate, theTime, meanAge) 
    VALUES
		(CURDATE(), CURRENT_TIME(), (SELECT AVG(age) 
									 FROM assign_four.customers));
END //




    
