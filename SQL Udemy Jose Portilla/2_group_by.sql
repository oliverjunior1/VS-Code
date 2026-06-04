/*
SELECT vendedor,
       SUM(valor) AS total_vendas
FROM vendas
GROUP BY vendedor;

*/
--ALTER TABLE vendas RENAME COLUMN produto TO nome_produto;

--SELECT * FROM vendas;

--ALTER TABLE vendas RENAME COLUMN produto TO nome_produto;

SELECT vendedor, COUNT(*) AS quantidade FROM vendas GROUP BY vendedor;