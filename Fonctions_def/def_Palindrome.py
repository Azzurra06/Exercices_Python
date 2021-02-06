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



s = input("Un mot : ")
while palindrome(s) == True :   # tant que la réponse est vraie
    print(palindrome(s))  
    s = input("Un mot : ")
    
      
   
