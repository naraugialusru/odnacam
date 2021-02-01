-- RDFST11: The LIMIT Clause
-- Get the top three loyal customers

SELECT * 
FROM sql_store.customers
ORDER BY points DESC
LIMIT 3;

