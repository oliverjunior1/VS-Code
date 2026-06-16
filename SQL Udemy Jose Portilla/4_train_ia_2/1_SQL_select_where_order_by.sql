-- Criar tabela
-- CREATE TABLE clientes (
-- 	id INT,
-- 	nome VARCHAR(50),
-- 	idade INT,
-- 	cidade VARCHAR(50),
-- 	compras INT
-- );

-- Inserir dados
-- INSERT INTO clientes (id, nome, idade, cidade, compras) VALUES
-- (1,'Ana', 22, 'São Paulo',3),
-- (2,'Bruno', 35, 'Rio de Janeiro',8),
-- (3,'Carla', 29, 'São Paulo',5),
-- (4,'Diego', 41, 'Recife',2),
-- (5,'Eva', 30, 'Curitiba',10);

-- Seleciona todas as colunas da tabela clientes
-- SELECT *
-- FROM clientes;

-- Seleciona apenas nome e cidade
-- SELECT nome, cidade FROM clientes;

-- Filtra clientes com idade maior ou igual a 30
-- SELECT * FROM clientes WHERE idade >= 30;

-- Mostra clientes ordenados por número de compras, do maior para o menor
-- SELECT * FROM clientes ORDER BY compras ASC;

-- Conta quantos clientes existem
-- SELECT COUNT(nome) FROM clientes;

-- Calcula a média da compras
-- SELECT AVG(compras) AS media_compras FROM clientes;

-- Agrupa clientes por cidade
SELECT cidade, COUNT(*) AS total
FROM clientes
GROUP BY cidade;



