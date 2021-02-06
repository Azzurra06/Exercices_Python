#definition de la fonction

def moyenne(l):
    res=""
    for c in l:
        (int(res))=res+c
        moy=int(res/len(l))
    return moy



#programme principal

l=[]
entier = int(input("Entre le premier terme entier de la liste :"))
l.append(entier)
a="oui"
while a=="oui":
    entier = int(input("Entre le terme entier suivant de la liste :"))
    l.append(entier)
    a=input("Voulez vous continuer à ajouter des termes? oui/non :")

print(moyenne(l))
