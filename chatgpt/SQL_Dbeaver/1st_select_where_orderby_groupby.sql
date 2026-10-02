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

SELECT MAX(salario) AS maior_salario FROM clientes c;

SELECT COUNT(*) AS quantidade, SUM(salario) AS total, AVG(salario) AS media, MIN(salario) AS menor, MAX(salario) as maior from clientes c;

SELECT cidade, COUNT(*) as quantidade FROM clientes c GROUP BY cidade;

SELECT cidade, AVG(salario) AS salario_medio FROM clientes c GROUP BY cidade;

SELECT cidade, AVG(salario) AS salario_medio FROM clientes GROUP BY cidade HAVING AVG(salario) > 5000;

SELECT nome AS cliente, salario AS renda FROM clientes;

SELECT * FROM clientes c WHERE nome LIKE 'A%';

SELECT cidade, COUNT(*) as quantidade_clientes, AVG(salario) AS salario_medio FROM clientes c GROUP BY cidade HAVING AVG(salario) > 4000 ORDER BY salario_medio DESC;

SELECT * FROM produtos p;

SELECT nome, preco FROM produtos p;

SELECT * FROM produtos p WHERE preco > 500;

SELECT * FROM produtos p ORDER BY preco DESC;

-- Mostre a média dos salários
SELECT AVG(preco) FROM produtos p;
-- ou
SELECT AVG(preco) AS media_de_precos FROM produtos p; 

