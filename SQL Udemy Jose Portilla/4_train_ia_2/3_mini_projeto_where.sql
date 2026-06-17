-- Criar tabela
CREATE TABLE produtos(
	id INT PRIMARY KEY,
	produto VARCHAR(50),
	categoria VARCHAR(50),
	preco DECIMAL(10,2),
	quantidade INT
);