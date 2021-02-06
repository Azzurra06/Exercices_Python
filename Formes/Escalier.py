from turtle import *

hauteur = window_height()
largeur = window_width()

a = int(input("Combien de marches voulez vous ? "))
b = int(input("Quelle est la hauteur des marches ? "))
z = int(input("Quelle est la longueur des marches ? "))

up()
goto((-largeur/2)+20,(hauteur/2)-20)
down()

write("Départ")
i=0
t=0
while i<=a :
    forward (z)
    right(90)
    forward(b)
    left(90)
    x,y = pos()
    if (((x+z)>(largeur/2)) and ((y+b)<(-hauteur/2))) :
        up()
        goto(0,0)
        write("Tronqué")
        i=1000000
        t=1
    i=i+1

if t!=1 :
    write("Arrivée")
