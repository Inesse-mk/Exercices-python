# Exercice 5
prix = [9.99, 14.5, 3.2, 29.0]
somme =0
for i in prix:
    print("prix :", i)
    somme  +=i
    if i > 10:
        print (f"Ce chiffre est supérieur à 10: {i}")
print (somme)
  
prixmoyen= somme/len(prix)
print(prixmoyen)


