# Définition de la classe Produit
class produit :
    def __init__(self, nom, prix_HT, stock):
        # Constructeur : initialise le nom, le prix hors taxes et le stock
        self.nom = nom
        self.prix_HT = prix_HT
        self.stock = stock
    # Méthode pour calculer le prix TTC d'un produit
    def prix_ttc(self, taux_tva):
        # Correction : le prix TTC = prix_HT * (1 + taux_tva/100)
        valeur = self.prix_HT + taux_tva
        return round(valeur, 2)
    # Méthode pour calculer la valeur totale du stock en TTC
    def valeur_stock_ttc(self, taux_tva):
        valeur = self.prix_HT * (1 + taux_tva / 100) * self.stock
        return round(valeur, 2)

# Création des produits   
p1 = produit("Clavier", 49.99, 10)
p2 =produit("Souris", 19.99, 23)
p3 = produit("Chargeur", 30.99, 5)
# Catalogue de produits
catalogue = [p1, p2, p3]

somme = 0

# Parcours du catalogue pour afficher les informations et calculer la valeur totale du stock
for produit in catalogue:
    print(f"{produit.nom}, Prix HT {produit.prix_HT} €, Prix TTC {produit.prix_ttc(20)} €, Stock {produit.stock} €, Stock TTC {produit.valeur_stock_ttc(20)} €")

    somme += produit.valeur_stock_ttc(20)
# Affichage de la somme totale des valeurs de stock TTC
print (f" la somme de toutes les valeurs de stock TTC est : {somme} €")




