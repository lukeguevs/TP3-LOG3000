"""
Tests unitaires pour le module server.operators.

Ce module vérifie le bon fonctionnement des opérations arithmétiques :
- Addition
- Soustraction
- Multiplication
- Division

Les tests couvrent des cas normaux, des cas limites,
ainsi que la gestion des erreurs (ex. division par zéro).
"""

import unittest
from server.operators import add, subtract, multiply, divide


class TestOperators(unittest.TestCase):
    """
    Suite de tests pour les fonctions arithmétiques
    définies dans le module server.operators.
    """

    # Tests de l'addition
    def test_add(self):
        # Addition de nombres positifs
        self.assertEqual(add(2, 3), 5)
        # Addition d'un nombre négatif et positif
        self.assertEqual(add(-1, 1), 0)
        # Addition avec zéro
        self.assertEqual(add(0, 0), 0)

    # Tests de la soustraction
    def test_subtract(self):
        # Résultat négatif
        self.assertEqual(subtract(2, 3), -1)
        # Résultat positif
        self.assertEqual(subtract(5, 2), 3)
        # Soustraction avec zéro
        self.assertEqual(subtract(0, 0), 0)

    # Tests de la multiplication
    def test_multiply(self):
        # Multiplication simple
        self.assertEqual(multiply(2, 3), 6)
        # Multiplication de nombres plus grands
        self.assertEqual(multiply(5, 2), 10)
        # Multiplication par zéro
        self.assertEqual(multiply(0, 10), 0)

    # Tests de la division entière
    def test_divide(self):
        # Division exacte
        self.assertEqual(divide(6, 3), 2)
        # Vérification de la division entière (troncature)
        self.assertEqual(divide(5, 2), 2)
        # Vérifie qu'une division par zéro lève une exception
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)


if __name__ == "__main__":
    # Permet d'exécuter les tests directement via ce fichier
    unittest.main()
