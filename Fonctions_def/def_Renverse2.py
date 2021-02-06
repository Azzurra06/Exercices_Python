#On définit la fonction

def renverse2 (s):

    res=""                   # La chaine résultat est vide
    for lettre in s:          # Pour chaque lettre de la chaine
        res=lettre+res         # On l'insère en première position
    return res               # On retourne la chaine

    

# Programme principal

s = input("Le texte : ")
r = renverse2(s)
if renverse2(r)!=s:
    print("Aie aie aie, une erreur ...")
else :
    print("A l'envers : ", r)
