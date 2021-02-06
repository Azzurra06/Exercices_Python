#definition de la fonction pour calculer la surface de la pièce à peindre
def surfaceMur(a,b,c) :
    return (a*b)*2 + (c*b)*2

#détérminer les données
hauteur = float(input("Quelle est la hauteur de la pièce ?"))
largeur = float(input("Quelle est la largeur de la pièce ? "))
longueur = float(input("Quelle est la longueur de la pièce ?"))

#début du programme
print(surfaceMur(largeur,hauteur,longueur))
