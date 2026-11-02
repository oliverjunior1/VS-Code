SELECT * FROM Customers
WHERE Country='UK' AND City='London';

-- AND OR
SELECT * FROM Customers
WHERE Country='Germany' AND (City='Stuttgard' OR City='Berlin');