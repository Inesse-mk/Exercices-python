# Définition d'une exception spécifique pour les commandes invalides
class CommandeInvalideError(Exception):
    pass
# Fonction pour valider le montant d'une commande
def valider_commande(montant):
    if montant <= 0:
        raise ValueError("Montant nul ou négatif.")
    if montant > 10000:
        raise CommandeInvalideError("Solde insuffisant.")
    return True
# Saisie et validation de la commande
try :
    montant= float(input("Entrez votre montant: "))
    valider_commande(montant)
except CommandeInvalideError as e:
    print("Erreur métier :", e)
except ValueError as e:
    print("Erreur de saisie :", e)
else:
    print("Commande valide")