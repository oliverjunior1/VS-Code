-- Criar a tabela
-- CREATE TABLE clientes (
-- 	cliente_id INT PRIMARY KEY,
-- 	nome VARCHAR(100)
-- );

-- Inserir os registros
-- INSERT INTO clientes (cliente_id, nome)
-- VALUES
-- (1,'Ana'),
-- (2,'Pedro'),
-- (3,'Julia');

-- SELECT * FROM clientes;

-- Criar a tabela
-- CREATE TABLE pedidos(
-- 	pedido_id INT PRIMARY KEY,
-- 	cliente_id INT,
-- 	valor DECIMAL(10,2)
-- );

-- Inserir os registros
-- INSERT INTO pedidos (pedido_id, cliente_id, valor)
-- VALUES
-- (101,1,100.00),
-- (102,1,200.00),
-- (103,2,300.00);

-- SELECT * FROM pedidos;

-- SELECT
-- 	c.nome,
-- 	p.valor
-- FROM clientes c
-- INNER JOIN pedidos p
-- 	ON c.cliente_id = p.cliente_id;

-- Quando usar Left join?
-- Clientes sem pedidos
-- Produtos sem vendas
-- Funcionários sem avaliações

-- SELECT 
-- 	c.nome,
-- 	p.valor
-- FROM clientes c
-- LEFT JOIN pedidos p
-- 	ON c.cliente_id = p.cliente_id;

-- Encontrando Clientes Sem Compras

-- SELECT *
-- FROM clientes c
-- LEFT JOIN pedidos p
-- 	ON c.cliente_id = p.cliente_id
-- WHERE p.cliente_id IS NULL;

-- JOIN + GROUP BY
-- Muito comum.
-- Total gasto por cliente:

-- SELECT
-- 	c.nome,
-- 	SUM(p.valor) AS total_gasto
-- FROM clientes c
-- INNER JOIN pedidos p
-- 	ON c.cliente_id = p.cliente_id
-- GROUP BY c.nome;


-- JOIN + HAVING
-- Clientes que gastaram mais de 250:

SELECT 
	c.nome,
	SUM(p.valor) AS total
FROM clientes c
JOIN pedidos p
	ON c.cliente_id = p.cliente_id
GROUP BY c.nome
HAVING SUM(p.valor) > 250;

SELECT
    p.nome_produto,
    SUM(i.quantidade) AS total
FROM produtos p
JOIN itens_pedido i
    ON p.produto_id = i.produto_id
GROUP BY p.nome_produto
ORDER BY total DESC;

-- Múltiplos JOINs
SELECT
    c.nome,
    p.pedido_id,
    pr.nome_produto
FROM clientes c

JOIN pedidos p
    ON c.cliente_id = p.cliente_id

JOIN itens_pedido i
    ON p.pedido_id = i.pedido_id

JOIN produtos pr
    ON i.produto_id = pr.produto_id;