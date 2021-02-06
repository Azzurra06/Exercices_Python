#définition fonction affine
def affine (a,b,x) :
    return a*x+b
#fin de la fonction

#lecture des données
T = int(input("Quelle est la température que vous voulez convertir ? "))
U = input("Vous voulez convertir en quelle unité de degré? Celsius ou Fahrenheit ?")

#début du programme

#si l'utilisateur demande à convertir des degrés Fahrenheit en Celsius
if U=="Celsius" or "celsius" or "C" or "c" :
    print(T," °F équivaut à ", affine(T-32,0,1/1.8), "°C")

#si l'utilisateur demande à convertir des degrés Celsius en Fahrenheit
elif U=="Fahrenheit" or "fahrenheit" or "F" or "f":
    print(T," °C équivaut à ",affine(T,1.8,32) , "°F")
#fin du programme

    
    
