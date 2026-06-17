-- Mostrar clientes de São Paulo.
-- SELECT nome FROM clientes WHERE cidade='São Paulo';

--Mostrar clientes com mais de 5 compras.
-- SELECT nome FROM clientes WHERE compras>=5;

-- Mostrar clientes com idade menor que 30.
-- SELECT nome FROM clientes WHERE idade<=30;

-- Ordenar clientes por idade, do mais novo para o mais velho.
-- SELECT nome, idade FROM clientes ORDER BY idade ASC;

-- Mostrar a maior quantidade de compras.
-- SELECT MAX(compras) AS biggest
-- FROM clientes GROUP BY nome;

-- Mostrar a maior quantidade de compras com o nome correspondente
SELECT nome, compras FROM clientes 
WHERE compras = (SELECT MAX(compras) 
FROM clientes);