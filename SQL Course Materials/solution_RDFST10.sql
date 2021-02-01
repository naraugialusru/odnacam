-- RDFST10: The ORDER BY Operator
-- Write a query to select all items from the order_items table with order id 2.
-- Sort them in descending order by total price.

SELECT *, unit_price * quantity
FROM sql_store.order_items
WHERE order_id = 2
ORDER BY unit_price * quantity DESC;
