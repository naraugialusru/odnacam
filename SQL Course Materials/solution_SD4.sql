-- SD4: The ROLLUP Operator
-- Write a query to produce
-- a table with columns:
-- payment_method, total
-- with rows = individual payment methods, and total.

USE sql_invoicing;

SELECT COALESCE(pm.name, 'All Methods') as payment_method,
       SUM(p.amount) as amount_paid
FROM payments p
JOIN payment_methods pm
	ON p.payment_method = pm.payment_method_id
GROUP BY pm.name WITH ROLLUP





