prix = [9.99, 14.5, 3.2, 29.0]      # liste des prix
somme = 0

# affichage des prix + calcul de la somme
for i in prix:
    print("prix :", i)
    somme += i

print(somme)                        # somme totale

prixmoyen = somme / len(prix)       # calcul de la moyenne
print(prixmoyen)

# affichage des prix supérieurs à 10
for i in prix:
    if i > 10:
        print(f"Ce chiffre est supérieur à 10: {i}")
