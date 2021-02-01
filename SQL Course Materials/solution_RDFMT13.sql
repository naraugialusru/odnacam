-- RDFMT13: Unions
-- Write a query with columns:
-- customer_id, first_name, points, type
-- where type is Bronze (< 2000), Silver (2000--3000) or Gold (> 3000)

USE sql_store;

SELECT customer_id, first_name, points, 'GOLD' as type
FROM customers
WHERE points > 3000
UNION
SELECT customer_id, first_name, points, 'SILVER' as type
FROM customers
WHERE points BETWEEN 3000 AND 2000
UNION
SELECT customer_id, first_name, points, 'BRONZE' as type
FROM customers
WHERE points < 2000
ORDER BY points DESC