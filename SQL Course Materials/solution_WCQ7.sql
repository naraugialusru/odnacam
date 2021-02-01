-- WCQ7: Correlated Subqueries
-- Get invoices that are larger than 
-- the client's average amount

USE sql_invoicing;

SELECT AVG(invoice_total) FROM invoices;

SELECT *
FROM invoices
	WHERE invoice_total > (SELECT AVG(invoice_total) FROM invoices)




