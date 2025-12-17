import td16_ex2_module

print("Avant l'appel à demo()")
td16_ex2_module.demo()
print("Après l'appel à demo()")


# EXPLICATIONS :

# Le bloc if __name__ == "__main__":
# ----------------------------------
# Il sert à exécuter du code SEULEMENT si le fichier est lancé directement
# (ex: python td16_ex2_module.py).

# Quand un fichier est importé, ce bloc NE s'exécute PAS.

# Exécuté directement :
# __name__ == "__main__"

# Importé comme module :
# __name__ == "td16_ex2_module"
