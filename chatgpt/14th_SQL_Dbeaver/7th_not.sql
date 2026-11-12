SELECT * FROM Customers
WHERE NOT Country='Germany';

SELECT * FROM Customers
WHERE Country='Germany' AND (City='Berlin' OR City='Stutgard');

SELECT * FROM Customers
WHERE NOT Country='Germany' AND NOT Country='USA';

SELECT * FROM Customers
WHERE CustomerName NOT LIKE 'A%';

SELECT * FROM Customers
WHERE CustomerID NOT BETWEEN 10 AND 60;