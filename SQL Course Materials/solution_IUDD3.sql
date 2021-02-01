-- IUDD3: Inserting Multiple Rows
-- Insert three rows in the products table.

USE sql_store;

SELECT * FROM products;

INSERT INTO products (name, quantity_in_stock, unit_price)
VALUES ('Clone Troopers', 99, 5.55),
	   ('Dad', 1, 36.00),
       ('Frogs', 69, 3.86);

SELECT * FROM products;