# CREATE TABLE users(
#     -> id INT AUTO_INCREMENT PRIMARY KEY,
#     -> login VARCHAR(255) NOT NULL UNIQUE,
#     -> password VARCHAR(255) NOT NULL,
#     -> salt VARCHAR(255) NOT NULL
#     -> );

import mysql.connector
import bcrypt
import env
#Conf BDD
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="livecampus",
    password=env.conf["dbPassword"],
    database="LIVECAMPUS"
)

#Je défini mon salf
def make_salt():
    salt = bcrypt.gensalt()
    return salt

#Fonction pour generer le salt
salt = make_salt()

def hash_password(password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

# Champ de test
username = "Tim"
password = "password4321"

#je hash mon mot de passe
hashed = hash_password(password)

# je rentre mes données en DB
cursor = mydb.cursor()
cursor.execute("INSERT INTO users (login, password, salt) VALUES (%s, %s, %s)", (username, hashed, salt))
mydb.commit()
cursor.close()
mydb.close()