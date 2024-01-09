USE ratings;
LOAD DATA LOCAL INFILE 'ratings.csv' INTO TABLE ratings
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'  
(@name,@grape,@region,@variety,@rating,@notes) set name=@name,rating=@rating,region=@region;

-- Doesn't work because loading local data disabled. Has to be enabled on both client and server sides