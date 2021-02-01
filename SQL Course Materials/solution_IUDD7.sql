-- IUDD8: Using Subqueries in Updates
-- For customers whose number of points is greater than 3000
-- and who have an order, add the comment "Gold" to their order
-- comments section.

USE sql_store;

UPDATE orders
SET  comments = 'Gold customer, ' + comments
WHERE customer_id IN
	(
	SELECT DISTINCT o.customer_id 
	FROM customers c
	JOIN orders o
		ON c.customer_id = o.customer_id
	WHERE c.points > 3000
	)