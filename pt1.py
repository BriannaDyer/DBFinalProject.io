import mysql.connector

b=mysql.connector.connect(host="localhost", user="root", password="Passtheword123!", database="menagerie")

sql = "INSERT INTO pet (name, owner, species, sex, birth, death) VALUES (%s, %s, %s, %s, %s, %s)"

VALUE = [
    ('Fluffy','Harold','cat','f','1993-02-04'),
    ('Claws','Gwen','cat','m','1994-03-17'),
    ('Buffy','Harold','dog','f','1989-05-13'),
    ('Fluffy','Harold','cat','f','1993-02-04'),
    ('Browser','Diane','dog','m','1979-08-31','1995-07-29'),
    ('Chirpy','Gwen','bird','f','1998-09-11'),
    ('Whistler','Gwen','bird','1997-12-09'),
    ('Slim','Benny','snake','m','1996-04-29'),
    ('Fang','Benny','dog','m','1990-08-27'),
    ('Puffball','Diane','hamster','f','1999-03-30')
    ]

cursor=b.cursor(sql,VALUE)



