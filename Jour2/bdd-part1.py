import mysql.connector
#CREATE USER 'livecampus'@'localhost' IDENTIFIED BY 'demoPwd';

mydb = mysql.connector.connect(
    host="localhost",
    user="livecampus",
    password="demoPwd",
    database="classicmodels"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM employees;")
myresult = mycursor.fetchall()

for resultat in myresult:
    print(resultat)