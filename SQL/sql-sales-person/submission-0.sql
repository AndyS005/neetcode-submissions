-- Write your query below
SELECT name FROM sales_person WHERE sales_id NOT IN 
(
    SELECT sales_id FROM orders LEFT JOIN company 
    ON company.com_id = orders.com_id
    WHERE company.name = 'CRIMSON'
)