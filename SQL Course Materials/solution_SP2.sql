-- SP2: Creating a Stored Proceedure
-- Create a stored proceedure called 
-- get_invoices_with_balance
-- that returns all invoices with a balance > 0

USE sql_invoicing;

DELIMITER $$

CREATE PROCEDURE get_invoices_with_balance()
BEGIN
SELECT *, invoice_total - payment_total AS balance
FROM invoices
WHERE invoice_total - payment_total > 0;
END$$

DELIMITER ;

get_invoices_with_balance()


