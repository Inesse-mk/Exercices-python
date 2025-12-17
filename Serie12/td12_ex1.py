# td12_ex1.py
import logging

# Configuration minimale du logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def traiter_commande(commande):
    logger.debug("Commande reçue : %s", commande)

    if not commande:
        logger.error("Commande vide")
        return

    logger.info("Vérification du stock...")
    if commande.get("quantite", 0) <= 0:
        logger.error("Quantité invalide")
        return

    logger.info("Commande validée pour le client %s", commande.get("client"))
    # ... autres traitements ...

if __name__ == "__main__":
    # Commande valide
    traiter_commande({"id": 1, "client": "Alice", "quantite": 3})

    # Commande vide
    traiter_commande({})

    # Commande avec quantité invalide
    traiter_commande({"id": 2, "client": "Bob", "quantite": 0})
