USE payroll_db;

DROP TABLE IF EXISTS temp_employee_profile;
CREATE TEMPORARY TABLE IF NOT EXISTS temp_employee_profile AS
SELECT emp.employee_id, jd.job_title, d.department, emp.first_name, emp.last_name, jp.start_date, 
	   jp.years_company, jp.employment_status, jp.job_salary
FROM employees emp
	JOIN identification_codes ic
		ON emp.employee_id = ic.employee_id
	 JOIN job_profile jp 
		ON emp.employee_id = jp.employee_id
	 JOIN department d
		ON ic.department_id = d.department_id
	 JOIN job_description jd
		ON ic.job_id = jd.job_id
GROUP BY emp.employee_id
LIMIT 5000;



SET @Annual_Budget = (SELECT SUM(job_salary) AS Annual_Budget FROM temp_employee_profile);
SET @BiWeekly_Budget = (SELECT ROUND((SUM(job_salary) / 12)/2, 2) BiWeekly_Budget FROM temp_employee_profile);
SET @Row_num := 0;

DROP TABLE IF EXISTS Calender;
CREATE TABLE Calender (
	WeekNumber INT,
    Week_Start DATE,
    WeekEnd DATE,
    Sales INT
    
);
INSERT INTO Calender
(SELECT @Row_num:= @Row_num + 1 WeekNumber, 
	   @start_date as Week_Start, 
       @start_date := date_add(@start_date, interval 2 week) AS WeekEnd,
	   Round(RAND()*(50000000-@BiWeekly_Budget)+15000000, 2) as Sales
FROM (SELECT @start_date := '2021-01-01') temp, employees
LIMIT 26);

#SELECT * FROM calender;

DELIMITER //

DROP PROCEDURE IF EXISTS payroll //
CREATE PROCEDURE payroll()
BEGIN
	DECLARE i INT DEFAULT 0;
    DECLARE total_employees INT;
    DECLARE Profit_Loss INT;
    DECLARE Employees_removed INT;
    DECLARE Total_Employees_Remaining INT;
    DECLARE New_BiWeekly_Payout INT;
    DECLARE BiWeekly_Budget INT;
    
    SET total_employees = (SELECT COUNT(*) FROM temp_employee_profile);
    
    DROP TABLE IF EXISTS money;
    CREATE TABLE money (
    WeekNumber INT,
	BiWeekly_Payout INT Default 0,
    Profit_Loss INT Default 0,
	Employees_removed INT Default 0, 
    Total_Employees_Remaining INT Default 0,
    New_BiWeekly_Payout INT Default 0
    );
    
    
    WHILE i < 26 DO
		SET BiWeekly_Budget = (SELECT ROUND((SUM(job_salary) / 12)/2, 2) FROM temp_employee_profile);
		SET Profit_Loss = (SELECT Sales FROM Calender LIMIT i, 1) - (BiWeekly_Budget);
        
        IF Profit_Loss < 0 THEN 
			DELETE FROM temp_employee_profile ORDER BY RAND() LIMIT 10;
		END IF;
        
        SET Employees_removed = total_employees - (SELECT COUNT(*) FROM temp_employee_profile);
        SET Total_Employees_Remaining = (SELECT COUNT(*) FROM temp_employee_profile
        );
        SET New_BiWeekly_Payout = (SELECT ROUND((SUM(job_salary) / 12)/2, 2) FROM temp_employee_profile);
        SET i = i+ 1;
        
        INSERT INTO money (WeekNumber, BiWeekly_Payout, Profit_Loss, Employees_removed, Total_Employees_Remaining, New_BiWeekly_Payout) 
        VALUES (i, BiWeekly_Budget, Profit_Loss, Employees_removed, Total_Employees_Remaining, New_BiWeekly_Payout);
		
	END WHILE;
    SELECT * FROM money;
END //

DELIMITER ;
CALL payroll();



   