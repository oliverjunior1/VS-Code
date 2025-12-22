-- How many payment transactions were greater than $5.00?
SELECT COUNT(amount) FROM payment WHERE amount > 5.99;

-- How many actors havea fist name thats starts  with the letter P?
SELECT COUNT(first_name) FROM actor WHERE first_name LIKE 'P%';

-- How many unique districts are our customers from?
SELECT COUNT(DISTINCT(district)) FROM address;

-- Retrieve the list of namesfo those distinct districts from the previous question.
SELECT DISTINCT(district) FROM address;

-- How many films have a rating of R and a replacement cost between $5 and $15?
SELECT COUNT(*) FROM film WHERE replacement_cost BETWEEN 5 AND 15 AND rating = 'R';

-- How many films have the word Truman womewhere in the title?
SELECT COUNT(*) FROM film WHERE title LIKE '%Truman%';