#On définit la fonction

def renverse (s):

    res=""                   # La chaine résultat est vide
    i=0
    while i<len(s):          # Tant que l'indice i est inférieur au nb de caractères de la chaine s 
        res=s[i]+res         # On l'insère en première position
        i=i+1
    return res               # On retourne la chaine

    

# Programme principal

s = input("Le texte : ")
r = renverse(s)
if renverse(r)!=s:
    print("Aie aie aie, une erreur ...")
else :
    print("A l'envers : ", r)
