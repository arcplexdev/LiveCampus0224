
var = "Du texte"
secondeVar = [[1,2,3],[1,4,4],[6,4,5]]

class voiture:
    couleur = ""
    marque = ""
    puissance = 1
    vitesse = 0
    def __init__(self, paramCouleur, paramMarque):
        self.couleur = paramCouleur
        self.marque = paramMarque
    def accelerer(self):
        self.vitesse += 10 * self.puissance - 10

mesVoitures = []
mesVoitures.append(voiture("rouge","Ferrari"))
mesVoitures.append(voiture("bleu","Dacia"))
mesVoitures[1].accelerer()
mesVoitures[1].couleur = "rouge"
mesVoitures[1].marque = "dacia"
print(mesVoitures[1].vitesse)