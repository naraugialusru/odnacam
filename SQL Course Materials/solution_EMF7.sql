-- EMF7: The IF function
-- Write a query to produce a table with columns
-- product_id, name (aka product_name), orders (the number of orders the product appears in), frequency ('Once' or 'Many times')

USE sql_store;

SELECT p.product_id
	 , p.name
     , COUNT(*) AS orders
     , IF(COUNT(*) > 1, 'Many Times', 'Once') AS frequency
FROM products p
JOIN order_items oi USING (product_id)
GROUP BY p.product_id, p.name




