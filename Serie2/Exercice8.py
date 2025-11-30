import json
from Exercice4 import calculer_ca, compter_commandes_par_statut,totaux_par_client

with open("commandes.json","r",encoding="utf-8") as f:
    commandes_lues = json.load(f)
 
commandes_tries = sorted(commandes_lues, key=lambda cmd: cmd["montant"], reverse=True)

print("""=== Tableau de bord commandes ===""")

print("Chiffre d'affaires (commandes payées) :", calculer_ca(commandes_lues))
print("Nombre de commandes par statut :")
for statut, nb in compter_commandes_par_statut(commandes_lues).items():
    print(f"  - {statut:<10}: {nb}")

print("Top clients :")
for client, total in sorted(totaux_par_client(commandes_lues).items(), key=lambda x: x[1], reverse=True):
    print(f"  - {client:<20}: {total:.2f} €")

print("Total par client :", totaux_par_client(commandes_lues))

print(f"{'Client':<20} {'Montant':<8}")
print("-" * 30)
for cmd in commandes_tries:
    print(f"{cmd['client']:<20} {cmd['montant']:<8}")