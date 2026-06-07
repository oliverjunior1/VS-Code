-- CREATE TABLE produtos (
-- 	produto VARCHAR(50),
-- 	valor INT
-- );

-- INSERT INTO produtos (produto, valor)
-- VALUES
-- ('Mouse', 100),
-- ('Mouse',150),
-- ('Monitor', 500);

-- o total vendido por produto.

SELECT produto, SUM(valor) AS total_vendido FROM produtos GROUP BY produto;