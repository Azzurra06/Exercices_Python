#on définit la fonction
def fonction(p, l) :
    i=0
    cpt=0
    while i< len(p) :
        if l == p[i] :
            cpt=cpt+1
        else:
            cpt=cpt + 0
        i=i+1
    return cpt

        

#programme principal

#on définit les variables
l = input("Une lettre ?")
p = input("Une phrase ? ")



print(l, " apparaît", fonction(p, l), " fois dans ",p)
rep = input("Encore ? o/n ")
total = fonction(p, l)

#tant que on répond oui, le programme s'execute
while rep=="o" :
    p = input("Une phrase ? ")
    print(l, " apparaît", fonction(p, l), " fois dans ",p)
    #on va additionner le compteur de la lettre chosie
    total = total + fonction(p, l)
    rep = input("Encore ? o/n ")

#quand on ne veut plus donner de phrase on affiche le total des fois où la lettre choisie à été écrite     
print(l, " apparaît", total, " fois au total")
    
       
