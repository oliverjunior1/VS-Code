SELECT * FROM Customers
WHERE NOT Country='Germany';

SELECT * FROM Customers
WHERE Country='Germany' AND (City='Berlin' OR City='Stutgard');

SELECT * FROM Customers
WHERE NOT Country='Germany' AND NOT Country='USA';
