def lire_fichier_securise(nom_fichier):
    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            contenu = f.read()
            return contenu
    except FileNotFoundError:
        print("Fichier introuvable.")
        return None

print(lire_fichier_securise("donnees.txt"))
    
livre=input("Entrez le fichier à lire: ")
texte = lire_fichier_securise(livre)

if texte is not None:
    print("\nContenu du fichier :")
    print(texte)
else:
    print("Lecture impossible.")