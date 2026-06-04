/*CREATE TABLE vendas_produtos (
    produto VARCHAR(50),
    vendas INT
);*/
/*
INSERT INTO vendas_produtos (produto, vendas)
VALUES
('Mouse', 100),
('Mouse', 150),
('Teclado', 200),
('Monitor', 500),
('Monitor', 300);*/

-- 1. Total vendido por produto.
--SELECT SUM(vendas) FROM vendas_produtos;
/*SELECT produto,
       SUM(vendas) AS total_vendido
FROM vendas_produtos
GROUP BY produto;*/

-- 2. Média por produto.
/*SELECT produto,
       AVG(vendas) AS media_vendas
FROM vendas_produtos
GROUP BY produto;*/

--3. Maior venda por produto.
/*SELECT produto,
       MAX(vendas) AS maior_venda
FROM vendas_produtos
GROUP BY produto;*/

--4. Produtos com total acima de 400.
SELECT produto FROM vendas_produtos WHERE vendas > 400 GROUP BY produto;