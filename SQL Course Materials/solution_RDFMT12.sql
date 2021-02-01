-- RDFMT12: Cross Joins
-- Do a cross join between shippers and products
-- using the implicit syntax
-- and then using the explicit syntax.

USE sql_store;

SELECT shippers.name AS shipper,
	   products.name AS product
FROM products, shippers
ORDER BY shippers.name;

SELECT shippers.name AS shipper,
	   products.name AS product
FROM products
CROSS JOIN shippers
ORDER BY shippers.name;

