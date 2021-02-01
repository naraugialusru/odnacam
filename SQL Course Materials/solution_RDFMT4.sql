-- RDFMT4: Joining Multiple Tables
-- Join the sql_invoicing payments table
-- with the clients table
-- and these with the payment methods table.
-- Show the client name, and the payment method

SELECT p.date, p.invoice_id, p.amount, c.name, pm.name 
FROM sql_invoicing.clients c
     JOIN sql_invoicing.payments p
	 ON c.client_id = p.client_id
     JOIN sql_invoicing.payment_methods pm  
     ON p.payment_method = pm.payment_method_id
     ORDER BY p.date;