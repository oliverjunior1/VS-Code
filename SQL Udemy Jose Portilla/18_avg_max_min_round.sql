SELECT * FROM film;

SELECT MIN(replacement_cost) FROM film;

-- Show only one result the max here and the minimun there
SELECT MAX(replacement_cost) FROM film;

SELECT COUNT(film_id) FROM film;

-- Show the average
SELECT AVG(replacement_cost) FROM film;

-- This number shows how much numeral number will be
SELECT ROUND(AVG(replacement_cost),2) FROM film;





