-- How many payment transactions were greater than U$ 5.00?
SELECT COUNT(amount) FROM payment
WHERE amount > 5;

-- How many actors have a fist name that starts with the letter P?
SELECT COUNT(first_name) FROM actor
WHERE first_name LIKE 'P%';

-- How many unique districts are our costumers from?
-- Retrieve the list of names for those districts from the previous question?
-- How many films have a rating of R and a replacement cost between $5 and $15?
-- How many films have the word Truman somewhere in the title?