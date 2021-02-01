-- SD2: The GROUP BY clause
-- collect total_payment on
-- a GROUP BY on the payments table
-- in the sql_invoicing database.

USE sql_invoicing;

SELECT date, 
	   pm.name, 
       SUM(amount) AS total_payment
FROM payments p
JOIN payment_methods pm
	ON p.payment_method = pm.payment_method_id
GROUP BY date, pm.name
ORDER BY date, total_payment DESC;




