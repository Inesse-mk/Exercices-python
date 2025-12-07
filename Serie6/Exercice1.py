# Définition d'une classe Rectangle
class rectangle:
    def __init__(self, largeur, hauteur):
    # Constructeur : initialise les dimensions du rectangle
        self.largeur = largeur
        self.hauteur = hauteur
    # Méthode pour calculer la surface
    def surface(self):
        return  self.largeur * self.hauteur 
    # Méthode pour calculer le périmètre
    def perimetre(self):
        return (self.largeur+ self.hauteur) * 2
    # Méthode pour afficher les dimensions
    def afficher(self):
        print (f"Rectangle ; largeur = {self.largeur},hauteur = {self.hauteur}")
# Création de deux rectangles
r1 = rectangle(4,5)
r2 = rectangle(10,2)
# Affichage et calculs pour r1
r1.afficher()
print (f"la surface du rectangle est : {r1.surface()}")
print (f"Le perimetre de rectangle est : {r1.perimetre()}")
# Affichage et calculs pour r2
r2.afficher()
print (f"la surface du rectangle est : {r2.surface()}")
print (f"Le perimetre de rectangle est : {r2.perimetre()}")




