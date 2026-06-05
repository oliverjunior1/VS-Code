/*CREATE TABLE funcionarios (
    departamento VARCHAR(50),
    salario DECIMAL(10,2)
);*/
/*
INSERT INTO funcionarios (departamento, salario)
VALUES
('TI', 5000),
('TI', 7000),
('RH', 4000),
('RH', 6000),
('Financeiro', 8000);*/

--1. Média salarial por departamento.
--SELECT departamento, AVG(salario) FROM funcionarios GROUP BY departamento;

--2. Total salarial por departamento.
--SELECT departamento,SUM(salario) FROM funcionarios GROUP BY departamento;

--3. Departamentos com média acima de 5500.
/*SELECT departamento,
       AVG(salario) AS media_salarial
FROM funcionarios
GROUP BY departamento
HAVING AVG(salario) > 5500;*/


/*CREATE TABLE clientes_vendas (
    cliente VARCHAR(50),
    valor DECIMAL(10,2)
);*/

/*INSERT INTO clientes_vendas (cliente, valor)
VALUES
('Ana', 100),
('Ana', 200),
('Ana', 150),
('Pedro', 300),
('Pedro', 100),
('Julia', 500);*/

--1. Total gasto por cliente.
SELECT cliente, SUM(valor) FROM clientes_vendas GROUP BY cliente;

--2. Quantidade de pedidos.
--3. Ticket médio.
--4. Clientes que gastaram mais de 300.
