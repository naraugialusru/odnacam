-- WCQ9: Subqueries in the SELECT Clause
-- Write a query to produce a table with columns
-- client_id, name, total_sales, average, difference
-- where average is the average is the average of all sales
-- and the difference is the difference between the total and average

USE sql_invoicing;

SELECT c.client_id
       , c.name 
       , (SELECT SUM(invoice_total) FROM invoices WHERE client_id = c.client_id) AS total_sales
       , (SELECT AVG(invoice_total) FROM invoices) AS average
       , (SELECT total_sales - average)
FROM clients c

