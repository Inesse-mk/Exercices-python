
def calculer_ca(commandes):
    """Retourne le total des montants des commandes payées."""
    total = 0
    for commande in commandes:
        if commande["statut"] == "payee":
            total += commande["montant"]
    return total


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

commandes = []

with open("commandes.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.strip()  
        if ligne:  
            champs = ligne.split(";")
            commande = {
                "id": int(champs[0]),
                "client": champs[1],
                "montant": float(champs[2]),
                "statut": champs[3]
            }
            commandes.append(commande)

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
