def chiffrer(message, decalage):
    resultat = ""
    for lettre in message:
        if lettre.isalpha():
            base = ord('A') if lettre.isupper() else ord('a')
            nouvelle_lettre = chr((ord(lettre) - base + decalage) % 26 + base)
            resultat += nouvelle_lettre
        else:
            resultat += lettre
    return resultat

def dechiffrer(message, decalage):
    return chiffrer(message, -decalage)

print("=== Chiffrement César ===")
print("1. Chiffrer")
print("2. Déchiffrer")

choix = input("Votre choix (1 ou 2) : ")
message = input("Entrez votre message : ")
decalage = int(input("Entrez la valeur de décalage : "))

if choix == "1":
    print("Message chiffré :", chiffrer(message, decalage))
elif choix == "2":
    print("Message déchiffré :", dechiffrer(message, decalage))
else:
    print("Choix invalide.")

        