-- SELECT CustomerID AS ID, CustomerName AS Customer
-- FROM Customers;

-- SELECT ProductName AS [My Great Products]
-- FROM Products;

-- SELECT ProductName AS "My Great Products"
-- FROM Products;

-- SELECT CustomerName, CONCAT(Address,', ',PostalCode,', ',City,', ',Country) AS Address
-- FROM Customers;

-- SELECT * FROM Customers AS Persons;

SELECT c.CustomerName, o.OrderID
FROM customers AS c
JOIN orders AS o ON c.customerID = o.customerID;