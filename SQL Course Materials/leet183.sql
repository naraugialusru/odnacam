-- Write a query to find customers with more than
-- 1000 points.

-- Use the EXPLAIN statement
-- Create an index on "this column" and compare the result

USE sql_store;

EXPLAIN
SELECT customer_id
FROM customers
WHERE points > 1000;

CREATE INDEX idx_points ON customers (points);

SELECT *
FROM customers

