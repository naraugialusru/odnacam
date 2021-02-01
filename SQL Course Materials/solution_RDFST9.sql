-- RDFST9: The IS NULL Operator
-- Get the orders that are not shipped

SELECT *
FROM sql_store.orders
WHERE shipped_date IS NULL