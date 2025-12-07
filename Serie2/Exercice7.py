import json
from Exercice4 import calculer_ca, compter_commandes_par_statut,totaux_par_client

# Liste des commandes
commandes = [
    {"id": 1, "client": "alice@example.com",  "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@example.com",    "montant": 15.00, "statut": "annulee"},
    {"id": 3, "client": "alice@example.com",  "montant": 19.90, "statut": "payee"},
    {"id": 4, "client": "charlie@example.com","montant": 120.0, "statut": "en_attente"},
    {"id": 5, "client": "bob@example.com",    "montant": 35.0,  "statut": "payee"},
]

# Conversion de la liste en chaîne JSON pour affichage
dump_json = json.dumps(commandes, indent = 2)
print(dump_json)

# Écriture de la liste des commandes dans un fichier JSON
with open("commandes.json","w", encoding="utf-8") as f:
    json.dump(commandes, f, indent=2, ensure_ascii=False)

# Lecture du fichier JSON pour récupérer les commandes
with open ("commandes.json","r", encoding="utf-8") as f:
    commandes_lues = json.load(f)

# Utilisation des fonctions importées pour analyser les commandes
print("Chiffre d'affaires :", calculer_ca(commandes_lues))
print("Commandes par statut :", compter_commandes_par_statut(commandes_lues))
print("Total par client :", totaux_par_client(commandes_lues))



