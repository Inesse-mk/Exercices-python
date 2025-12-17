"""
Outil de maintenance de fichiers (logs, CSV, JSON) pour la série 18.
- Nettoyage des logs (~ suppression des lignes DEBUG)
- Nettoyage des clients CSV (séparation OK / erreurs)
- Mise à jour d'un fichier de configuration JSON
"""

import csv
import json
from pathlib import Path
import shutil

# ------------------ Logs ------------------
def nettoyer_logs(chemin_log: Path):
    if not chemin_log.exists():
        print(f"Fichier {chemin_log} introuvable, merci de vérifier le chemin.")
        return

    nom_sans_ext = chemin_log.stem
    chemin_sortie = chemin_log.parent / f"{nom_sans_ext}_sans_debug.log"

    total = 0
    conserves = 0
    with chemin_log.open("r", encoding="utf-8") as fin, chemin_sortie.open("w", encoding="utf-8") as fout:
        for ligne in fin:
            total += 1
            if "[DEBUG]" in ligne:
                continue
            fout.write(ligne)
            conserves += 1

    print(f"Logs traités : {total} lignes, {conserves} lignes conservées")
    print(f"Fichier nettoyé créé : {chemin_sortie}")

# ------------------ CSV ------------------
def est_ligne_valide(ligne: dict) -> (bool, str):
    champs = ["nom", "age", "ville"]
    for champ in champs:
        if not ligne.get(champ):
            return False, f"Champ {champ} vide"
    try:
        int(ligne["age"])
    except ValueError:
        return False, "Age non convertible en entier"
    return True, ""

def nettoyer_clients_csv(chemin_csv: Path):
    if not chemin_csv.exists():
        print(f"Fichier {chemin_csv} introuvable, merci de vérifier le chemin.")
        return

    propre = chemin_csv.with_name(chemin_csv.stem + "_propre.csv")
    erreurs = chemin_csv.with_name(chemin_csv.stem + "_erreurs.csv")

    lignes_valides = []
    lignes_invalides = []

    with chemin_csv.open("r", encoding="utf-8", newline="") as f:
        lecteur = csv.DictReader(f, delimiter=';')
        for ligne in lecteur:
            valide, raison = est_ligne_valide(ligne)
            if valide:
                lignes_valides.append(ligne)
            else:
                ligne_err = ligne.copy()
                ligne_err["raison"] = raison
                lignes_invalides.append(ligne_err)

    if lignes_valides:
        with propre.open("w", encoding="utf-8", newline="") as f:
            champs = lignes_valides[0].keys()
            writer = csv.DictWriter(f, fieldnames=champs, delimiter=';')
            writer.writeheader()
            writer.writerows(lignes_valides)

    if lignes_invalides:
        with erreurs.open("w", encoding="utf-8", newline="") as f:
            champs = list(lignes_invalides[0].keys())
            writer = csv.DictWriter(f, fieldnames=champs, delimiter=';')
            writer.writeheader()
            writer.writerows(lignes_invalides)

    print(f"CSV nettoyé : {propre} ({len(lignes_valides)} lignes valides)")
    print(f"CSV erreurs : {erreurs} ({len(lignes_invalides)} lignes invalides)")

# ------------------ JSON ------------------
def mettre_a_jour_config_json(chemin_config: Path):
    if not chemin_config.exists():
        print(f"Fichier {chemin_config} introuvable, merci de vérifier le chemin.")
        return

    backup = chemin_config.with_name(chemin_config.stem + "_backup.json")

    try:
        with chemin_config.open('r', encoding='utf-8') as f:
            config_orig = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Erreur : fichier JSON invalide ({e})")
        return

    shutil.copy(chemin_config, backup)
    print(f"Sauvegarde créée : {backup}")

    # Mise à jour
    config_nouv = config_orig.copy()
    config_nouv['debug'] = False
    ver_parts = config_nouv['version'].split('.')
    ver_parts[-1] = str(int(ver_parts[-1]) + 1)
    config_nouv['version'] = '.'.join(ver_parts)
    config_nouv['max_connexions'] += 10
    if 'admin' not in config_nouv['services']:
        config_nouv['services'].append('admin')
    config_nouv['theme'] = 'dark'

    # Écriture temporaire puis remplacement
    temp = chemin_config.with_suffix('.json.tmp')
    with temp.open('w', encoding='utf-8') as f:
        json.dump(config_nouv, f, ensure_ascii=False, indent=2)
    temp.replace(chemin_config)

    # Diff simple
    print("\nDiff configuration :")
    print(f"Ancienne version : {config_orig['version']}")
    print(f"Nouvelle version : {config_nouv['version']}")
    print(f"Ancien debug    : {config_orig['debug']}")
    print(f"Nouveau debug   : {config_nouv['debug']}")

# ------------------ Menu ------------------
if __name__ == "__main__":
    print("--- Outil de maintenance ---")
    print("1) Nettoyer les logs")
    print("2) Nettoyer le CSV clients")
    print("3) Mettre à jour config")

    choix = input("Votre choix : ").strip()

    if choix == "1":
        chemin = Path("logs") / "app.log"
        nettoyer_logs(chemin)
    elif choix == "2":
        chemin = Path("donnees") / "clients_brut.csv"
        nettoyer_clients_csv(chemin)
    elif choix == "3":
        chemin = Path("config_app.json")
        mettre_a_jour_config_json(chemin)
    else:
        print("Choix invalide.")
