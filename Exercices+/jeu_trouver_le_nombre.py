import random
print("Vous devez trouver un nombre entre 0 et 100")
print("Vous avez au plus 7 tentatives")
i = 1
x=random.randint(0,100)
while i<=7 :
    nombre = int(input("Choisissez un nombre : "))
    if nombre>x :
        print("Trop grand")
        i=i+1
    elif nombre<x :
        print("Trop petit")
        i=i+1
    else :
        print("Vous avez gagné en ", i, "tentatives!")
        i=i+10
if i==8 :
    print("Vous avez perdu")
