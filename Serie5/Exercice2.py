
import os

def lire_fichier_lbyl(nom_fichier):
    if os.path.exists(nom_fichier):
        with open(nom_fichier, "r", encoding="utf-8") as f:
            contenu = f.read()
        return contenu
    else:
        print("Fichier introuvable :", nom_fichier)
        return None

print(lire_fichier_lbyl("donnees.txt"))
print(lire_fichier_lbyl("fichier.txt"))

def lire_fichier_eafp(nom_fichier):
    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            contenu = f.read()
        return contenu
    except FileNotFoundError:
        print("Fichier introuvable :", nom_fichier)
        return None
    
print(lire_fichier_eafp("donnees.txt"))
print(lire_fichier_eafp("fichier.txt"))
