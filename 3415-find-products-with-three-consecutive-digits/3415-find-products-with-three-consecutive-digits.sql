# Write your MySQL query statement below
SELECT product_id, name
from Products
where name REGEXP "[0-9]{3}" AND name NOT REGEXP '[0-9]{4,}'
order by product_id ASC