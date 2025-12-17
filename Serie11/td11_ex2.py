#Utilisation excessive de global : Les fonctions modifient directement 
# une variable globale. Cela crée un couplage fort entre les fonctions 
# et la variable externe, rendant le code fragile et difficile à maintenir.

#Difficulté à tester et réutiliser : Les fonctions ne peuvent pas être 
# utilisées avec d’autres valeurs de score sans toucher à la variable globale.
score = 0

def ajouter_bonus(score):
    score += 5
    print("Nouveau score après bonus :", score)
    return score

def ajouter_malus(score):
    score -= 3
    print("Nouveau score après malus :", score)
    return score
# Scénario de test
score = ajouter_bonus(score)
score = ajouter_bonus(score)
score = ajouter_malus(score)
print("Score final :", score)