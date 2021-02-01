-- IUDD5: Creating a Copy of a Table
-- Make a copy of the invoices table with
-- the client_id replaced with the client name
-- and only non-null payment dates included

USE sql_invoicing;

DROP TABLE invoices_archive;
CREATE TABLE invoices_archive AS
SELECT invoice_id, 
	   number, 
       c.name, 
       invoice_total, 
       payment_total,
       due_date, 
       payment_date
FROM invoices iv
JOIN clients c
    ON iv.client_id = c.client_id
WHERE NOT payment_date IS NULL;

SELECT * FROM invoices_archive;