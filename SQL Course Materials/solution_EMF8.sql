-- EMF8: The CASE Operator
-- Write the customer-points-category table
-- Using the CASE operator

USE sql_store;

SELECT CONCAT(first_name, ' ', last_name) AS name
     , points
     , CASE
			WHEN points > 3000 THEN 'Gold'
            WHEN points BETWEEN 2000 AND 3000 THEN 'Silver'
            ELSE 'Bronze'
		END
		AS category
FROM customers
ORDER BY points DESC




