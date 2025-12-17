# td14_ex4.py

from dataclasses import dataclass, field
from typing import List

# ---------------------------------------------------------
# On importe le Produit depuis l’exercice précédent
# ---------------------------------------------------------
from td14_ex3 import Produit


# ---------------------------------------------------------
# Dataclass LigneFacture
# ---------------------------------------------------------
@dataclass
class LigneFacture:
    produit: Produit
    quantite: int

    total_ht: float = field(init=False)
    total_ttc: float = field(init=False)

    def __post_init__(self):
        if self.quantite <= 0:
            raise ValueError("La quantité doit être positive")

        self.total_ht = self.produit.prix_ht * self.quantite
        self.total_ttc = self.produit.prix_ttc() * self.quantite

    def __str__(self):
        return (
            f"{self.quantite} × {self.produit.nom} — "
            f"{Produit.format_euro(self.total_ht)} HT — "
            f"{Produit.format_euro(self.total_ttc)} TTC"
        )


# ---------------------------------------------------------
# Dataclass Facture
# ---------------------------------------------------------
@dataclass
class Facture:
    numero: int
    client: str
    lignes: List[LigneFacture]

    total_ht: float = field(init=False)
    total_ttc: float = field(init=False)

    def __post_init__(self):
        if not self.lignes:
            raise ValueError("Une facture doit contenir au moins une ligne")

        # Calcul des totaux
        self.recalculer_totaux()

    # Méthode privée utilitaire
    def recalculer_totaux(self):
        self.total_ht = sum(l.total_ht for l in self.lignes)
        self.total_ttc = sum(l.total_ttc for l in self.lignes)

    # Optionnel mais recommandé
    def ajouter_ligne(self, ligne: LigneFacture):
        self.lignes.append(ligne)
        self.recalculer_totaux()

    def __str__(self):
        lignes_str = "\n".join(str(l) for l in self.lignes)

        return (
            f"Facture n°{self.numero} – Client : {self.client}\n"
            f"{'-'*40}\n"
            f"{lignes_str}\n"
            f"{'-'*40}\n"
            f"Total HT  : {Produit.format_euro(self.total_ht)}\n"
            f"Total TTC : {Produit.format_euro(self.total_ttc)}"
        )


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
if __name__ == "__main__":
    # Produits
    p1 = Produit("Ordinateur", 1000)
    p2 = Produit("Clavier", 50)
    p3 = Produit("Souris", 25)

    # Lignes
    l1 = LigneFacture(p1, 1)
    l2 = LigneFacture(p2, 2)
    l3 = LigneFacture(p3, 3)

    # Facture
    facture = Facture(
        numero=123,
        client="Alice Dupont",
        lignes=[l1, l2, l3]
    )

    print(facture)

    # Test erreur : facture vide
    try:
        Facture(999, "Client Test", [])
    except ValueError as e:
        print("Erreur détectée :", e)
