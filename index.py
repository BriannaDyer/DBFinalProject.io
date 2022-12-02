import mysql.connector

b = mysql.connector.connect(host="localhost", user= "root", password = "Passtheword123!", database="menagerie")

cursor=b.cursor()

cursor.execute("SELECT name, birth, MONTH(birth) FROM pet")

myresult=cursor.fetchall()

for pet in myresult:
    print(pet)
