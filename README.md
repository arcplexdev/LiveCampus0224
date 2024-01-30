# LiveCampus0224
Formation du 29-01 au 02-02

Lundi PM : 

Rappels de Python
Administration de MySQL
TP Administration de MySQL et import de données

Importer la DB : 
mysql < mysqlsampledatabase.sql 

Créer un utilisateur : 
CREATE USER 'demoUser'@'localhost' IDENTIFIED BY 'demoPwd';

Assigner des droits sur la DB : 
GRANT ALL ON NomDB.* TO 'demoUser'@'localhost'

# Exemple de jointure SQL 

Exemple de jointure : 

SELECT personnes.nom AS Nom, #-> Le champ nom de la table personnes renommé Nom
personnes.prenom AS Prenom, #-> Le champ prenom de la table personnes renommé Prénom
entreprise.nom AS Entreprise #-> Le champ nom de la table entreprise renommé Entreprise
FROM personnes LEFT JOIN entreprise #-> Jointure (ici de type LEFT)
ON entreprise.id = personnes.entreprise;  #-> Critere de jointure


