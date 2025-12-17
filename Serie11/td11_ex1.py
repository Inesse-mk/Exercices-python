# Le score global ne sera jamais modifié, car Python n’arrivera 
# même pas à exécuter la fonction jusqu’au bout.
# Non, il va planter.
# Type d'erreur : UnboundLocalError.
# Type d'erreur : UnboundLocalError: cannot access local variable 'score' where
# it is not associated with a value
# Dès qu'une variable est assignée dans une fonction, Python la traite
# automatiquement comme locale, même si une variable globale du même nom existe.
score = 0

def ajouter_points(score, points):
    
    print("Score avant :", score)
    score = score + points
    print("Score après :", score)
   
ajouter_points(score, 10)