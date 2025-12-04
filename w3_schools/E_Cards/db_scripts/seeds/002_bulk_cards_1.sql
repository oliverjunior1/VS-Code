INSERT INTO tbl_cards (
    hp, name, info, attack, damage, weak, resist, retreat,
    cardNumberInCollection, collection_id, type_id, stage_id
) VALUES
(60, 'Pikachu', 'Mouse Pokémon', 'Thunder Shock', '30', 'Fighting', 'Metal', '1 Colorless',
 25, 1, (SELECT id FROM tbl_types WHERE typeName='Electric'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(120, 'Charizard', 'Flame Pokémon', 'Fire Spin', '100', 'Water', 'None', '3 Colorless',
 4, 1, (SELECT id FROM tbl_types WHERE typeName='Fire'), (SELECT id FROM tbl_stages WHERE stageName='Stage 2')),

(50, 'Bulbasaur', 'Seed Pokémon', 'Vine Whip', '20', 'Fire', 'Water', '1 Colorless',
 44, 1, (SELECT id FROM tbl_types WHERE typeName='Grass'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(70, 'Squirtle', 'Tiny Turtle Pokémon', 'Bubble', '20', 'Electric', 'None', '1 Colorless',
 7, 1, (SELECT id FROM tbl_types WHERE typeName='Water'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(80, 'Ivysaur', 'Seed Pokémon', 'Razor Leaf', '30', 'Fire', 'Water', '2 Colorless',
 2, 1, (SELECT id FROM tbl_types WHERE typeName='Grass'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(90, 'Wartortle', 'Turtle Pokémon', 'Water Gun', '40', 'Electric', 'None', '2 Colorless',
 8, 1, (SELECT id FROM tbl_types WHERE typeName='Water'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(150, 'Blastoise', 'Shellfish Pokémon', 'Hydro Pump', '60', 'Electric', 'None', '3 Colorless',
 9, 1, (SELECT id FROM tbl_types WHERE typeName='Water'), (SELECT id FROM tbl_stages WHERE stageName='Stage 2')),

(45, 'Charmander', 'Lizard Pokémon', 'Ember', '30', 'Water', 'None', '1 Colorless',
 46, 1, (SELECT id FROM tbl_types WHERE typeName='Fire'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(80, 'Charmeleon', 'Flame Pokémon', 'Flamethrower', '50', 'Water', 'None', '2 Colorless',
 24, 1, (SELECT id FROM tbl_types WHERE typeName='Fire'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(60, 'Jigglypuff', 'Balloon Pokémon', 'Sing', '20', 'Steel', 'Darkness', '1 Colorless',
 39, 2, (SELECT id FROM tbl_types WHERE typeName='Fairy'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(70, 'Meowth', 'Scratch Cat Pokémon', 'Pay Day', '20', 'Fighting', 'Psychic', '1 Colorless',
 56, 2, (SELECT id FROM tbl_types WHERE typeName='Colorless'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(100, 'Snorlax', 'Sleeping Pokémon', 'Body Slam', '50', 'Fighting', 'None', '4 Colorless',
 11, 2, (SELECT id FROM tbl_types WHERE typeName='Colorless'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(60, 'Eevee', 'Evolution Pokémon', 'Quick Attack', '20', 'Fighting', 'None', '1 Colorless',
 55, 2, (SELECT id FROM tbl_types WHERE typeName='Colorless'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(90, 'Vaporeon', 'Bubble Jet Pokémon', 'Water Gun', '40', 'Electric', 'None', '2 Colorless',
 12, 2, (SELECT id FROM tbl_types WHERE typeName='Water'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(90, 'Jolteon', 'Lightning Pokémon', 'Thunderbolt', '60', 'Fighting', 'None', '2 Colorless',
 13, 2, (SELECT id FROM tbl_types WHERE typeName='Electric'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(90, 'Flareon', 'Flame Pokémon', 'Flamethrower', '60', 'Water', 'None', '2 Colorless',
 14, 2, (SELECT id FROM tbl_types WHERE typeName='Fire'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(70, 'Oddish', 'Weed Pokémon', 'Absorb', '20', 'Fire', 'Water', '1 Colorless',
 58, 2, (SELECT id FROM tbl_types WHERE typeName='Grass'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(100, 'Gloom', 'Weed Pokémon', 'Poison Powder', '30', 'Fire', 'Water', '2 Colorless',
 59, 2, (SELECT id FROM tbl_types WHERE typeName='Grass'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(140, 'Vileplume', 'Flower Pokémon', 'Solar Beam', '60', 'Fire', 'Water', '3 Colorless',
 60, 2, (SELECT id FROM tbl_types WHERE typeName='Grass'), (SELECT id FROM tbl_stages WHERE stageName='Stage 2')),

(80, 'Scyther', 'Mantis Pokémon', 'Slash', '40', 'Fire', 'Fighting', '1 Colorless',
 10, 2, (SELECT id FROM tbl_types WHERE typeName='Grass'), (SELECT id FROM tbl_stages WHERE stageName='Basic'));