-- Get the orders placed  this year
select * 
from sql_store.orders
where order_date >= '2019-01-01'