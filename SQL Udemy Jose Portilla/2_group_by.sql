SELECT vendedor,
       SUM(valor) AS total_vendas
FROM vendas
GROUP BY vendedor;



