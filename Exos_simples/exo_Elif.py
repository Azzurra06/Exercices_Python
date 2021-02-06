prix = int(input("Prix ? "))

if prix > 1000 :
    print("Trop cher")
    print("J'achète pas")
elif 100 < prix < 1000:
    print("J'achète")
    print("Même si c'est pas donné")
else :
    print("J'achète")
    print("C'est donné!")
print("Fin des achats")
