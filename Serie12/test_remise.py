# test_remise.py
import unittest
from remise import calculer_prix_ttc

class TestCalculerPrixTTC(unittest.TestCase):

    def test_prix_normal(self):
        """Test avec un prix normal et TVA 20%"""
        prix_ht = 100
        taux_tva = 0.2
        expected = 120
        self.assertAlmostEqual(calculer_prix_ttc(prix_ht, taux_tva), expected)

    def test_prix_zero(self):
        """Test avec un prix HT nul"""
        prix_ht = 0
        taux_tva = 0.2
        expected = 0
        self.assertAlmostEqual(calculer_prix_ttc(prix_ht, taux_tva), expected)

    def test_prix_negatif(self):
        """Test que ValueError est levée pour un prix négatif"""
        with self.assertRaises(ValueError):
            calculer_prix_ttc(-50, 0.2)

if __name__ == "__main__":
    unittest.main()
