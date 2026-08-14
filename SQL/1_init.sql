/*SELECT * 
FROM clientes;

CREATE TABLE clientes (
	id INTEGER,
	nome TEXT,
	idade INTEGER
);

INSERT INTO clientes VALUES (1, Ana, 25);
INSERT INTO clientes VALUES (2, Pedro, 30);
INSERT INTO clientes VALUES (3, Julia, 22);

SELECT * FROM clientes;
*/

-- SELECT * FROM Clientes;

-- SELECT nome FROM clientes;

-- SELECT nome, idade FROM clientes;

--SELECT * FROM clientes WHERE idade > 25;

/*
INSERT INTO clientes VALUES (4,'Ana',25);
INSERT INTO clientes VALUES (5,'Pedro',30);
INSERT INTO clientes VALUES (6,'Julia',22);
*/

-- 1. Mostrar apenas idade.
SELECT idade FROM clientes;

-- 2. Mostrar clientes com idade menor que 30:
SELECT idade, clientes FROM clientes WHERE idade > 30;

-- 3. Motrar apenas nome e idade:
SELECT nome, idade FROM clientes;

