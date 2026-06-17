-- Criar tabela
-- CREATE TABLE produtos(
-- 	id INT PRIMARY KEY,
-- 	produto VARCHAR(50),
-- 	categoria VARCHAR(50),
-- 	preco DECIMAL(10,2),
-- 	quantidade INT
-- );

-- INSERT INTO produtos (id, produto, categoria, preco, quantidade) VALUES
-- (1, 'Mouse', 'Informática', 50.00,2),
-- (2, 'Teclado', 'Informática', 120.00,1),
-- (3, 'Caderno', 'Papelaria', 25.00,4),
-- (4, 'Caneta', 'Papelaria', 5.00,10),
-- (5, 'Monitor', 'Informática', 900.00,1);

-- Todos os produtos da categoria Informática.
SELECT produto FROM produtos 
WHERE categoria = 'Informática';