SELECT CustomerName, City, Country FROM Customers;

SELECT DISTINCT Country FROM Customers;

-- In that case the exit is 21
SELECT COUNT(DISTINCT Country) FROM Customers;

-- In that case the exit is 91 because repeat a lot of countries
SELECT COUNT(Country) FROM Customers;

CREATE TABLE vendas (
    id_venda INT PRIMARY KEY,
    cliente VARCHAR(50),
    produto VARCHAR(50),
    cidade VARCHAR(50),
    categoria VARCHAR(50)
);



