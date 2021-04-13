import random

def generateur_lettre(lettre,alphabet):
    i = 0
    while i < 26:
        lettre = random.choice(alphabet)
        print(lettre)
        alphabet = alphabet.replace(lettre, "")
        i = i + 1




print("Generateur de lettre aléatoire")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettre = random.choice(alphabet)
print(generateur_lettre(lettre,alphabet))






