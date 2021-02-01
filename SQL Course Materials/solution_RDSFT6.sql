-- Return customers born
--                  between 1/1/1990 and 1/1/2000

SELECT * 
FROM sql_store.customers
-- ORDER BY birth_date;
WHERE birth_date > '1990-1-1' AND birth_date < '2000-1-1';