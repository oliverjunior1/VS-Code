-- Seleciona o Pokémon com maior HP
SELECT 
    c.id,
    c.name AS pokemon_name,
    c.hp,
    t.typeName AS tipo,
    s.stageName AS estagio,
    col.CollectionSetName AS colecao
FROM tbl_cards c
JOIN tbl_types t ON c.type_id = t.id
JOIN tbl_stages s ON c.stage_id = s.id
JOIN tbl_collections col ON c.collection_id = col.id
ORDER BY c.hp DESC
LIMIT 1;
