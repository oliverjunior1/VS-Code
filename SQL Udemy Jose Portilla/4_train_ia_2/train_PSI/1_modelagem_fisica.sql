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

-- CREATE TABLE cliente (
--     id_cliente INT PRIMARY KEY,
--     nome VARCHAR(100),
--     email VARCHAR(100)
-- );

-- CREATE TABLE produto (
--     id_produto INT PRIMARY KEY,
--     nome VARCHAR(100),
--     preco DECIMAL(10,2)
-- );

-- CREATE TABLE pedido (
--     id_pedido INT PRIMARY KEY,
--     data_pedido DATE,
--     id_cliente INT,
--     FOREIGN KEY(id_cliente)
--     REFERENCES cliente(id_cliente)
-- );

-- CREATE TABLE item_pedido (
--     id_pedido INT,
--     id_produto INT,
--     quantidade INT,

--     PRIMARY KEY(id_pedido, id_produto),

--     FOREIGN KEY(id_pedido)
--     REFERENCES pedido(id_pedido),

--     FOREIGN KEY(id_produto)
--     REFERENCES produto(id_produto)
-- );

-- Inserir dados no dataset
-- INSERT INTO cliente
-- VALUES (1,'Ana', 'ana@email.com');

