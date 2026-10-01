SELECT nome FROM clientes c ;

SELECT nome, cidade, salario FROM clientes;

SELECT * FROM clientes;

SELECT nome, cidade FROM clientes;

SELECT * FROM clientes WHERE cidade = 'Goiânia';

SELECT * FROM clientes c WHERE salario > 5000;

SELECT nome, idade FROM clientes WHERE idade>30;

SELECT * FROM clientes c WHERE cidade = 'Goiânia' AND salario > 5000;

SELECT * FROM clientes c WHERE cidade = 'Goiânia' or c.cidade = 'Anápolis';

SELECT  * FROM clientes c WHERE cidade IN ('Goiânia', 'Anápolis');

SELECT * FROM clientes c WHERE c.cidade NOT IN ('Goiânia', 'Anápolis');

SELECT nome, salario FROM clientes c ORDER BY salario;

SELECT nome, salario FROM clientes ORDER BY salario DESC;

SELECT nome, salario FROM clientes c ORDER BY salario DESC LIMIT 3;

SELECT COUNT(*) FROM clientes;

SELECT COUNT(*) as local_clientes FROM clientes;

SELECT SUM(salario) AS folha_total FROM clientes c;

SELECT AVG(salario) AS salario_medio FROM clientes;

SELECT MIN(salario) as menor_salario FROM clientes;