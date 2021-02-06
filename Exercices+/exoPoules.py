poules = 5
nbDoeufsProduits = 14
nbDeJours = 4
x = input ("Combien d'oeufs voulez-vous produire ?")
print ("type de x", type(x))
y = input ("En combien de jours ? ")
print ("type de y", type(y))
x = int(x)
y = int(y)
moyenneOeufsPondus = nbDoeufsProduits/(poules * nbDeJours)
print ("En moyenne, une poule pond", moyenneOeufsPondus, "oeufs par jours")
nbPoulesNecessaires = int((x // y) // moyenneOeufsPondus)
print ("Il vous faut", nbPoulesNecessaires , "poules pour avoir", x ,"oeufs en", y, "jours")


#Je n'ai pas réussi à trouver une fonction qui marche me permettant d'arrondir le résultat à l'entier supérieur
#J'avais trouvé cela sur internet mais ça n'as pas fonctionné:
from math import *
arrondiSup = ceil(nbPoulesNecessaires)
print (arrondiSup)
