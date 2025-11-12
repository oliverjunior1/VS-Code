SELECT * FROM payment
LIMIT 2;
SELECT DISTINCT(amount) FROM payment
ORDER BY amount;
SELECT COUNT(*) FROM payment WHERE amount IN (0.99,1.98, 1.99);
SELECT * FROM customer WHERE first_name IN ('John', 'Jake', 'Julie');