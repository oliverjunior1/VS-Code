SELECT * FROM Employee e;

SELECT c.FirstName, c.LastName FROM Customer c 
WHERE Company IS NULL AND c.FirstName IN 
(SELECT FirstName FROM Employee e );

-- Quais dos clientes são colaboradores?

SELECT c.FirstName, c.LastName FROM Customer c INNER JOIN Employee e 
WHERE c.FirstName = e.FirstName;