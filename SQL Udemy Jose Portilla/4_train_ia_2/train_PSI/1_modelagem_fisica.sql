-- Criar a tabela
-- CREATE TABLE cliente(
-- 	id_cliente INT PRIMARY KEY,
-- 	nome VARCHAR(100),
-- 	email VARCHAR(100)
-- );

-- CREATE TABLE pedido (
--     id_pedido INT PRIMARY KEY,
--     id_cliente INT,
--     FOREIGN KEY (id_cliente)
--     REFERENCES cliente(id_cliente)
-- );

CREATE TABLE cliente (
    id_cliente INT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100)
);