-- CREATE TABLE clientes_novo(
-- 	clientes_id INT PRIMARY KEY,
-- 	nome VARCHAR(100)
-- );

-- INSERT INTO clientes_novo (clientes_id, nome)
-- VALUES
-- 	(1, 'Ana'),
-- 	(2, 'Pedro'),
-- 	(3, 'Julia');

-- SELECT * FROM clientes_novo;

-- CREATE TABLE pedidos(
-- pedido_id INT PRIMARY KEY,
-- cliente_id INT,
-- valor INT
-- );

-- INSERT INTO pedidos (pedido_id, cliente_id, valor)
-- VALUES
-- (101,1,100),
-- (102,1,200),
-- (103,2,300);

-- SELECT * FROM pedidos;

SELECT
    c.nome,
    p.valor
FROM clientes_novo c
INNER JOIN pedidos p
    ON c.cliente_id = p.cliente_id;
