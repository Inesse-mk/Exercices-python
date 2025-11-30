# Exercice 5
class CommandeInvalideError(Exception):
    pass

def valider_commande(montant):
    if montant <= 0:
        raise ValueError("Montant nul ou négatif.")
    if montant > 10000:
        raise CommandeInvalideError("Solde insuffisant.")
    return True

try :
    montant= float(input("Entrez votre montant: "))
    valider_commande(montant)
except CommandeInvalideError as e:
    print("Erreur métier :", e)
except ValueError as e:
    print("Erreur de saisie :", e)
else:
    print("Commande valide")