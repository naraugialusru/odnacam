-- WCQ4: Subqueries vs Joins
-- Find the customers who have ordered lettuce (id = 3)
-- Select customer_id, first_name, last_name

USE sql_store;

/*
SELECT c.customer_id,
	   c.first_name,
       c.last_name
FROM customers c
	WHERE c.customer_id IN (
		SELECT DISTINCT o.customer_id 
		FROM orders o
			WHERE o.customer_id IN (
				SELECT DISTINCT oi.order_id
				FROM order_items oi
					WHERE oi.product_id IN (
						SELECT DISTINCT p.product_id 
						FROM products p
							WHERE p.name LIKE '%Lettuce%'
					)
            )
	)

*/

SELECT DISTINCT c.customer_id,
	            c.first_name,
                c.last_name
FROM customers c
JOIN orders o USING (customer_id)
JOIN order_items oi USING (order_id)
JOIN products p USING (product_id)
	WHERE p.name LIKE '%Lettuce%';



