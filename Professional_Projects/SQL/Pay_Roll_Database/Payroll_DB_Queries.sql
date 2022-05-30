USE payroll_db;

SELECT emp.employee_id, ic.job_id, ic.department_id, first_name, last_name
FROM employees emp
	JOIN identification_codes ic
		ON emp.employee_id = ic.employee_id
	JOIN job_profile jp
		ON ic.job
        
#USE payroll_db;

#DROP VIEW IF EXISTS employee_data;
#CREATE VIEW employee_data AS
#SELECT emp.employee_id, emp.first_name, emp.last_name, jp.job_title, jp.start_date, jp.years_company
#FROM identification_codes ic
	#INNER JOIN employees emp
		#ON emp.employee_id = ic.employee_id
	#INNER JOIN job_profile jp 
		#ON ic.job_id = jp.job_id
	#INNER JOIN department d
		#ON ic.department_id = d.department_id;

#SELECT *
#FROM employee_data
