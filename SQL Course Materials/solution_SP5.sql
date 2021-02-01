-- SP5: Parameters
-- Write a stored procedure to return invoices
-- for a given client
--
-- get_invoices_by_client

USE sql_invoicing;

DELIMITER $$

CREATE PROCEDURE get_invoices_by_client
(
	client CHAR(50)
)
BEGIN
SELECT *
FROM invoices
WHERE client_id IN (SELECT client_id FROM clients WHERE name = client);
END$$

DELIMITER ;


