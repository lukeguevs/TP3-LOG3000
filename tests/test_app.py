import pytest
from server.app import app, calculate

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_calculate_addition():
    assert calculate("3 + 5") == 8

def test_calculate_subtraction():
    assert calculate("10 - 4") == 6

def test_calculate_multiplication():
    assert calculate("6 * 7") == 42

def test_calculate_division():
    assert calculate("8 / 2") == 4

def test_calculate_invalid_expression():
    with pytest.raises(ValueError, match="invalid expression format"):
        calculate("+")

def test_calculate_multiple_operators():
    with pytest.raises(ValueError, match="only one operator is allowed"):
        calculate("3 + 5 - 2")

def test_calculate_non_numeric_operands():
    with pytest.raises(ValueError, match="operands must be numbers"):
        calculate("a + b")

def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"" in response.data

def test_index_post_valid_expression(client):
    response = client.post('/', data={'display': '3 + 5'})
    assert response.status_code == 200
    assert b"8" in response.data

def test_index_post_invalid_expression(client):
    response = client.post('/', data={'display': '3 + '})
    assert response.status_code == 200
    assert b"Error: invalid expression format" in response.data