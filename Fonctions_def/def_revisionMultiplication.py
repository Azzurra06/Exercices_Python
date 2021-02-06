#on définit la fonction
def reviserTable(t,r):

    print("Révision de la table de ", t," jusqu'à ",r)
    i = 1
    while i<=r :
        print(i,"fois ",t," :",i*t)
        i=i+1


    

#programme principal

print("Révision des tables de multiplication")

i="oui"
while i=="oui":
    t = int(input("Quelle table voulez-vous réviser?"))
    r = int(input("Jusqu'à quelle rang?"))
    print(reviserTable(t,r))
    i=input("Encore ? (oui/non)")
    
print("Fin des revisions")
