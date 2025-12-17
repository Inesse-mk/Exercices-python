from banque import CompteBancaire, virement


# Création de deux comptes
compte1 = CompteBancaire("Alice", 1000)
compte2 = CompteBancaire("Bob", 500)


print("Soldes initiaux :")
compte1.afficher()
compte2.afficher()


# Virement de 200€ d'Alice vers Bob
virement(compte1, compte2, 200)


print("\nAprès le virement :")
compte1.afficher()
compte2.afficher()



# EXPLICATION :


# 1. from banque.comptes import CompteBancaire
# - On importe directement la classe depuis le sous-module comptes.
# - On doit connaître le chemin complet du sous-module.


# 2. from banque import CompteBancaire
# - Grâce à __init__.py, le package expose directement les éléments souhaités.
# - Plus pratique : on ne fait pas référence aux sous-modules, on importe depuis le package.
# - Cela centralise et simplifie les imports pour l’utilisateur du package.
