# Saisie du mot de passe
mdp = input("Entrez votre mot de passe: ")

valide = True  # On suppose que le mot de passe est valide au départ

# Vérification des critères principaux
if len(mdp) < 8:
    print("Il doit contenir au moins 8 caractères")
    valide = False

if not any(i.islower() for i in mdp):
    print("Il doit contenir au moins une lettre minuscule")
    valide = False

if not any(i.isupper() for i in mdp):
    print("Il doit contenir au moins une lettre majuscule")
    valide = False

if not any(i.isdigit() for i in mdp):
    print("Il doit contenir au moins un chiffre.")
    valide = False

# Affichage final si toutes les conditions sont remplies
if valide:
    print("Mot de passe valide")
