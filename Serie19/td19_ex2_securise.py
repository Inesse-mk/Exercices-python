from pathlib import Path
import json

FICHIER_TODOS = Path("todos.json")

def charger_taches_securise(chemin_fichier: Path) -> list[dict]:
    """Charge la liste de tâches en gérant les fichiers manquants ou JSON corrompu."""
    if not chemin_fichier.exists():
        print(f"Fichier {chemin_fichier} introuvable. Une liste vide sera utilisée.")
        return []
    try:
        with chemin_fichier.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"Erreur : JSON invalide ({e}). Liste vide utilisée.")
        return []

def sauvegarder_taches(chemin_fichier: Path, taches: list[dict]) -> None:
    """Sauvegarde la liste de tâches dans un fichier JSON."""
    with chemin_fichier.open("w", encoding="utf-8") as f:
        json.dump(taches, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    taches = charger_taches_securise(FICHIER_TODOS)
    nb_avant = len(taches)

    # Ajouter une tâche si la liste est vide
    if nb_avant == 0:
        nouvelle_tache = {"id": 1, "titre": "Première tâche", "fait": False}
        taches.append(nouvelle_tache)

    sauvegarder_taches(FICHIER_TODOS, taches)
    nb_apres = len(taches)

    print(f"Tâches avant ajout : {nb_avant}")
    print(f"Tâches après ajout  : {nb_apres}")
