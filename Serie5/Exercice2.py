
import os
# --- LBYL (Look Before You Leap) : on vérifie si le fichier existe avant de l'ouvrir ---
def lire_fichier_lbyl(nom_fichier):
    if os.path.exists(nom_fichier): # vérification de l'existence du fichier
        with open(nom_fichier, "r", encoding="utf-8") as f:
            contenu = f.read()
        return contenu
    else:
        print("Fichier introuvable :", nom_fichier)
        return None

print(lire_fichier_lbyl("donnees.txt"))
print(lire_fichier_lbyl("fichier.txt"))
# --- EAFP (Easier to Ask for Forgiveness than Permission) : on tente l'ouverture et on gère l'exception ---
def lire_fichier_eafp(nom_fichier):
    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            contenu = f.read()
        return contenu
    except FileNotFoundError: # gestion si le fichier n'existe pas
        print("Fichier introuvable :", nom_fichier)
        return None
    
print(lire_fichier_eafp("donnees.txt"))
print(lire_fichier_eafp("fichier.txt"))
