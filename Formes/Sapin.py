# On définit le programme
from turtle import *
def dessinePolygone(nb,l,x,y,couleur):
    
    up()
    goto(x,y)
    down()
    color(couleur)

    i=1
    while i<=nb :
        forward(l)
        left(360/nb)
        i=i+1



nb = int(4)
l = float(input("Quelle longueur pour les côtés ?"))
x = float(input("Abscisse du point en bas à gauche ?"))
y = float(input("Ordonnée du point en bas à gauche ?"))
couleur = "brown"      
print(dessinePolygone(nb,l,x,y,couleur))



nb = int(3)
x = int(x-(l/2))
y = int(y+l)
l = int(2*l)
couleur = "green"       
print(dessinePolygone(nb,l,x,y,couleur))
