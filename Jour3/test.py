import bcrypt

# Hachage du mot de passe
password = b"motdepasse"
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)

# Vérification du mot de passe
if bcrypt.checkpw(password, hashed):
    print("Accès autorisé")
else:
    print("Accès refusé")

