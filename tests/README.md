# **Module Tests**

## Raison d'être
Le module tests contient tous les tests unitaires et d'intégration pour valider <br/> 
le bon fonctionnement de la calculatrice Flask. Il utilise le framework pytest <br/> 
pour exécuter et organiser les tests, garantissant la qualité et la fiabilité du <br/> 
code avant toute mise en production.

### Structure du module

    tests/
    ├── test_operators.py    # Tests des fonctions arithmétiques
    └── __init__.py          # (optionnel) Fichier d'initialisation du package

## Fichiers principaux

### `test_operators.py`

**Responsabilités**

- Teste toutes les opérations arithmétiques définies dans `server/operators.py`

**Classes de tests:**

-

## Dépendances

### Dépendances externes

- pytest

### Dépendances internes

- `server.operators`
