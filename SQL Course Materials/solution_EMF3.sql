-- EMF3: Date Functions in MySQL
-- Write a query to select all orders in the year two years ago.

USE sql_store;

SELECT *
FROM orders
WHERE YEAR(order_date) = YEAR(NOW()) - 2



