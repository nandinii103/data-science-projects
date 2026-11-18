Drop TABLE IF EXISTS Restaurant;
CREATE TABLE Restaurant (
name TEXT,
neighborhood TEXT,
cuisine TEXT,
review REAL,
price TEXT,
health TEXT

);

-- Insert data

INSERT INTO Restaurant (name, neighborhood, cuisine, review, price, health)
VALUES

('Peter', 'Brooklyn', 'Steak', 4.4, '$$$$', 'A'),
('Jongro', 'Midtown', 'Korean', 3.5, '$$', 'A'),
('Pocha', 'Midtown', 'Pizza', 4.0, '$$$', 'B'),
('Lighthouse', 'Queens', 'Chinese', 3.9, '$', 'A'),
('Minca', 'Downtown', 'American', 4.6, '$$$', ''),
('Marea', 'Chinatown', 'Chinese', 3.0, '$$', ''),
('Dirty Candy', 'Uptown', 'Italian', 4.9, '$$$$', 'B'),
('Di Fara Pizza', 'Brooklyn', 'Pizza', 3.8, '$$', 'A'),
('Golden Unicorn', 'Uptown', 'Italian', 3.8, '$$', 'A');


SELECT DISTINCT neighborhood
FROM Restaurant;

SELECT DISTINCT cuisine
FROM Restaurant;

SELECT * FROM Restaurant
WHERE cuisine = 'chinese';

SELECT * FROM Restaurant
WHERE review >= 4.0;

SELECT * FROM Restaurant
WHERE cuisine = 'Italian' AND price IN ('$$' , '$$$');

SELECT * FROM Restaurant
WHERE price = '$$$' ;

SELECT * FROM Restaurant
WHERE name LIKE '%Candy%';

SELECT * FROM Restaurant
WHERE neighborhood IN ('Midtown','Chinatown' , 'Downtown');

SELECT * FROM Restaurant
WHERE health IS NULL OR '';

SELECT * FROM Restaurant
ORDER BY review DESC 
LIMIT 4;





