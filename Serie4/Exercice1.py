
while True:
    try:
        age = int(input("Entrez votre âge: "))
        break
    except ValueError : 
        print("Veuillez entrer un entier (ex: 25).")

print(f"Vous avez {age} ans.")

