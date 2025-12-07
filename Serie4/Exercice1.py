# Boucle jusqu'à ce que l'utilisateur saisisse un entier valide
while True:
    try:
        age = int(input("Entrez votre âge: "))  # conversion en entier
        break       # sortie de la boucle si saisie correcte
    except ValueError : 
        print("Veuillez entrer un entier (ex: 25).")  # message d'erreur si non-entier

print(f"Vous avez {age} ans.")

