CREATE TABLE students(
student_id INTEGER PRIMARY KEY
Name TEXT
age INTEGER
grade text
);


INSERT INTO students
(student_id , Name , age, grade)
VALUES
(1,'alice' ,13 , 'A')
(2,'bob' ,14 , 'B')
(3,'john' ,18 , 'A')

SELECT * FROM students;


SELECT * FROM students
WHERE age = 14;
