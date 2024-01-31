import bcrypt

mot_de_passe = "motdepasse123".encode("utf-8")
salt = bcrypt.gensalt()
mot_de_passe_chiffre = bcrypt.hashpw(mot_de_passe, salt)
print(str(mot_de_passe_chiffre))


monTexte = "Vincent"
mon_byte = b"Vincent"
