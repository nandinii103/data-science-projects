DROP TABLE IF EXISTS Customer;
CREATE TABLE Customer(
customer_id INTEGER PRIMARY KEY,
cust_name TEXT,
city TEXT,
grade INTEGER
);
INSERT INTO Customer(customer_id,cust_name,city,grade)
VALUES

(3002,"nick rimando","new york",100),
(3007,"brad davis","new york",200),
(3005,"graham zusi","california",200),
(3008,"julian green","london",300),
(3004,"fabian johnson","paris",300),
(3009,"geoff cameron","berlin",100),
(3003,"jozy altidor","moscow",200),
(3001,"brad guzan","london",NULL);

-- SELECT * FROM Customer;
SELECT cust_name , city
FROM Customer;

SELECT cust_name AS "customers_name" , city as "customers_city"
FROM Customer;

SELECT * FROM Customer
WHERE city = "london";

SELECT * FROM Customer
WHERE grade = 200;

SELECT * FROM Customer
WHERE city = "london" AND grade = 300;

SELECT * FROM Customer
WHERE city = "london" OR city = "paris";

SELECT * FROM Customer
WHERE cust_name LIKE "b%" ;

SELECT * FROM Customer
WHERE cust_name LIKE "%john%";


SELECT 
MIN(grade) AS "minimum grade",
MAX(grade) AS max "maximum grade" ,
FROM Customer;



