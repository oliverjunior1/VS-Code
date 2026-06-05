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
SELECT departamento,
       AVG(salario) AS media_salarial
FROM funcionarios
GROUP BY departamento
HAVING AVG(salario) > 5500;
