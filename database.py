import mysql.connector

mydb = mysql.connector.connect(user='GMA', password='password',host='localhost',database='student')

mycursor = mydb.cursor()

mycursor.execute("select * from profile")

result = mycursor.fetchall()

for i in result:
    print(i)



