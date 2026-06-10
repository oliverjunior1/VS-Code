-- SELECT * FROM payment;

 -- SELECT customer_id, SUM(amount) FROM payment
 -- GROUP BY customer_id
 -- ORDER BY SUM(amount) DESC;

 -- SELECT staff_id, customer_id, SUM(amount), SUM(amount) FROM payment
 -- GROUP BY staff_id, customer_id;

 -- SELECT staff_id, customer_id, SUM(amount) FROM payment
 -- GROUP BY staff_id, customer_id
 -- ORDER BY staff_id, customer_id;

 -- SELECT staff_id, customer_id, SUM(amount) FROM payment
 -- GROUP BY staff_id, customer_id
 -- ORDER BY customer_id;
 
 SELECT staff_id, customer_id, SUM(amount) FROM payment
 GROUP BY staff_id, customer_id
 ORDER BY SUM(amount);

 