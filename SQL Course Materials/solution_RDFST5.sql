-- Return products with
--     quantity in stock equal to 49, 38, 72

SELECT * 
FROM sql_store.products
WHERE quantity_in_stock IN (49, 38, 72);