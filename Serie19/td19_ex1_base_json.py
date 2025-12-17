import json

def charger_taches(chemin_fichier: str) -> list[dict]:
    """Charge la liste de tâches depuis un fichier JSON."""
    with open(chemin_fichier, 'r', encoding='utf-8') as f:
        taches = json.load(f)
    return taches


def sauvegarder_taches(chemin_fichier: str, taches: list[dict]) -> None:
    """Sauvegarde la liste de tâches dans un fichier JSON."""
    with open(chemin_fichier, 'w', encoding='utf-8') as f:
        json.dump(taches, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    chemin = "todos.json"

    # Charger les tâches existantes
    taches = charger_taches(chemin)

    # Affichage des tâches
    print("Tâches existantes :")
    for tache in taches:
        print(f"[{tache['id']}] {tache['titre']} (fait={tache['fait']})")

    # Ajouter une nouvelle tâche
    nouvelle_tache = {"id": len(taches) + 1, "titre": "Écrire un script JSON", "fait": False}
    taches.append(nouvelle_tache)

    # Sauvegarder les tâches mises à jour
    sauvegarder_taches(chemin, taches)

    print(f"\nNouvelle tâche ajoutée et sauvegardée dans {chemin}.")