# td14_ex1.py
from dataclasses import dataclass

@dataclass
class Produit:
    nom: str
    prix_ht: float
    taux_tva: float = 0.2  # 20 % par défaut

    def __post_init__(self):
        # Normalisation du nom
        self.nom = self.nom.strip()

        # Vérification des contraintes métier
        if self.prix_ht < 0:
            raise ValueError(f"Prix HT invalide pour {self.nom} : {self.prix_ht} (doit être positif)")
        if not (0 <= self.taux_tva <= 1):
            raise ValueError(f"Taux de TVA invalide pour {self.nom} : {self.taux_tva} (doit être entre 0 et 1)")

    def prix_ttc(self) -> float:
        """Renvoie le prix TTC"""
        return self.prix_ht * (1 + self.taux_tva)

    def __str__(self) -> str:
        return f"Produit {self.nom} – {self.prix_ht:.2f} € HT – {self.prix_ttc():.2f} € TTC"


if __name__ == "__main__":
    # Création de produits valides
    produit1 = Produit("Ordinateur", 1000)
    produit2 = Produit(" Clavier ", 50)
    produit3 = Produit("Souris", 25, taux_tva=0.1)

    # Affichage
    print(produit1)
    print(produit2)  # Le nom sera normalisé sans espaces
    print(produit3)

    # Test d'un produit invalide (prix négatif)
    try:
        produit_invalide = Produit("Casque", -30)
    except ValueError as e:
        print("Erreur détectée :", e)

    # Test d'un produit invalide (taux de TVA > 1)
    try:
        produit_invalide2 = Produit("Micro", 50, taux_tva=1.5)
    except ValueError as e:
        print("Erreur détectée :", e)
