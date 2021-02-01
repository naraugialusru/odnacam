-- WCQ2: Subqueries
-- In the sql_hr database
-- find the employees that make more than average

USE sql_hr;

SELECT first_name,
	   last_name,
       salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
ORDER BY salary DESC




