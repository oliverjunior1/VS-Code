INSERT INTO tbl_collections (CollectionSetName, releaseDate, totalCardsInCollection, cardNameInCollection)
VALUES
('Base Set', '1999-01-09', 102, 'Charizard'),
('Jungle', '1999-06-16', 64, 'Snorlax'),
('Fossil', '1999-10-10', 62, 'Aerodactyl');

INSERT INTO tbl_types (typeName)
VALUES
('Fire'),
('Water'),
('Grass'),
('Electric'),
('Psychic'),
('Fighting');

INSERT INTO tbl_stages (stageName)
VALUES
('Basic'),
('Stage 1'),
('Stage 2');

INSERT INTO tbl_cards (hp, name, info, attack, damage, weak, collection_id, type_id, stage_id)
VALUES
(120, 'Charizard', 'Flame Pokémon, evolves from Charmeleon', 'Fire Spin', '100', 'Water', 1, 1, 3),
(90, 'Blastoise', 'Shellfish Pokémon, evolves from Wartortle', 'Hydro Pump', '60', 'Electric', 1, 2, 3),
(60, 'Pikachu', 'Mouse Pokémon, mascot of the franchise', 'Thunder Jolt', '30', 'Fighting', 1, 4, 1),
(70, 'Snorlax', 'Sleeping Pokémon, known for blocking paths', 'Body Slam', '30', 'Fighting', 2, 6, 1),
(80, 'Aerodactyl', 'Fossil Pokémon revived from Old Amber', 'Wing Attack', '30', 'Electric', 3, 6, 1);