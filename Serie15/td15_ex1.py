class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        print("L'animal fait un bruit.")


class Chien(Animal):
    def __init__(self, nom):
        super().__init__(nom)

    def parler(self):
        print(f"{self.nom} aboie : Wouf !")


class Chat(Animal):
    def __init__(self, nom):
        super().__init__(nom)

    def parler(self):
        print(f"{self.nom} miaule : Miaou !")


if __name__ == "__main__":
    animaux = [
        Animal("Mystère"),
        Chien("Rex"),
        Chat("Minou")
    ]

    for animal in animaux:
        animal.parler()
