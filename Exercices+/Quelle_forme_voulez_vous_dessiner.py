# On définit les programmes
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

def dessineCarre(l,x,y,couleur):
    dessinePolygone(4,l,x,y,couleur)

def dessineCercle(l,x,y,couleur):
    up()
    goto(x,y)
    down()
    color(couleur)
    circle(l)

def dessineTriangle(l,x,y,couleur):
    dessinePolygone(3,l,x,y,couleur)


# Programme principal

i="oui"

while i=="oui":
    a = input("Que voulez vous dessiner ? (cercle, triangle ou carré) ")
    if a=="cercle" :
        l = float(input("Rayon du cercle ? "))
        x = float(input("Abscisse du point en bas à gauche ?"))
        y = float(input("Ordonnée du point en bas à gauche ?"))
        couleur = input ("Quelle couleur (en anglais) ?")
        print(dessineCercle(l,x,y,couleur))

    if a=="triangle" :
        l = float(input("Longueur des côtés ? "))
        x = float(input("Abscisse du point en bas à gauche ?"))
        y = float(input("Ordonnée du point en bas à gauche ?"))
        couleur = input ("Quelle couleur (en anglais) ?")
        print(dessineTriangle(l,x,y,couleur))

    if a=="carré" :
        l = float(input("Longueur des côtés ? "))
        x = float(input("Abscisse du point en bas à gauche ?"))
        y = float(input("Ordonnée du point en bas à gauche ?"))
        couleur = input ("Quelle couleur (en anglais) ?")
        print(dessineCarre(l,x,y,couleur))
        
    i = input("Voulez vous continuer à dessiner ? ")
    clearscreen()

