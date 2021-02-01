-- RDFMT8: Outer Join Between Multiple Tables
-- Write a query that produces the columns:
-- order date, order id, first name, shipper (null if not shipped), status

USE sql_store;

SELECT o.order_date AS date, 
       o.order_id, 
       c.first_name AS customer,  
       s.name AS shipper, 
       os.name AS status
FROM orders o
LEFT JOIN customers c
    ON o.customer_id = c.customer_id
LEFT JOIN shippers s
    ON o.shipper_id = s.shipper_id
LEFT JOIN order_statuses os
    ON o.status = os.order_status_id;

