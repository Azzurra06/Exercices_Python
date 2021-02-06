#On définit la fonction palindrome

def palindrome(s) :
    res=""                      # la chaine resultat est vide
    for lettre in s :           # pour chaque caractère de la chaine
        res=lettre+res          # on l'insère en première position
    if res==s :                 # si la chaine inversée est identique à la chaine de départ
        reponse=True            # il s'agira d'un palindrome
    else :                      # sinon non
        reponse=False

    return reponse              # on retourne la réponse



#programme principal

s = input("Un mot (fin pour finir) : ")

cpt_palindromes=0
cpt_mot=0

while s != "fin" :             # tant que le mot est différent du mot "fin"
    
    s = input("Un mot (fin pour finir) : ")
    
    if palindrome(s)==True :
        cpt_palindromes = cpt_palindromes+1
    else :
        cpt_palindromes = cpt_palindromes
        
    cpt_mot=cpt_mot+1
    
print("Vous avez entré" , cpt_mot , "mots, dont" , cpt_palindromes , "palindromes")
