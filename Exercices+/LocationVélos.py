print ("Location de vélos !")

nbHeuresSouhaitées = int(input("Combien d'heures souhaitez-vous louer ? "))

if nbHeuresSouhaitées > 8 :
    print ("Rappel : Le nombre d'heures maximum de location des vélos est de 8h ")
    
    nbHeuresSouhaitées2 = int(input("Combien d'heures souhaitez-vous louer ? "))
    abonnement = (input("Avez-vous un abonnement ? "))
    
    if nbHeuresSouhaitées <= 2 :
        coût = 3 * nbHeuresSouhaitées2
        if abonnement=="non" :
            coût = coût + 2
        print ("Le montant prévisionnel pour ",nbHeuresSouhaitées2, "heures de location est de ", coût, "euros")
        
    else :
        coût2 = 5 * (nbHeuresSouhaitées2 - 2) + 6
        if abonnement=="non" :
            coût2 = coût2 + 2
        print ("Le montant prévisionnel pour ",nbHeuresSouhaitées2, "heures de location est de ", coût2, "euros")

    
else :
    abonnement = (input("Avez-vous un abonnement ? "))
    if nbHeuresSouhaitées <= 2 :
        coût = 3 * nbHeuresSouhaitées
        if abonnement=="non" :
            coût = coût + 2
        print ("Le montant prévisionnel pour ",nbHeuresSouhaitées, "heures de location est de ", coût, "euros")
        
    else :
        coût2 = 5 * (nbHeuresSouhaitées-2) + 6
        if abonnement=="non" :
            coût2 = coût2 + 2
        print ("Le montant prévisionnel pour ",nbHeuresSouhaitées, "heures de location est de ", coût2, "euros")
            

            
    


    
