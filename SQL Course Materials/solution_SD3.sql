-- SD3: The HAVING clause
-- Get the customers located in Virginia
-- who have spent more than $100

USE sql_store;

SELECT -- *, 
       c.first_name,
	   c.last_name,
       SUM(quantity * unit_price) AS total_sales
FROM customers c
JOIN orders o USING (customer_id)
JOIN order_items oi USING (order_id)
	WHERE c.state = 'VA'
GROUP BY c.first_name, c.last_name
	HAVING total_sales > 100



