-- RDFMT10: The USING clause
-- Make a query that produces:
-- date, client, amount, name (aka payment method)

USE sql_invoicing;

SELECT p.date, c.name AS client, p.amount, pm.name
FROM payments as p
JOIN clients as c
    ON p.client_id = c.client_id
JOIN payment_methods as pm
    ON p.payment_method = pm.payment_method_id;

