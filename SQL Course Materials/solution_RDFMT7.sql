-- RDFMT7: Outer Joins
-- Write a query that produces 
-- product_id, name (of the product), quantity (possibly NULL)

USE sql_store;

SELECT p.product_id, p.name, oi.quantity
FROM  products p
LEFT JOIN order_items oi
ON p.product_id = oi.product_id