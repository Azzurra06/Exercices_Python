#Ce code permet de compter le nombre de fois qu'une lettre apparait dans le mot

#on définit la fonction
def fonction(t, l) :
    i=0
    cpt=0
    while i< len(t) :
        if l == t[i] :
            cpt=cpt+1
        else:
            cpt=cpt + 0
        i=i+1
    return cpt

#programme principal
t = input("Un mot ? ")
l = input("Une lettre ?")
print (fonction(t, l))

        
