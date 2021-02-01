-- SD1: Aggregate Functions
-- Write a query to generate a summary of the invoices table
-- with columns: date_range, total_sales, total_payments, what_we_expect
-- and rows: 'First half of 2019', 'Second half of 2019', 'Total'

USE sql_invoicing;

SELECT *
FROM invoices;

SELECT 
	'First half of 2019' AS date_range,
	SUM(invoice_total) AS total_sales,
	SUM(payment_total) AS total_payments,
    SUM(invoice_total - payment_total) AS what_we_expect
FROM invoices
WHERE invoice_date 
	BETWEEN '2019-1-1' AND '2019-6-2'
UNION
SELECT 
	'Second half of 2019' AS date_range,
	SUM(invoice_total) AS total_sales,
	SUM(payment_total) AS total_payments,
    SUM(invoice_total - payment_total) AS what_we_expect
FROM invoices
WHERE invoice_date 
	BETWEEN '2019-6-3' AND '2019-12-31'
UNION
SELECT 
	'Total' AS date_range,
	SUM(invoice_total) AS total_sales,
	SUM(payment_total) AS total_payments,
    SUM(invoice_total - payment_total) AS what_we_expect
FROM invoices
WHERE invoice_date 
	BETWEEN '2019-1-1' AND '2019-12-31';


