INSERT INTO tbl_cards (
    hp, name, info, attack, damage, weak, resist, retreat,
    cardNumberInCollection, collection_id, type_id, stage_id
) VALUES
(60, 'Magikarp', 'Fish Pokémon', 'Splash', '0', 'Electric', 'None', '1 Colorless',
 90, 1, (SELECT id FROM tbl_types WHERE typeName='Water'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(120, 'Gyarados', 'Atrocious Pokémon', 'Dragon Rage', '50', 'Electric', 'None', '3 Colorless',
 91, 1, (SELECT id FROM tbl_types WHERE typeName='Water'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(70, 'Poliwag', 'Tadpole Pokémon', 'Bubble', '20', 'Electric', 'None', '1 Colorless',
 92, 1, (SELECT id FROM tbl_types WHERE typeName='Water'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(90, 'Poliwhirl', 'Tadpole Pokémon', 'Water Gun', '30', 'Electric', 'None', '2 Colorless',
 93, 1, (SELECT id FROM tbl_types WHERE typeName='Water'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(130, 'Poliwrath', 'Tadpole Pokémon', 'Submission', '60', 'Electric', 'None', '3 Colorless',
 94, 1, (SELECT id FROM tbl_types WHERE typeName='Water'), (SELECT id FROM tbl_stages WHERE stageName='Stage 2')),

(60, 'Tentacool', 'Jellyfish Pokémon', 'Poison Sting', '20', 'Psychic', 'None', '1 Colorless',
 95, 1, (SELECT id FROM tbl_types WHERE typeName='Water'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(100, 'Tentacruel', 'Jellyfish Pokémon', 'Wrap', '30', 'Psychic', 'None', '2 Colorless',
 96, 1, (SELECT id FROM tbl_types WHERE typeName='Water'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(50, 'Diglett', 'Mole Pokémon', 'Dig', '20', 'Grass', 'None', '1 Colorless',
 97, 1, (SELECT id FROM tbl_types WHERE typeName='Fighting'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(80, 'Dugtrio', 'Mole Pokémon', 'Earthquake', '60', 'Grass', 'None', '2 Colorless',
 98, 1, (SELECT id FROM tbl_types WHERE typeName='Fighting'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(60, 'Geodude', 'Rock Pokémon', 'Tackle', '20', 'Grass', 'None', '1 Colorless',
 99, 1, (SELECT id FROM tbl_types WHERE typeName='Fighting'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(90, 'Graveler', 'Rock Pokémon', 'Rock Throw', '30', 'Grass', 'None', '2 Colorless',
 100, 1, (SELECT id FROM tbl_types WHERE typeName='Fighting'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(130, 'Golem', 'Megaton Pokémon', 'Explosion', '60', 'Grass', 'None', '3 Colorless',
 101, 1, (SELECT id FROM tbl_types WHERE typeName='Fighting'), (SELECT id FROM tbl_stages WHERE stageName='Stage 2')),

(60, 'Magnemite', 'Magnet Pokémon', 'Thunder Shock', '20', 'Fighting', 'None', '1 Colorless',
 102, 1, (SELECT id FROM tbl_types WHERE typeName='Electric'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(80, 'Magneton', 'Magnet Pokémon', 'Selfdestruct', '60', 'Fighting', 'None', '2 Colorless',
 103, 1, (SELECT id FROM tbl_types WHERE typeName='Electric'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(50, 'Doduo', 'Twin Bird Pokémon', 'Peck', '20', 'Electric', 'Fighting', '1 Colorless',
 104, 1, (SELECT id FROM tbl_types WHERE typeName='Colorless'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(90, 'Dodrio', 'Triple Bird Pokémon', 'Rage', '30', 'Electric', 'Fighting', '2 Colorless',
 105, 1, (SELECT id FROM tbl_types WHERE typeName='Colorless'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(60, 'Seel', 'Sea Lion Pokémon', 'Headbutt', '20', 'Electric', 'None', '1 Colorless',
 106, 1, (SELECT id FROM tbl_types WHERE typeName='Water'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(100, 'Dewgong', 'Sea Lion Pokémon', 'Aurora Beam', '50', 'Electric', 'None', '2 Colorless',
 107, 1, (SELECT id FROM tbl_types WHERE typeName='Water'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(60, 'Grimer', 'Sludge Pokémon', 'Pound', '20', 'Psychic', 'None', '1 Colorless',
 108, 1, (SELECT id FROM tbl_types WHERE typeName='Psychic'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(90, 'Muk', 'Sludge Pokémon', 'Sludge', '30', 'Psychic', 'None', '2 Colorless',
 109, 1, (SELECT id FROM tbl_types WHERE typeName='Psychic'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(60, 'Shellder', 'Bivalve Pokémon', 'Clamp', '20', 'Electric', 'None', '1 Colorless',
 110, 1, (SELECT id FROM tbl_types WHERE typeName='Water'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(100, 'Cloyster', 'Bivalve Pokémon', 'Spike Cannon', '40', 'Electric', 'None', '2 Colorless',
 111, 1, (SELECT id FROM tbl_types WHERE typeName='Water'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(50, 'Gastly', 'Gas Pokémon', 'Lick', '10', 'Psychic', 'None', '1 Colorless',
 112, 1, (SELECT id FROM tbl_types WHERE typeName='Psychic'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(80, 'Haunter', 'Gas Pokémon', 'Nightmare', '30', 'Psychic', 'None', '2 Colorless',
 113, 1, (SELECT id FROM tbl_types WHERE typeName='Psychic'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(130, 'Gengar', 'Shadow Pokémon', 'Dark Mind', '60', 'Psychic', 'None', '3 Colorless',
 114, 1, (SELECT id FROM tbl_types WHERE typeName='Psychic'), (SELECT id FROM tbl_stages WHERE stageName='Stage 2')),

(60, 'Horsea', 'Dragon Pokémon', 'Smokescreen', '20', 'Electric', 'None', '1 Colorless',
 115, 1, (SELECT id FROM tbl_types WHERE typeName='Water'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(90, 'Seadra', 'Dragon Pokémon', 'Water Gun', '40', 'Electric', 'None', '2 Colorless',
 116, 1, (SELECT id FROM tbl_types WHERE typeName='Water'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(130, 'Kingdra', 'Dragon Pokémon', 'Dragon Breath', '60', 'Electric', 'None', '3 Colorless',
 117, 1, (SELECT id FROM tbl_types WHERE typeName='Dragon'), (SELECT id FROM tbl_stages WHERE stageName='Stage 2')),

(70, 'Staryu', 'Star Shape Pokémon', 'Slap', '20', 'Electric', 'None', '1 Colorless',
 118, 1, (SELECT id FROM tbl_types WHERE typeName='Water'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(100, 'Starmie', 'Mysterious Pokémon', 'Recover', '30', 'Electric', 'None', '2 Colorless',
 119, 1, (SELECT id FROM tbl_types WHERE typeName='Water'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1'));