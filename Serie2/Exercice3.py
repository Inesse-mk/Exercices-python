# Exercice 3
commandes = [
    {"id": 1, "client": "alice@example.com",  "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@example.com",    "montant": 15.00, "statut": "annulee"},
    {"id": 3, "client": "alice@example.com",  "montant": 19.90, "statut": "payee"},
    {"id": 4, "client": "charlie@example.com","montant": 120.0, "statut": "en_attente"},
    {"id": 5, "client": "bob@example.com",    "montant": 35.0,  "statut": "payee"},
]
# Calcul du chiffre d'affaires total pour les commandes payées
chiffre_affaires =0
for cmd in commandes:
    if cmd["statut"] == "payee":
        chiffre_affaires+= cmd["montant"]

print("Chiffre d'affaires total :", chiffre_affaires)
# Comptage des commandes selon leur statut
nb_payee = 0
nb_annulee = 0
nb_en_attente = 0

for cmd in commandes:
    if cmd["statut"] == "payee":
        nb_payee += 1
    elif cmd["statut"] == "annulee":
        nb_annulee += 1
    elif cmd["statut"] == "en_attente":
        nb_en_attente += 1

print("Nombre de commandes payées :", nb_payee)
print("Nombre de commandes annulées :", nb_annulee)
print("Nombre de commandes en attente :", nb_en_attente)

# Calcul du total des montants par client

totaux_clients = {}

for cmd in commandes:
    client = cmd["client"]
    montant = cmd["montant"]
    if client not in totaux_clients:
        totaux_clients[client] = 0
    totaux_clients[client] += montant

print(totaux_clients)