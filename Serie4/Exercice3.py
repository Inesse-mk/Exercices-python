produits = ["PC Portable", "Écran", "Clavier", "Souris", "Casque"]
index = int(input("Indice : "))
try:
    print("Nom :", produits[index])
except IndexError:
    print("Indice invalide. Veuillez entrer un nombre entre 0 et", len(produits)-1)