class Tache:
    def __init__(self, titre, description="", statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut


    def afficher(self):
        print(f"Titre : {self.titre}")
        print(f"Description : {self.description}")
        print(f"Statut : {self.statut}")
        print("-" * 30)