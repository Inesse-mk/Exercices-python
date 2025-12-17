# td13_ex2.py

class StockProduit:
    def __init__(self, nom: str, stock_initial: int = 0):
        self.nom = nom
        if stock_initial < 0:
            raise ValueError("Le stock initial doit être positif ou nul")
        self._stock = stock_initial  # attribut interne

    def ajouter(self, qte: int):
        if qte <= 0:
            raise ValueError("La quantité à ajouter doit être positive")
        self._stock += qte
        print(f"{qte} unités ajoutées. Stock actuel de {self.nom} : {self._stock}")

    def retirer(self, qte: int):
        if qte < 0:
            raise ValueError("La quantité à retirer doit être positive")
        if qte > self._stock:
            raise ValueError(f"Impossible de retirer {qte} unités. Stock disponible : {self._stock}")
        self._stock -= qte
        print(f"{qte} unités retirées. Stock actuel de {self.nom} : {self._stock}")

    def afficher_stock(self):
        print(f"Produit : {self.nom}, Stock actuel : {self._stock}")


if __name__ == "__main__":
    # Création du stock
    stock_clavier = StockProduit("Clavier", 10)
    stock_clavier.afficher_stock()

    # Ajout de stock
    stock_clavier.ajouter(5)

    # Retrait de stock valide
    stock_clavier.retirer(3)

    # Tentative de retrait trop important
    try:
        stock_clavier.retirer(20)
    except ValueError as e:
        print("Erreur :", e)

    # Tentative de retrait négatif
    try:
        stock_clavier.retirer(-5)
    except ValueError as e:
        print("Erreur :", e)

    # Exemple dangereux : modification directe de _stock
    # stock_clavier._stock = -100  # Cela contournerait toutes les règles métier !
    # print(stock_clavier._stock)
