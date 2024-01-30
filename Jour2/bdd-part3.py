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
values = [
    ("THOMPSON","Jim",43,13),
("DURAND","Paul",25,12),
("MORA","Stan",19,13)
    ]
mycursor.executemany(sql,values)
mydb.commit()

mycursor.execute("SELECT * FROM personnes;")
myresult = mycursor.fetchall()
for resultat in myresult:
    print(resultat)

#Premier exercice :
#Je veux un classe Personne qui va avoir un constructeur avec nom, prenom, age, entreprise
#je veux faire un tableau avec 3 ou 4 personnes dedans
#je veux intégrer ces 4 personnes dans la DB

# Part 2 : Je veux intégrer si NOM PRENOM ENTREPRISE n'existe pas DEJA dans la DB