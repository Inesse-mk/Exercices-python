class produit :
    def __init__(self, nom, prix_HT, stock):
        self.nom = nom
        self.prix_HT = prix_HT
        self.stock = stock

    def prix_ttc(self, taux_tva):
        valeur = self.prix_HT + taux_tva
        return round(valeur, 2)
    
    def valeur_stock_ttc(self, taux_tva):
        valeur = self.prix_HT * (1 + taux_tva / 100) * self.stock
        return round(valeur, 2)
    
p1 = produit("Clavier", 49.99, 10)
p2 =produit("Souris", 19.99, 23)
p3 = produit("Chargeur", 30.99, 5)

catalogue = [p1, p2, p3]

somme = 0

for produit in catalogue:
    print(f"{produit.nom}, Prix HT {produit.prix_HT} €, Prix TTC {produit.prix_ttc(20)} €, Stock {produit.stock} €, Stock TTC {produit.valeur_stock_ttc(20)} €")

    somme += produit.valeur_stock_ttc(20)

    print (f" la somme de toutes les valeurs de stock TTC est : {somme} €")




