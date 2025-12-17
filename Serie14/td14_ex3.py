# td14_ex3.py
from dataclasses import dataclass


@dataclass
class Produit:
    nom: str
    prix_ht: float
    taux_tva: float = 0.2

    # -------------------------
    # MÉTHODES STATIQUES
    # -------------------------
    @staticmethod
    def est_prix_valide(prix: float) -> bool:
        """Renvoie True si le prix est valide (>= 0)."""
        return prix >= 0

    @staticmethod
    def format_euro(montant: float) -> str:
        """Formatte un montant en euros avec deux décimales."""
        return f"{montant:.2f} €"

    # -------------------------
    # POST-INIT & MÉTHODES
    # -------------------------
    def __post_init__(self):
        # Normalisation du nom
        self.nom = self.nom.strip()

        # Validation du prix
        if not Produit.est_prix_valide(self.prix_ht):
            raise ValueError(f"Prix HT invalide : {self.prix_ht}")

        # Validation de la TVA
        if not (0 <= self.taux_tva <= 1):
            raise ValueError(f"Taux de TVA invalide : {self.taux_tva}")

    def prix_ttc(self) -> float:
        """Calcule le prix TTC."""
        return self.prix_ht * (1 + self.taux_tva)

    def __str__(self):
        return (
            f"Produit {self.nom} – "
            f"{Produit.format_euro(self.prix_ht)} HT – "
            f"{Produit.format_euro(self.prix_ttc())} TTC"
        )


# ---------------------------------------------------------------
# MAIN : tests
# ---------------------------------------------------------------
if __name__ == "__main__":
    p1 = Produit("Ordinateur", 1200)
    p2 = Produit("  Clavier  ", 49.99)
    p3 = Produit("Souris", 25, taux_tva=0.1)

    print(p1)
    print(p2)
    print(p3)

    # Test invalides
    try:
        Produit("Casque", -10)
    except ValueError as e:
        print("Erreur détectée :", e)

    try:
        Produit("Micro", 50, taux_tva=1.5)
    except ValueError as e:
        print("Erreur détectée :", e)
