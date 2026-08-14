SELECT * FROM Artist;

SELECT * FROM Artist WHERE Name = "Nicki Minaj"; --- Dont appear nothing

INSERT INTO Artist (ArtistId, Name) VALUES (276, "Nicki Minaj");

SELECT * FROM Artist WHERE Name = "Nicki Minaj"; --- Appear her name now

SELECT * FROM Artist WHERE Name = 'Cardi B'; --- There's no record

INSERT INTO Artist VALUES ('Cardi B', 277); --- Here give an error

INSERT INTO Artist VALUES (277, 'Cardi B'); --- Now it's work


