CREATE TABLE marine(
marine_id INTEGER PRIMARY KEY,
name INTEGER
group TEXT
weight REAL 
);
INSERT INTO marine
(marine_id , name, group , weight)
VALUES
(1,'blue whale' ,'mammal' , 1500)
(2,'dolphin' ,'mammal' , 904)
(3,'shark' , 'fish' , 89)
(4,'tuna' ,'fish' , 56)

SELECT * FROM marine;

SELECT DISTINCT
group
FROM marine;

SELECT COUNT(*) AS total_weight
FROM weight;

SELECT COUNT(*) AS total_group
FROM group
WHERE weight = 56;

SELECT SUM(weight) AS total_weight
FROM marine;

SELECT AVG(weight) AS avg_weight
FROM marine;




