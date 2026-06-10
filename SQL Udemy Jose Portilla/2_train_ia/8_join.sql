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


