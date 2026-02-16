"""
Module contenant les opérations arithmétiques de base définies
"""

def add(a,b):
    """
    Additionne deux nombres

    Args:
        a (float): Premier opérande
        b (float): Deuxième opérande

    Returns:
        float: La somme de a et b
    """

    return a + b

def subtract(a,b):
    """
    Soustrait le 2e nombre du 1er

    Args:
        a (float): Premier opérande (la base)
        b (float) : Deuxième opérande (à soustraire de la base)

    Returns:
        float: La différence a - b
    """

    return a - b

def multiply(a,b):
    """
    Multiplie 2 nombres

    Args:
        a (float): Premier opérande
        b (float) : Deuxième opérande

    Returns:
        float: Le produit a*b
    """

    return a * b

def divide(a,b):
    """
    Effectue une division de a par b
    Arrondie à 8 décimales près, pour contourner le problème de la virgule flottante en Python

    Args:
        a (float): Premier opérande (dividende)
        b (float) : Deuxième opérande (diviseur)

    Returns:
        float: Le quotient a/b
    """
    return round(a / b, 8)
