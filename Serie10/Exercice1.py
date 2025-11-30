# Données brutes
donnees_produits = [
    {"id": 1, "nom": "Clavier",  "categorie": "Informatique", "prix": 39.99, "stock": 10},
    {"id": 2, "nom": "Souris",   "categorie": "Informatique", "prix": 19.99, "stock": 0},
    {"id": 3, "nom": "Écran",    "categorie": "Informatique", "prix": 129.90, "stock": 5},
    {"id": 4, "nom": "Chaise",   "categorie": "Bureau",       "prix": 89.90, "stock": 2}
]

# Classe Produit
class Produit:
    def __init__(self, id, nom, categorie, prix, stock):
        self.id = id
        self.nom = nom
        self.categorie = categorie
        self.prix = prix
        self.stock = stock

    def est_en_rupture(self):
        return self.stock == 0

    def afficher_resume(self):
        print(f"[{self.categorie}] {self.nom} - {self.prix}€ (stock: {self.stock})")

# Classe Catalogue
class Catalogue:
    def __init__(self):
        self.produits = []

    def ajouter_produit(self, produit):
        self.produits.append(produit)

    def produits_par_categorie(self, categorie):
        return [p for p in self.produits if p.categorie == categorie]

    def prix_moyen(self):
        if not self.produits:
            return 0
        return sum(p.prix for p in self.produits) / len(self.produits)

    def produits_en_rupture(self):
        return [p for p in self.produits if p.est_en_rupture()]

# Bloc principal
if __name__ == "__main__":
    catalogue = Catalogue()

    # Conversion des dicts en objets Produit et ajout dans le catalogue
    for data in donnees_produits:
        produit = Produit(**data)
        catalogue.ajouter_produit(produit)

    # Affichage du prix moyen
    print(f"Prix moyen des produits : {catalogue.prix_moyen():.2f}€\n")

    # Produits en rupture
    print("Produits en rupture :")
    for p in catalogue.produits_en_rupture():
        p.afficher_resume()
    print()

    # Produits de la catégorie "Informatique"
    print('Produits de la catégorie "Informatique" :')
    for p in catalogue.produits_par_categorie("Informatique"):
        p.afficher_resume()
