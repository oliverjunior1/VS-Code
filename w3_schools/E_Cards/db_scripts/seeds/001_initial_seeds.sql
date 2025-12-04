-- Inserir coleções
INSERT INTO tbl_collections (collectionSetName, releaseDate, totalCardsInCollection) VALUES
('Base Set', '1999-01-09', 102),
('Jungle', '1999-06-16', 64),
('Fossil', '1999-10-10', 62);

-- Inserir tipos
INSERT INTO tbl_types (typeName) VALUES
('Fire'), ('Water'), ('Grass'), ('Electric'), ('Psychic'),
('Fighting'), ('Darkness'), ('Metal'), ('Dragon'), ('Fairy'), ('Colorless');

-- Inserir estágios
INSERT INTO tbl_stages (stageName) VALUES
('Basic'), ('Stage 1'), ('Stage 2'), ('Mega'), ('GX'), ('V'), ('VSTAR');

-- Inserir cartas (exemplo: Pikachu, Charizard, Bulbasaur)
INSERT INTO tbl_cards (
    hp, name, info, attack, damage, weak, resist, retreat,
    cardNumberInCollection, collection_id, type_id, stage_id
) VALUES
(60, 'Pikachu', 'Mouse Pokémon', 'Thunder Shock', '30', 'Fighting', 'Metal', '1 Colorless',
 25, 1, (SELECT id FROM tbl_types WHERE typeName='Electric'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(120, 'Charizard', 'Flame Pokémon', 'Fire Spin', '100', 'Water', 'None', '3 Colorless',
 4, 1, (SELECT id FROM tbl_types WHERE typeName='Fire'), (SELECT id FROM tbl_stages WHERE stageName='Stage 2')),

(50, 'Bulbasaur', 'Seed Pokémon', 'Vine Whip', '20', 'Fire', 'Water', '1 Colorless',
 44, 1, (SELECT id FROM tbl_types WHERE typeName='Grass'), (SELECT id FROM tbl_stages WHERE stageName='Basic'));
