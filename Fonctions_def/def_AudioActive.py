def audioActive(terme):
    suivant=""
    terme=str(terme)
    c_actuel=terme[0]
    compteur_audio = 0
    for c in terme:
        if c == c_actuel :
            compteur_audio = compteur_audio+1
            print(compteur_audio)
            print(c)
        else :
            compteur_audio = 0
            print(1)
            print(c)


terme = int(input("Combien de termes (>=2) ?"))
i=2
while i<=terme :
    print("terme", i, ": ", audioActive(terme))
    i=i+1
            
        
