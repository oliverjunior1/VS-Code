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