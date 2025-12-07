# Liste des produits
produits = ["PC Portable", "Écran", "Clavier", "Souris", "Casque"]
# Saisie de l'indice
index = int(input("Indice : "))
# Tentative d'accès à l'élément de la liste
try:
    print("Nom :", produits[index])
except IndexError:
    # Gestion des indices hors limites
    print("Indice invalide. Veuillez entrer un nombre entre 0 et", len(produits)-1)