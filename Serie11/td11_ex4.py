class ScoreBoard:
    def __init__(self):
        self.scores = {}

    def ajouter_points(self, nom_joueur, points):
        if nom_joueur not in self.scores:
            self.scores[nom_joueur] = 0
        self.scores[nom_joueur] += points

    def afficher(self):
        for joueur, score in self.scores.items():
            print(f"{joueur.capitalize()} : {score}")


if __name__ == "__main__":
    tableau = ScoreBoard()
    
    tableau.ajouter_points("joueur1", 10)
    tableau.ajouter_points("joueur2", 5)
    tableau.ajouter_points("invité", 7)
    
    tableau.afficher()  

"""
Pourquoi cette solution avec une classe est plus claire qu'une approche avec plusieurs variables globales :
1. Tous les scores sont centralisés dans un seul objet (self.scores), pas dispersés dans plusieurs variables.
2. Les méthodes ajoutent des points et affichent les scores, ce qui rend le code plus lisible et modulaire.
3. Il est facile d'ajouter de nouveaux joueurs : il suffit de passer un nouveau nom à ajouter_points sans modifier le reste du code.
4. L'état du score est encapsulé dans l'objet ScoreBoard, ce qui évite les effets de bord liés aux variables globales.
"""
