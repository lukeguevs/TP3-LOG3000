"""
Module contenant les opérations arithmétiques de base définies
"""

def add(a,b):
    # Additionne 2 nombres

    return a + b

def subtract(a,b):
    # Soustrait le premier nombre du deuxième

    return b - a

def multiply(a,b):
    # Multiplie 2 nombres

    return a * b

def divide(a,b):
    # Effectue une division de a par b
    # Arrondie à 8 décimales près, pour contourner le problème de la virgule flottante en Python
    return round(a / b, 8)
