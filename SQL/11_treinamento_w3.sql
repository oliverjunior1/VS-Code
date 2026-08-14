SELECT * FROM actor;
SELECT actor_id, first_name FROM actor;
SELECT DISTINCT last_name FROM actor;
SELECT DISTINCT COUNT(last_name) FROM actor;
SELECT first_name FROM 	actor;
SELECT COUNT(*) AS actor_id FROM (SELECT DISTINCT actor_id FROM actor);
SELECT * FROM actor WHERE actor_id=1;
SELECT * FROM city WHERE city_id>30;
SELECT * FROM city ORDER BY city_id DESC;
SELECT * FROM payment ORDER BY amount ASC;
SELECT * FROM payment WHERE rental_id>1 AND amount>10;
SELECT * FROM film_actor WHERE actor_id>10 OR film_id >10;
SELECT * FROM city WHERE city_id>15 AND city like 'B%';
SELECT * FROM city WHERE city NOT LIKE 'B%' AND city NOT LIKE 'C%';
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode Country) 
VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');

