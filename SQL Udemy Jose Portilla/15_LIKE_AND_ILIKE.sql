SELECT * FROM customer
WHERE first_name LIKE 'J%';

SELECT COUNT(*) FROM customer
WHERE first_name LIKE 'J%';

SELECT * FROM customer
WHERE first_name LIKE 'J%' AND last_name LIKE 'S%';

-- ILIKE ISN'T CASE SENSITIVE, AND LIKE IS CASE SENSITIVE
SELECT * FROM customer
WHERE first_name ILIKE 'j%' AND last_name ILIKE 's%';

-- Had er in someplace
SELECT * FROM customer
WHERE first_name LIKE '%er%';

-- Indicate a position of any character
SELECT * FROM customer
WHERE first_name LIKE '_her%';

SELECT * FROM customer
WHERE first_name LIKE 'A%' AND last_name NOT LIKE 'B%'
ORDER BY last_name;





