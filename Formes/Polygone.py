# On définit le programme
from turtle import *
def dessinePolygone(nb,l,x=0,y=0,couleur="blue"):
    
    up()
    goto(x,y)
    down()
    color(couleur)

    i=1
    while i<=nb :
        forward(l)
        left(360/nb)
        i=i+1


#Programme principal
        
nb = float(input("Combien de côtés ?"))
l = float(input("Quelle longueur pour les côtés ?"))      
print(dessinePolygone(nb,l))
