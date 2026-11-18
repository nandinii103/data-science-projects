CREATE TABLE activity(
activity_id INTEGER PRIMARY KEY
name TEXT
type TEXT
fee REAL 
);

INSERT INTO activity
(activity_id , name,type,fee)
VALUES
(1,'yoga' ,'fitness' , 10.00)
(2,'drawing' , 'art' , 27.90)
(3,'dance' , 'fitness' , 12.00)
(4,'guitar' , 'music' , 41.90)

SELECT * FROM activity;

SELECT * FROM activity;
ORDER BY fee DESC;

SELECT name,type,fee FROM activity;

SELECT type
COUNT(*) AS total_activites
FROM activity
GROUP BY type;

SELECT type,
SUM(fee) AS total_fee
FROM activity
GROUP BY type;

SELECT type,
AVG(fee) AS average_fee
FROM activity
FROUP BY type;




