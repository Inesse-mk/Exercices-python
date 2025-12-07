commandes = [
    {"id": 1, "client": "alice@example.com",  "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@example.com",    "montant": 15.00, "statut": "annulee"},
    {"id": 3, "client": "alice@example.com",  "montant": 19.90, "statut": "payee"},
    {"id": 4, "client": "charlie@example.com","montant": 120.0, "statut": "en_attente"},
    {"id": 5, "client": "bob@example.com",    "montant": 35.0,  "statut": "payee"},
]
# Calcul du chiffre d'affaires total des commandes payées
def calculer_ca(commandes):
    """Retourne le total des montants des commandes payées."""
    total = 0
    for commande in commandes:
        if commande["statut"] == "payee":
            total += commande["montant"]
    return total

# Comptage des commandes par statut
def compter_commandes_par_statut(commandes):
    """Retourne un dictionnaire {statut: nombre}."""
    stats = {}
    for commande in commandes:
        statut = commande["statut"]
        if statut in stats:
            stats[statut] += 1
        else:
            stats[statut] = 1
    return stats

# Calcul du total dépensé par client
def totaux_par_client(commandes):
    """Retourne un dictionnaire {client: total dépensé}."""
    totaux = {}
    for commande in commandes:
        client = commande["client"]
        montant = commande["montant"]
        if client in totaux:
            totaux[client] += montant
        else:
            totaux[client] = montant
    return totaux


# Partie exécutable
if __name__ == "__main__":
    ca = calculer_ca(commandes)
    stats = compter_commandes_par_statut(commandes)
    totaux = totaux_par_client(commandes)

    print("=== Résultats ===")
    print(f"Chiffre d'affaires total (commandes payées) : {ca} €")

    print("\nNombre de commandes par statut :")
    for s, n in stats.items():
        print(f" - {s} : {n}")

    print("\nTotal dépensé par client :")
    for client, total in totaux.items():
        print(f" - {client} : {total} €")
