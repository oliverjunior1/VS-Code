/*CREATE TABLE vendas (
	id INT PRIMARY KEY,
	nome_vendedor VARCHAR(100),
	vendas_dia DECIMAL(10,2),
	vendas_mes DECIMAL(10,2),
	vendas_ano DECIMAL(12,2)
);


INSERT INTO vendas
(id, nome_vendedor, vendas_dia, vendas_mes, vendas_ano)
VALUES
(1, 'Ana Silva', 350.50, 8200.00, 98500.00),
(2, 'Pedro Souza', 420.00, 9500.00, 114000.00),
(3, 'Carlos Lima', 180.00, 6100.00, 73200.00),
(4, 'Mariana Costa', 500.00, 11000.00, 132000.00),
(5, 'Juliana Santos', 275.00, 7400.00, 88800.00),
(6, 'Felipe Rocha', 620.00, 12800.00, 153600.00),
(7, 'Ricardo Alves', 390.00, 8900.00, 106800.00),
(8, 'Fernanda Oliveira', 455.00, 9800.00, 117600.00),
(9, 'Gabriel Pereira', 315.00, 7700.00, 92400.00),
(10, 'Patricia Gomes', 520.00, 11300.00, 135600.00),
(11, 'Lucas Martins', 280.00, 6800.00, 81600.00),
(12, 'Roberta Castro', 610.00, 12600.00, 151200.00),
(13, 'Bruno Ferreira', 470.00, 10200.00, 122400.00),
(14, 'Aline Mendes', 240.00, 6500.00, 78000.00),
(15, 'Thiago Ramos', 430.00, 9400.00, 112800.00),
(16, 'Camila Barbosa', 550.00, 11800.00, 141600.00),
(17, 'Rafael Nunes', 300.00, 7200.00, 86400.00),
(18, 'Vanessa Melo', 490.00, 10500.00, 126000.00),
(19, 'Eduardo Silva', 370.00, 8500.00, 102000.00),
(20, 'Priscila Lopes', 530.00, 11500.00, 138000.00),
(21, 'Daniel Cardoso', 260.00, 6700.00, 80400.00),
(22, 'Tatiane Ribeiro', 580.00, 12100.00, 145200.00),
(23, 'Marcelo Teixeira', 340.00, 8100.00, 97200.00),
(24, 'Larissa Freitas', 465.00, 9900.00, 118800.00),
(25, 'Joao Almeida', 410.00, 9200.00, 110400.00);


SELECT * FROM vendas;
SELECT nome_vendedor FROM vendas WHERE vendas_mes > 10000;
SELECT nome_vendedor FROM vendas WHERE vendas_ano > 100000;



ALTER TABLE vendas
ADD produto VARCHAR(100);

UPDATE vendas
SET produto = 'Notebook'
WHERE id IN (1,4,10,15,20,25);


UPDATE vendas
SET produto = 'Smartphone'
WHERE id IN (2,8,13,18,24);


UPDATE vendas
SET produto = 'Tablet'
WHERE id IN (6,12,16,22);


SELECT * FROM vendas;

UPDATE vendas
SET produto = 'Monitor'
WHERE produto IS NULL;


SELECT * FROM vendas;
*/

--SELECT produto, SUM(vendas) AS vendas_mensais
--FROM vendas GROUP BY produto
--ORDER BY total DESC
--LIMIT 5;

