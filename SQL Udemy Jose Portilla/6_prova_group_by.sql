-- CREATE TABLE vendas_computer_store (
--     nome_vendedor VARCHAR(50),
--     produto VARCHAR(50),
--     valor_produto DECIMAL(10,2),
--     quantidade INT,
--     total DECIMAL(10,2)
-- );

-- INSERT INTO vendas_computer_store
-- (nome_vendedor, produto, valor_produto, quantidade, total)
-- VALUES
-- ('Ana', 'Mouse', 50, 2, 100),
-- ('Pedro', 'Teclado', 120, 1, 120),
-- ('Carlos', 'Monitor', 900, 1, 900),
-- ('Julia', 'Notebook', 3500, 1, 3500),
-- ('Mariana', 'Mouse', 50, 5, 250),
-- ('Lucas', 'Headset', 180, 2, 360),
-- ('Fernanda', 'Monitor', 850, 1, 850),
-- ('Ricardo', 'Webcam', 200, 3, 600),
-- ('Patricia', 'Teclado', 120, 4, 480),
-- ('Roberta', 'Mouse', 50, 8, 400);

-- INSERT INTO vendas_computer_store
-- (nome_vendedor, produto, valor_produto, quantidade, total)
-- VALUES
-- ('Ana', 'Mouse', 50, 3, 150),
-- ('Pedro', 'Monitor', 900, 1, 900),
-- ('Carlos', 'Notebook', 3500, 1, 3500),
-- ('Julia', 'Webcam', 200, 2, 400),
-- ('Mariana', 'Headset', 180, 4, 720),
-- ('Lucas', 'Teclado', 120, 3, 360),
-- ('Fernanda', 'Mouse', 50, 6, 300),
-- ('Ricardo', 'Notebook', 3500, 1, 3500),
-- ('Patricia', 'Monitor', 900, 2, 1800),
-- ('Roberta', 'Headset', 180, 5, 900);

-- Total vendido por vendedor
SELECT nome_vendedor, SUM(total) AS vendas_total_vendedor 
FROM vendas_computer_store GROUP BY nome_vendedor 
ORDER BY vendas_total_vendedor DESC;

-- Produto mais vendido
SELECT produto, SUM(valor_produto) AS produtos_mais_vendidos 
FROM vendas_computer_store GROUP BY produto 
ORDER BY produtos_mais_vendidos DESC;

-- Ticket médio por vendedor
SELECT nome_vendedor, AVG(total) AS media_vendas 
FROM vendas_computer_store GROUP BY nome_vendedor 
ORDER BY media_vendas DESC;
