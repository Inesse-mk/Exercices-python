# td11_ex3_initial.py

# Programme initial avec variables globales
score_joueur1 = 0
score_joueur2 = 0

def ajouter_points_j1(points):
    global score_joueur1
    score_joueur1 += points

def ajouter_points_j2(points):
    global score_joueur2
    score_joueur2 += points

def afficher_scores():
    print("Joueur 1 :", score_joueur1)
    print("Joueur 2 :", score_joueur2)

# Scénario de jeu
ajouter_points_j1(10)
ajouter_points_j2(5)
ajouter_points_j1(7)
afficher_scores()

"""
Problèmes liés à l’usage des variables globales dans ce code :
1. Lisibilité : Les fonctions modifient des variables externes sans qu’on le voit directement.
2. Testabilité : Impossible de tester les fonctions isolément, car elles dépendent de l’état global.
3. Evolutivité : Ajouter un troisième joueur nécessiterait de créer de nouvelles variables globales et de nouvelles fonctions, ce qui rend le code rapidement difficile à maintenir.
4. Risque d’effets de bord : Toute modification accidentelle des variables globales ailleurs dans le code peut casser le programme.
"""
