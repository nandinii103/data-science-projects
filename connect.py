import sqlite3
connection = sqlite3.connect('connection.db')
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS data(
student_id INTEGER PRIMARY KEY ,
age INTEGER ,
grade TEXT ,
marks INTEGER ,
year REAL ,
name TEXT
) """)

cursor.execute("""
INSERT INTO data(student_id,age,grade,marks,year,name)
VALUES
(1,17,'A',89,11,'vlada') ,
(2,15,'D' ,35,10,'adrianna') ,
(3,19,'B',75,12,'giselle'),
(4,12,'C',52,9,'shalom')
""")
connection.commit()
print("studnetr info")
connection.close()