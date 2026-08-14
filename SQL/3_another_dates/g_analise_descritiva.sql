SELECT * FROM Invoice i LIMIT 10;
SELECT * FROM InvoiceLine il LIMIT 10;
SELECT * FROM InvoiceLine il ORDER BY Quantity DESC LIMIT 10;

SELECT UnitPrice, COUNT(*) AS Record FROM InvoiceLine il ORDER BY UnitPrice;

SELECT * FROM InvoiceLine il INNER JOIN Invoice i LIMIT 2;
SELECT i.CustomerId, COUNT(*) AS Record FROM InvoiceLine il 
	INNER JOIN Invoice i 
	INNER JOIN Customer c 
	GROUP BY i.CustomerId;

SELECT * FROM Invoice i
	INNER JOIN InvoiceLine il 
	INNER JOIN Customer c ON c.CustomerId = i.CustomerId 
	LIMIT 10;
