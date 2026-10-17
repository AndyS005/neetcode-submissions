-- Write your query below
SELECT seller_name FROM seller LEFT JOIN orders 
ON seller.seller_id = orders.seller_id
AND EXTRACT(YEAR FROM sale_date) = 2020
WHERE orders.order_id IS NULL
ORDER BY seller_name
