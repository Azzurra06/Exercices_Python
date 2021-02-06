#definition de la fonction pour calculer la surface de la pièce à peindre
def surfaceMur(a,b,c) :
    return (a*b)*2 + (c*b)*2

print("Déco and Co")
#détérminer les données
hauteur = float(input("Quelle est la hauteur des pièces ?"))
nb_pièces = float(input("Combien de pièces ? "))

#début du programme
total=0
i=1
while i<=nb_pièces :
    #déterminer les données pour chaque pièce
    nom = input("Quelle est le nom de la pièce ?")
    longueur = float(input("Quelle est la longueur de la pièce ? (en m)"))
    largeur = float(input("Quelle est la largeur de la pièce ? (en m)"))
    #calculer la surface à peindre dans la pièce
    print(surfaceMur(longueur, hauteur, largeur), "m2 à peindre dans", nom)
    total=total+surfaceMur(longueur, hauteur, largeur)
    i=i+1
print("Vous allez peindre au total", total," m2 dans votre appartement")
