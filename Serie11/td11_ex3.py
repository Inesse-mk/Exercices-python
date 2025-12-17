# Scores stockés dans un dictionnaire
scores = {
    "joueur1": 0,
    "joueur2": 0,
}

def ajouter_points(scores, nom_joueur, points):
    """
    Ajoute 'points' au joueur indiqué dans le dictionnaire 'scores'.
    Renvoie le dictionnaire modifié.
    """
    if nom_joueur in scores:
        scores[nom_joueur] += points
    else:
        print(f"Erreur : {nom_joueur} n'existe pas dans le dictionnaire.")
    return scores

def afficher_scores(scores):
    """
    Affiche les scores actuels des joueurs.
    """
    for joueur, score in scores.items():
        print(f"{joueur.capitalize()} : {score}")

# Scénario de jeu (même que le programme initial)
scores = ajouter_points(scores, "joueur1", 10)
scores = ajouter_points(scores, "joueur2", 5)
scores = ajouter_points(scores, "joueur1", 7)
afficher_scores(scores)

"""
Pourquoi ce code est plus simple à faire évoluer pour ajouter un troisième joueur :
- Il suffit d’ajouter une nouvelle clé dans le dictionnaire 'scores', par exemple 'joueur3': 0.
- La fonction ajouter_points() fonctionne automatiquement pour n’importe quel joueur présent dans le dictionnaire.
- On n’a pas besoin de créer de nouvelles variables globales ni de nouvelles fonctions pour chaque joueur.
- Le code reste modulable et facile à tester.
"""
