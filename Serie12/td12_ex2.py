# td12_ex2.py
import logging

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    filename="commande.log",  # écrit dans le fichier commande.log
    filemode="a",             # mode ajout
)
logger = logging.getLogger(__name__)

def traiter_commande(commande):
    logger.debug("commande reçue : %s", commande)
    if not commande:
        logger.error("commande vide")
        return

    logger.info("vérification du stock...")
    if commande.get("quantite", 0) <= 0:
        logger.error("quantité invalide")
        return

    logger.info("commande validée pour le client %s", commande.get("client"))
    # ... autres traitements ...

if __name__ == "__main__":
    # Commande valide
    traiter_commande({"id": 1, "client": "Alice", "quantite": 3})

    # Commandes invalides pour générer des ERROR
    traiter_commande({})
    traiter_commande({"id": 2, "client": "Bob", "quantite": 0})

    print("Logs écrits dans le fichier commande.log")
