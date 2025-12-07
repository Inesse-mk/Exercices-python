# Fonction pour lire un fichier en gérant les erreurs
def lire_fichier_securise(nom_fichier):
    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            contenu = f.read()
            return contenu
    except FileNotFoundError:
        print("Fichier introuvable.")
        return None

# Exemple d'utilisation avec un fichier prédéfini
print(lire_fichier_securise("donnees.txt"))
# Saisie du nom du fichier à lire   
livre=input("Entrez le fichier à lire: ")
texte = lire_fichier_securise(livre)
# Affichage du contenu si lecture réussie
if texte is not None:
    print("\nContenu du fichier :")
    print(texte)
else:
    print("Lecture impossible.")