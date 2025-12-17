import csv
from pathlib import Path

# Définir les chemins des fichiers
fichier_brut = Path("donnees") / "clients_brut.csv"
fichier_propre = Path("donnees") / "clients_propre.csv"
fichier_erreurs = Path("donnees") / "clients_erreurs.csv"

# Fonction pour vérifier si une ligne est valide
def est_ligne_valide(ligne: dict) -> (bool, str):
    champs = ["nom", "age", "ville"]
    for champ in champs:
        if not ligne.get(champ):
            return False, f"Champ {champ} vide"
    try:
        int(ligne["age"])
    except ValueError:
        return False, "Age non convertible en entier"
    return True, ""

# Listes pour stocker les lignes valides et invalides
lignes_valides = []
lignes_invalides = []

# Lecture du fichier CSV brut
with fichier_brut.open("r", encoding="utf-8", newline="") as f:
    lecteur = csv.DictReader(f, delimiter=';')
    for ligne in lecteur:
        valide, raison = est_ligne_valide(ligne)
        if valide:
            lignes_valides.append(ligne)
        else:
            ligne_err = ligne.copy()
            ligne_err["raison"] = raison
            lignes_invalides.append(ligne_err)

# Écriture des lignes valides
if lignes_valides:
    with fichier_propre.open("w", encoding="utf-8", newline="") as f:
        champs = lignes_valides[0].keys()
        ecrivain = csv.DictWriter(f, fieldnames=champs, delimiter=';')
        ecrivain.writeheader()
        ecrivain.writerows(lignes_valides)

# Écriture des lignes invalides avec la raison
if lignes_invalides:
    with fichier_erreurs.open("w", encoding="utf-8", newline="") as f:
        champs = list(lignes_invalides[0].keys())
        ecrivain = csv.DictWriter(f, fieldnames=champs, delimiter=';')
        ecrivain.writeheader()
        ecrivain.writerows(lignes_invalides)

# Affichage du résumé
print(f"Lignes lues      : {len(lignes_valides) + len(lignes_invalides)}")
print(f"Lignes valides   : {len(lignes_valides)}")
print(f"Lignes invalides : {len(lignes_invalides)}")
print("Résultats :")
print(f"  - {fichier_propre}")
print(f"  - {fichier_erreurs}")


# Commentaires :

# 1. csv.reader (liste de listes) :
#    - Chaque ligne est une liste d’éléments.
#    - Plus rapide pour les fichiers simples ou très volumineux.
#    - Mais on doit se rappeler à quel index correspond chaque colonne, ce qui peut rendre le code moins lisible pour le nettoyage.

# 2. csv.DictReader (dictionnaires) :
#    - Chaque ligne est un dictionnaire avec les noms des colonnes comme clés.
#    - Idéal pour filtrer ou nettoyer les données en utilisant le nom des champs.
#    - Le code est plus lisible et maintenable.

