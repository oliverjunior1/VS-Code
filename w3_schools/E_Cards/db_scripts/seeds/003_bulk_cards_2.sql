INSERT INTO tbl_cards (
    hp, name, info, attack, damage, weak, resist, retreat,
    cardNumberInCollection, collection_id, type_id, stage_id
) VALUES
(60, 'Pidgey', 'Tiny Bird Pokémon', 'Gust', '20', 'Electric', 'Fighting', '1 Colorless',
 15, 1, (SELECT id FROM tbl_types WHERE typeName='Colorless'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(80, 'Pidgeotto', 'Bird Pokémon', 'Whirlwind', '30', 'Electric', 'Fighting', '2 Colorless',
 16, 1, (SELECT id FROM tbl_types WHERE typeName='Colorless'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(120, 'Pidgeot', 'Bird Pokémon', 'Hurricane', '60', 'Electric', 'Fighting', '2 Colorless',
 17, 1, (SELECT id FROM tbl_types WHERE typeName='Colorless'), (SELECT id FROM tbl_stages WHERE stageName='Stage 2')),

(50, 'Caterpie', 'Worm Pokémon', 'String Shot', '10', 'Fire', 'Water', '1 Colorless',
 45, 1, (SELECT id FROM tbl_types WHERE typeName='Grass'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(70, 'Metapod', 'Cocoon Pokémon', 'Harden', '0', 'Fire', 'Water', '2 Colorless',
 11, 1, (SELECT id FROM tbl_types WHERE typeName='Grass'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(100, 'Butterfree', 'Butterfly Pokémon', 'Whirlwind', '40', 'Fire', 'Water', '1 Colorless',
 12, 1, (SELECT id FROM tbl_types WHERE typeName='Grass'), (SELECT id FROM tbl_stages WHERE stageName='Stage 2')),

(40, 'Weedle', 'Hairy Bug Pokémon', 'Poison Sting', '10', 'Fire', 'Grass', '1 Colorless',
 13, 1, (SELECT id FROM tbl_types WHERE typeName='Grass'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(80, 'Kakuna', 'Cocoon Pokémon', 'Stiffen', '0', 'Fire', 'Grass', '2 Colorless',
 14, 1, (SELECT id FROM tbl_types WHERE typeName='Grass'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(110, 'Beedrill', 'Poison Bee Pokémon', 'Twineedle', '50', 'Fire', 'Grass', '2 Colorless',
 15, 1, (SELECT id FROM tbl_types WHERE typeName='Grass'), (SELECT id FROM tbl_stages WHERE stageName='Stage 2')),

(60, 'Abra', 'Psi Pokémon', 'Teleport', '0', 'Psychic', 'None', '1 Colorless',
 63, 1, (SELECT id FROM tbl_types WHERE typeName='Psychic'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(80, 'Kadabra', 'Psi Pokémon', 'Confusion', '30', 'Psychic', 'None', '2 Colorless',
 64, 1, (SELECT id FROM tbl_types WHERE typeName='Psychic'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(130, 'Alakazam', 'Psi Pokémon', 'Psychic', '60', 'Psychic', 'None', '3 Colorless',
 65, 1, (SELECT id FROM tbl_types WHERE typeName='Psychic'), (SELECT id FROM tbl_stages WHERE stageName='Stage 2')),

(50, 'Machop', 'Superpower Pokémon', 'Low Kick', '20', 'Psychic', 'None', '1 Colorless',
 66, 1, (SELECT id FROM tbl_types WHERE typeName='Fighting'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(90, 'Machoke', 'Superpower Pokémon', 'Karate Chop', '50', 'Psychic', 'None', '2 Colorless',
 67, 1, (SELECT id FROM tbl_types WHERE typeName='Fighting'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(140, 'Machamp', 'Superpower Pokémon', 'Seismic Toss', '60', 'Psychic', 'None', '3 Colorless',
 68, 1, (SELECT id FROM tbl_types WHERE typeName='Fighting'), (SELECT id FROM tbl_stages WHERE stageName='Stage 2')),

(60, 'Gastly', 'Gas Pokémon', 'Lick', '10', 'Psychic', 'None', '1 Colorless',
 69, 1, (SELECT id FROM tbl_types WHERE typeName='Psychic'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(80, 'Haunter', 'Gas Pokémon', 'Nightmare', '30', 'Psychic', 'None', '2 Colorless',
 70, 1, (SELECT id FROM tbl_types WHERE typeName='Psychic'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(130, 'Gengar', 'Shadow Pokémon', 'Dark Mind', '60', 'Psychic', 'None', '3 Colorless',
 71, 1, (SELECT id FROM tbl_types WHERE typeName='Psychic'), (SELECT id FROM tbl_stages WHERE stageName='Stage 2')),

(50, 'Onix', 'Rock Snake Pokémon', 'Rock Throw', '30', 'Grass', 'None', '3 Colorless',
 72, 1, (SELECT id FROM tbl_types WHERE typeName='Fighting'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(70, 'Drowzee', 'Hypnosis Pokémon', 'Pound', '20', 'Psychic', 'None', '1 Colorless',
 73, 1, (SELECT id FROM tbl_types WHERE typeName='Psychic'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(100, 'Hypno', 'Hypnosis Pokémon', 'Confuse Ray', '30', 'Psychic', 'None', '2 Colorless',
 74, 1, (SELECT id FROM tbl_types WHERE typeName='Psychic'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(60, 'Krabby', 'River Crab Pokémon', 'Vice Grip', '20', 'Electric', 'None', '1 Colorless',
 75, 1, (SELECT id FROM tbl_types WHERE typeName='Water'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(90, 'Kingler', 'Pincer Pokémon', 'Crabhammer', '50', 'Electric', 'None', '2 Colorless',
 76, 1, (SELECT id FROM tbl_types WHERE typeName='Water'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(50, 'Voltorb', 'Ball Pokémon', 'Tackle', '20', 'Fighting', 'None', '1 Colorless',
 77, 1, (SELECT id FROM tbl_types WHERE typeName='Electric'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(80, 'Electrode', 'Ball Pokémon', 'Explosion', '60', 'Fighting', 'None', '2 Colorless',
 78, 1, (SELECT id FROM tbl_types WHERE typeName='Electric'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(60, 'Koffing', 'Poison Gas Pokémon', 'Smog', '20', 'Psychic', 'None', '1 Colorless',
 79, 1, (SELECT id FROM tbl_types WHERE typeName='Psychic'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(90, 'Weezing', 'Poison Gas Pokémon', 'Selfdestruct', '60', 'Psychic', 'None', '2 Colorless',
 80, 1, (SELECT id FROM tbl_types WHERE typeName='Psychic'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(70, 'Rhyhorn', 'Spikes Pokémon', 'Horn Attack', '30', 'Grass', 'None', '2 Colorless',
 81, 1, (SELECT id FROM tbl_types WHERE typeName='Fighting'), (SELECT id FROM tbl_stages WHERE stageName='Basic')),

(120, 'Rhydon', 'Drill Pokémon', 'Horn Drill', '60', 'Grass', 'None', '3 Colorless',
 82, 1, (SELECT id FROM tbl_types WHERE typeName='Fighting'), (SELECT id FROM tbl_stages WHERE stageName='Stage 1')),

(60, 'Chansey', 'Egg Pokémon', 'Double-Edge', '80', 'Fighting', 'None', '1 Colorless',
 83, 1, (SELECT id FROM tbl_types WHERE typeName='Colorless'), (SELECT id FROM tbl_stages WHERE stageName='Basic