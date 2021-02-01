-- WCQ3: The IN Operator
-- Find clients without invoices

USE sql_invoicing;

SELECT name
FROM clients 
WHERE client_id NOT IN
	(
	SELECT DISTINCT client_id 
	FROM invoices
	)	





