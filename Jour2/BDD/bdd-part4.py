#Requete 1
sql = "SELECT employees.employeeNumber, employees.firstName, employees.lastName, offices.city FROM employees LEFT JOIN offices ON employees.officeCode=offices.officecode;"
#requete 2
sql = "SELECT customers.customerName, customers.customerNumber, orders.orderNumber, orders.orderDate FROM customers INNER JOIN orders ON customers.customerNumber=orders.customernumber;"

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="livecampus",
    password="demoPwd",
    database="classicmodels"
)
mycursor = mydb.cursor()
mycursor.execute(sql)
myresult = mycursor.fetchall()

for resultat in myresult:
    print(resultat[3])