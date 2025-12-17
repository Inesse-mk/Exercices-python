# test_service_remise_log.py
import unittest
from service_remise_log import appliquer_remise

class TestAppliquerRemise(unittest.TestCase):

    def test_remise_valide(self):
        """Test d'une remise valide : 100€ avec 10% → 90€"""
        prix_ht = 100
        remise = 0.1
        expected = 90
        self.assertAlmostEqual(appliquer_remise(prix_ht, remise), expected)

    def test_remise_invalide_negative(self):
        """Test qu'une remise négative lève une ValueError"""
        with self.assertRaises(ValueError):
            appliquer_remise(100, -0.1)

    def test_remise_invalide_sup_1(self):
        """Test qu'une remise > 1 lève une ValueError"""
        with self.assertRaises(ValueError):
            appliquer_remise(100, 1.5)

if __name__ == "__main__":
    unittest.main()
