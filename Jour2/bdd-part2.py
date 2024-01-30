import mysql.connector
# Table personnes
# +------------+--------------+------+-----+---------+----------------+
# | Field      | Type         | Null | Key | Default | Extra          |
# +------------+--------------+------+-----+---------+----------------+
# | id         | int(11)      | NO   | PRI | NULL    | auto_increment |
# | nom        | varchar(255) | NO   |     | NULL    |                |
# | prenom     | varchar(255) | NO   |     | NULL    |                |
# | age        | int(11)      | YES  |     | NULL    |                |
# | entreprise | int(11)      | YES  |     | NULL    |                |
# +------------+--------------+------+-----+---------+----------------+

mydb = mysql.connector.connect(
    host="localhost",
    user="livecampus",
    password="demoPwd",
    database="LIVECAMPUS"
)
mycursor = mydb.cursor()

sql = "INSERT INTO personnes (nom, prenom, age, entreprise) VALUES (%s, %s, %s, %s)"
values = ("THOMPSON","Jim",43,13)
mycursor.execute(sql,values)
mydb.commit()

mycursor.execute("SELECT * FROM personnes;")
myresult = mycursor.fetchall()
for resultat in myresult:
    print(resultat)

