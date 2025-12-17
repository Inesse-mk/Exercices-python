import json
from pathlib import Path
import shutil

fichier_config = Path("config_app.json")
fichier_backup = Path("config_app_backup.json")

def mettre_a_jour_config(config: dict) -> dict:
    # Mise à jour du debug
    config['debug'] = False

    # Incrémentation simple de version (dernier chiffre)
    # Exemple : '1.0.0' -> '1.0.1'
    ver_parts = config['version'].split('.')
    ver_parts[-1] = str(int(ver_parts[-1]) + 1)
    config['version'] = '.'.join(ver_parts)

    # Augmentation de max_connexions
    config['max_connexions'] += 10

    # Ajout du service 'admin' si absent
    if 'admin' not in config['services']:
        config['services'].append('admin')

    # Changement de theme
    config['theme'] = 'dark'

    return config

try:
    # Lecture de la configuration
    with fichier_config.open('r', encoding='utf-8') as f:
        config_orig = json.load(f)
except json.JSONDecodeError as e:
    print(f"Erreur : le fichier JSON est invalide ({e})")
    exit(1)

# Création de la sauvegarde
shutil.copy(fichier_config, fichier_backup)
print(f"Sauvegarde créée : {fichier_backup}")

# Mise à jour de la configuration
config_nouvelle = mettre_a_jour_config(config_orig.copy())

# Écriture dans un fichier temporaire
fichier_temp = fichier_config.with_suffix('.json.tmp')
with fichier_temp.open('w', encoding='utf-8') as f:
    json.dump(config_nouvelle, f, ensure_ascii=False, indent=2)

# Remplacement du fichier original
fichier_temp.replace(fichier_config)

# Affichage du diff textuel
print("\nDiff de configuration :")
print(f"Ancienne version : {config_orig['version']}")
print(f"Nouvelle version : {config_nouvelle['version']}")
print(f"Ancien debug    : {config_orig['debug']}")
print(f"Nouveau debug   : {config_nouvelle['debug']}")