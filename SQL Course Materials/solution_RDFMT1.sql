-- RDFMT1:Inner Joins
-- Write a query to join the order_items table with the products table.
-- Return both the product id as well as its name followed by the quantity and the unit price from the order items table.
-- Use an alias to simplify the code.

SELECT order_id, items.product_id, name, quantity, items.unit_price
FROM      sql_store.order_items AS items 
     JOIN sql_store.products AS products
ON items.product_id = products.product_id;

