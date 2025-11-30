
class rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def surface(self):
        return  self.largeur * self.hauteur 
    
    def perimetre(self):
        return (self.largeur+ self.hauteur) * 2
    
    def afficher(self):
        print (f"Rectangle ; largeur = {self.largeur},hauteur = {self.hauteur}")

r1 = rectangle(4,5)
r2 = rectangle(10,2)

r1.afficher()
print (f"la surface du rectangle est : {r1.surface()}")
print (f"Le perimetre de rectangle est : {r1.perimetre()}")

r2.afficher()
print (f"la surface du rectangle est : {r2.surface()}")
print (f"Le perimetre de rectangle est : {r2.perimetre()}")




