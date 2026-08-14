SELECT * FROM customer LIMIT 10;
SELECT customer_id, COUNT(*) AS Total FROM Customer GROUP BY 1;


-- Verificar se há customer_id null
SELECT * FROM Customer WHERE customer_id IS NOT null;
SELECT COUNT(*) FROM Customer WHERE customer_id IS NOT null;
