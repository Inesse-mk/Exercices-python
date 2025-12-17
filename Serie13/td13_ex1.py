class Produit:
    # attribut de classe
    taux_tva = 0.2

    def __init__(self, nom: str, prix_ht: float):
        if prix_ht < 0:
            raise ValueError("Le prix HT doit être positif")
        # attributs d'instance
        self.nom = nom
        self.prix_ht = prix_ht

    def prix_ttc(self) -> float:
        """Renvoie le prix TTC en utilisant le taux de TVA de la classe"""
        return self.prix_ht * (1 + Produit.taux_tva)


if __name__ == "__main__":
    # Création de deux produits
    produit1 = Produit("Ordinateur", 1000)
    produit2 = Produit("Clavier", 50)

    # Affichage des prix HT et TTC
    for p in (produit1, produit2):
        print(f"{p.nom} : prix HT = {p.prix_ht:.2f} €, prix TTC = {p.prix_ttc():.2f} €")

    print("\n--- Modification du taux de TVA ---")
    # Modification de l'attribut de classe
    Produit.taux_tva = 0.1

    # Affichage après modification
    for p in (produit1, produit2):
        print(f"{p.nom} : prix HT = {p.prix_ht:.2f} €, prix TTC = {p.prix_ttc():.2f} €")
