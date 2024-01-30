monDico = {"Cle":"Valeur","AutreCle":"AutreValeur"}

print(monDico['Cle'])

monDico['Cle'] = "Je définie une valeur"
monDico.pop('Cle')
for cle,valeur in monDico.items():
    print("La clé est : %s et la valeur associée est : %s"%(cle,valeur))