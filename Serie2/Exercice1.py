mdp=input("Entrez votre mot de passe: ")
valide = True
if len(mdp) < 8:
    print("il doit contenir au moins 8 caractères")
    valide = False
if not any(i.islower() for i in mdp):
    print("il doit contenir au moins une lettre minuscule")
    valide = False
if not any(i.isupper() for i in mdp):
    print("il doit contenir au moins une lettre majiscule")
    valide = False
if not any(i.isdigit() for i in mdp):
    print("il doit contenir au moins un chiffre.")
    valide = False
if valide:
    print ("Mot de passe valide")