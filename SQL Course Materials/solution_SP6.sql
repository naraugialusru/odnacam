-- SP6: Write a stored procedure called get_payments
-- with two parameters
--
-- client_id => INT
-- payment_method => TINYINT(1)

DROP PROCEEDURE IF EXISTS get_clients_by_state

DELIMITER $$

USE sql_invoicing$$

CREATE PROCEDURE get_payments 
	(
		client_id INT
	  , payment_method TINYINT
    )
BEGIN
	SELECT *
    FROM payments p
    WHERE p.client_id = IFNULL(client_id, p.client_id) 
      AND p.payment_method = IFNULL(payment_method, p.payment_method);
END

DELIMITER ;

