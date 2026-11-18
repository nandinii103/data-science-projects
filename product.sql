CREATE TABLE products(
products_id INTEGER PRIMARY KEY
name TEXT
brand TEXT
price REAL 
);
INSERT INTO products
VALUES
(1, 'laptop' , 'HP' , 600.00)
(2,'mouse' , 'samsung' , 98.00)
(3,'keyboard' , 'cannon' , 876.00)
(4,'moniter' ,'apple' ,34.00)
(5,'printer' , 'microsoft' , 234.00)

SELECT * FROM products


SELECT 8 FOMR products
WHERE name LIKE '%O%';

SELECT MIN(price) AS highest_price
FROM products

SELECT MAX(price) AS lowest_price
FROM products

UPDATE products
SET price = 600.00
WHERE products_id = 1;

DELETE FROM  products
WHERE products_id = 5;

SELECT * FROM products