from pathlib import Path
import sys

# Chemin vers le fichier de logs
fichier_logs = Path("logs") / "app.log"

# Vérification de l'existence du fichier
if not fichier_logs.exists():
    print(f"Erreur : le fichier {fichier_logs} est introuvable.")
    sys.exit(1)

# Initialisation des compteurs
nb_total = 0
nb_error = 0
nb_warning = 0

# Lecture ligne par ligne pour compter et filtrer
# On évite f.read() pour ne pas charger tout le fichier en mémoire
# (utile pour les fichiers très volumineux)
with fichier_logs.open("r", encoding="utf-8") as f:
    for ligne in f:
        nb_total += 1
        if "[ERROR]" in ligne:
            nb_error += 1
        if "[WARNING]" in ligne:
            nb_warning += 1

# Affichage du rapport
print(f"Lignes totales  : {nb_total}")
print(f"Lignes WARNING  : {nb_warning}")
print(f"Lignes ERROR    : {nb_error}")

# Filtrage des lignes DEBUG et écriture dans un nouveau fichier
fichier_sans_debug = Path("logs") / "app_sans_debug.log"
with fichier_logs.open("r", encoding="utf-8") as fin, \
     fichier_sans_debug.open("w", encoding="utf-8") as fout:
    for ligne in fin:
        if "[DEBUG]" in ligne:
            continue
        fout.write(ligne)

print(f"Fichier filtré créé : {fichier_sans_debug}")
