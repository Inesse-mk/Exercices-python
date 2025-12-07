# Fonction pour effectuer une division sécurisée
def division_securisee():
    try:
        x = int(input("Numérateur : "))
        y = int(input("Dénominateur : "))
        resultat = x / y
    except ValueError:
        print("Veuillez entrer des entiers uniquement.")
        return None
    except ZeroDivisionError:
        print("Le dénominateur ne peut pas être zéro.")
        return None
    else:
        return resultat  # retourne le résultat si pas d'erreur

# Boucle principale
while True:
    resultat = division_securisee()  # appel de la fonction
    if resultat is not None:
        print(f"Le résultat de la division est : {resultat}")
        break  # sortie de la boucle après une division réussie
