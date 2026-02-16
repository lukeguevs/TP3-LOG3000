"""
Tests unitaires pour le module server.app.

Ce module vérifie le bon fonctionnement de l'application Flask :
- Fonction calculate() : parsing et évaluation des expressions arithmétiques
- Route index() : gestion des requêtes GET et POST
- Validation des expressions et gestion des erreurs

Les tests couvrent la logique de calcul, les cas d'erreurs,
ainsi que les interactions HTTP avec l'application web.
"""

import pytest
from server.app import app, calculate

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestCalculateFunction:
    """
    Suite de tests pour la fonction calculate()
    qui parse et évalue les expressions arithmétiques.
    """

    # Tests des opérations valides
    def test_calculate_addition(self):
        assert calculate("3 + 5") == 8

    def test_calculate_subtraction(self):
        assert calculate("2 - 2") == 0

    def test_calculate_multiplication(self):
        assert calculate("6 * 7") == 42

    def test_calculate_division(self):
        assert calculate("8 / 2") == 4

    # Tests de validation des expressions
    def test_calculate_invalid_expression(self):
        with pytest.raises(ValueError, match="invalid expression format"):
            calculate("+")

    def test_calculate_multiple_operators(self):
        with pytest.raises(ValueError, match="only one operator is allowed"):
            calculate("3 + 5 - 2")

    def test_calculate_non_numeric_operands(self):
        with pytest.raises(ValueError, match="operands must be numbers"):
            calculate("a + b")

class TestIndexRoute:
    """
    Suite de tests pour la route index() de l'application Flask,
    teste les requêtes GET et POST ainsi que le rendu des templates.
    """

    # Tests de la route GET
    def test_index_get(self, client):
        response = client.get('/')
        assert response.status_code == 200
        assert b"" in response.data

    # Tests de la route POST avec expressions valides
    def test_index_post_valid_expression(self, client):
        response = client.post('/', data={'display': '3 + 5'})
        assert response.status_code == 200
        assert b"8" in response.data

    # Tests de la route POST avec expressions invalides
    def test_index_post_invalid_expression(self, client):
        response = client.post('/', data={'display': '3 + '})
        assert response.status_code == 200
        assert b"Error: invalid expression format" in response.data