from math import pi


class Forme:
    def aire(self):
        # Méthode générique, à surcharger dans les sous-classes
        raise NotImplementedError("Méthode aire() à implémenter dans les sous-classes")


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur


class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return pi * (self.rayon ** 2)


class TriangleRectangle(Forme):
    def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return (self.base * self.hauteur) / 2


# Fonction illustrant le polymorphisme
# Elle fonctionne pour toutes les formes SANS tester leur type
# car chaque objet possède une méthode aire().
def afficher_aires(formes):
    for f in formes:
        print(f"Forme : {type(f).__name__}, aire = {f.aire()}")


# --- MAIN ---
if __name__ == "__main__":
    formes = [
        Rectangle(4, 5),
        Rectangle(10, 2),
        Cercle(3),
        Cercle(5),
        TriangleRectangle(6, 4)
    ]

    # Affichage direct
    for f in formes:
        print(f"Forme : {type(f).__name__}, aire = {f.aire()}")

    print("\nAvec la fonction polymorphe :")
    afficher_aires(formes)
