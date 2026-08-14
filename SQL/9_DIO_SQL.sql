SELECT * FROM actor;
SELECT COUNT(*) AS first_name FROM actor;
SELECT actor_id, first_name FROM actor WHERE actor_id is NULL;
SELECT COUNT(*) FROM actor WHERE actor_id IS NULL;
SELECT address2, address FROM address WHERE address2 IS NULL;
SELECT COUNT(*) FROM address;
SELECT * FROM film INNER JOIN film_actor;
