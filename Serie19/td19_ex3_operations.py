"""
TD19 - Exercice 3 : opérations métier sur une todo list en JSON
- Ajouter une tâche
- Marquer une tâche faite
- Supprimer une tâche
- Afficher la liste
- Sauvegarder dans todos.json

Structure JSON attendue :
{
  "utilisateur": "alice",
  "derniere_id": 3,
  "taches": [
    {"id": 1, "titre": "Apprendre Python", "fait": true},
    {"id": 2, "titre": "Lire la fiche JSON", "fait": false},
    {"id": 3, "titre": "Terminer le TD 19", "fait": false}
  ]
}
"""

from pathlib import Path
import json
from typing import Any

###############################################################
# Chargement sécurisé (repris de l'exercice 2)
###############################################################
def charger_donnees(chemin: Path) -> dict[str, Any]:
    if not chemin.exists():
        print("Fichier introuvable → création d'une structure par défaut.")
        return {
            "utilisateur": "alice",
            "derniere_id": 0,
            "taches": []
        }
    try:
        with chemin.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("JSON corrompu → utilisation d'une structure vide.")
        return {
            "utilisateur": "alice",
            "derniere_id": 0,
            "taches": []
        }

###############################################################
# Sauvegarde
###############################################################
def sauvegarder_donnees(chemin: Path, donnees: dict[str, Any]) -> None:
    with chemin.open("w", encoding="utf-8") as f:
        json.dump(donnees, f, ensure_ascii=False, indent=2)

###############################################################
# Opérations métier
###############################################################
def ajouter_tache(donnees: dict[str, Any], titre: str) -> None:
    """
    Ajoute une tâche et incrémente donnees["derniere_id"].
    """
    donnees["derniere_id"] += 1
    nouvelle = {
        "id": donnees["derniere_id"],
        "titre": titre,
        "fait": False
    }
    donnees["taches"].append(nouvelle)


def marquer_tache_faite(donnees: dict[str, Any], id_tache: int) -> bool:
    """
    Marque la tâche comme faite. Renvoie True si trouvée.
    """
    for t in donnees["taches"]:
        if t["id"] == id_tache:
            t["fait"] = True
            return True
    return False


def supprimer_tache(donnees: dict[str, Any], id_tache: int) -> bool:
    """
    Supprime une tâche. Renvoie True si suppression effectuée.
    """
    for t in donnees["taches"]:
        if t["id"] == id_tache:
            donnees["taches"].remove(t)
            return True
    return False

###############################################################
# Affichage
###############################################################
def afficher_taches(donnees: dict[str, Any]) -> None:
    print(f"Tâches de {donnees['utilisateur']} :")
    for t in donnees["taches"]:
        print(f"[{t['id']}] {t['titre']} (fait={t['fait']})")
    print()

###############################################################
# Programme principal
###############################################################
if __name__ == "__main__":
    FICHIER = Path("todos.json")

    # Chargement des données
    donnees = charger_donnees(FICHIER)

    print("=== LISTE INITIALE ===")
    afficher_taches(donnees)

    # Ajout d'une nouvelle tâche
    ajouter_tache(donnees, "Nouvelle tâche ajoutée automatiquement")

    # Marquer une tâche existante
    marquer_tache_faite(donnees, 1)

    # Suppression d'une tâche
    supprimer_tache(donnees, 2)

    print("=== APRÈS MODIFICATIONS ===")
    afficher_taches(donnees)

    # Sauvegarde
    sauvegarder_donnees(FICHIER, donnees)
    print("Données sauvegardées dans todos.json.")
