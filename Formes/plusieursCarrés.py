from turtle import *

x = int(input("Combien de carrés voulez vous ? "))
y = int(input("Quelle longueur pour leurs côtés ? "))

up()
goto(-350,-300)
down()

i=1
while i<=x :
    k=1
    while k<=4 :
        forward(y)
        left(90)
        k=k+1
        
    up()
    forward(y)
    left(90)
    forward(y)
    right(90)
    down()
    
    i=i+1
