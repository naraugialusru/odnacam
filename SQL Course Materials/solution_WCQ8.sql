-- WCQ8: The EXISTS Operator
-- Find the products that have never been ordered.

USE sql_store;

SELECT *
FROM products p 
WHERE NOT
EXISTS (SELECT order_items.product_id
			  FROM order_items
              WHERE p.product_id = order_items.product_id)
