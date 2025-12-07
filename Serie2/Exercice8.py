import json
from Exercice4 import calculer_ca, compter_commandes_par_statut,totaux_par_client

# Lecture des commandes depuis le fichier JSON
with open("commandes.json","r",encoding="utf-8") as f:
    commandes_lues = json.load(f)
# Tri des commandes par montant décroissant
commandes_tries = sorted(commandes_lues, key=lambda cmd: cmd["montant"], reverse=True)

print("""=== Tableau de bord commandes ===""")
# Chiffre d'affaires pour les commandes payées
print("Chiffre d'affaires (commandes payées) :", calculer_ca(commandes_lues))
# Nombre de commandes par statut
print("Nombre de commandes par statut :")
for statut, nb in compter_commandes_par_statut(commandes_lues).items():
    print(f"  - {statut:<10}: {nb}")
# Top clients selon le total dépensé
print("Top clients :")
for client, total in sorted(totaux_par_client(commandes_lues).items(), key=lambda x: x[1], reverse=True):
    print(f"  - {client:<20}: {total:.2f} €")
# Affichage du total dépensé par client
print("Total par client :", totaux_par_client(commandes_lues))
# Affichage d'un tableau des commandes triées
print(f"{'Client':<20} {'Montant':<8}")
print("-" * 30)
for cmd in commandes_tries:
    print(f"{cmd['client']:<20} {cmd['montant']:<8}")