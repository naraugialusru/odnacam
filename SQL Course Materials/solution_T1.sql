-- T1: Triggers
-- Create as trigger that gets fired when we 
-- delete a payment.

USE sql_invoicing;

DROP TRIGGER IF EXISTS correct_invoices_after_payment_deletion;

DELIMITER $$

USE sql_invoicing$$

CREATE TRIGGER correct_invoices_after_payment_deletion
	AFTER DELETE ON payments
    FOR EACH ROW
BEGIN
	UPDATE invoices
    SET payment_total = payment_total - OLD.amount
	WHERE invoice_id = OLD.invoice_id;
END$$



DELIMITER ;

