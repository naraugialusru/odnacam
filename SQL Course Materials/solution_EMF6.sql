-- EMF6: The IFNULL and COALESCE Functions
-- Display Full Name and Phone Number of customers.
-- If a Phone Number is NULL, then display UNKNOWN

USE sql_store;

SELECT CONCAT(first_name, ' ', last_name) AS full_name
	   , COALESCE(phone, 'Unknown') as phone
FROM CUSTOMERS



