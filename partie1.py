#Partie 1 :

a = 1
b = "12"
print( int(a) + int(b) )

if a == 1:
    print(" a : 1")
else:
    print("Autre")


c = ["#1","2"]
print(len(c))
c.append("3é")
print(c[2])

d = ["Fruit","Legume"]
tableau = c + d
print(tableau)
# variable1 = float(7)
# print(variable1)
#
# var12 = "Un texte"
# print(type(var12))
# print(var12[4])

#Partie 2 : Print
age = 23
nom = "Jean"
print("%s a %.2f ans"%(nom,age))

count = 0
while count < 10:
    print(count)
    count = count + 1
    if count == 5:
        continue # ou break 2 comportements
else:
    print("Fin de traitement")