#Premier exercice :

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
#Je veux un classe Personne qui va avoir un constructeur avec nom, prenom, age, entreprise

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="livecampus",
    password="demoPwd",
    database="LIVECAMPUS"
)
mycursor = mydb.cursor()

class Person:
    nom = ""
    prenom = ""
    age = 0
    entreprise = 0
    def __init__(self, nom, prenom, age, entreprise):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.entreprise = entreprise

    def getTuple(self):
        return (self.nom, self.prenom, self.age, self.entreprise)

    def checkExisting(self):
        return (self.nom, self.prenom, self.entreprise)

#je veux faire un tableau avec 3 ou 4 personnes dedans
personnes = []
personnes.append(Person("NOM1", "PRENOM1", "18", 13))
personnes.append(Person("NOM2", "PRENOM2", "19", 1))
personnes.append(Person("NOM3", "PRENOM3", "20", 10))
personnes.append(Person("NOM4", "PRENOM4", "21", 12))
personnes.append(Person("NOM5", "PRENOM5", "22", 12))

mycursor.execute("SELECT * FROM personnes;")
myresult = mycursor.fetchall()
for resultat in myresult:
    print(resultat)

#J'ai un tableau (myresult) qui contient la DB existante et un tableau personnes qui contient ce que je veux entrer

values = []
for personne in personnes:
    #Si personne.getTuple() n'est PAS dans result:
    #values.append(personne.getTuple())

#je veux intégrer ces 4 personnes dans la DB

sql = "INSERT INTO personnes (nom, prenom, age, entreprise) VALUES (%s, %s, %s, %s)"
mycursor.executemany(sql,values)
mydb.commit()


# Part 2 : Je veux intégrer si NOM PRENOM ENTREPRISE n'existe pas DEJA dans la DB

