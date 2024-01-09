USE ratings;
(SELECT 'name', 'rating', 'region' FROM ratings)
UNION
SELECT * FROM ratings
INTO OUTFILE '../table.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
