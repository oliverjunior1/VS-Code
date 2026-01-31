-- How many payment transactions were greater than $5.00?
SELECT * FROM payment WHERE amount >= 5;

-- How many actors have the fist name thats starts  with the letter P?
SELECT COUNT(*) FROM actor WHERE first_name LIKE 'P%';

-- How many unique districts are our customers from?
SELECT COUNT(DISTINCT address_id) FROM customer;

-- Retrieve the list of names for those distinct districts from the previous question.
SELECT DISTINCT address_id FROM customer;

-- How many films have a rating of R and a replacement cost between $5 and $15?


-- How many films have the word Truman womewhere in the title?
