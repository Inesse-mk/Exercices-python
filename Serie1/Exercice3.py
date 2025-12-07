age = int (input("Entrez votre age: "))     # saisie et conversion en nombre
# vérification des tranches d'âge
if age < 12:
    print ("Tarif : 5.0€")
elif age >= 12 and age <= 17:
    print ("Tarif : 7.0€")
elif age >= 18 and age <= 25:
    print("Tarif : 8.5€")
else:
    print("Tarif : 10.0€")