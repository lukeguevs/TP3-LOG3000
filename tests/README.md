# **Module Tests**

## Raison d'être
Le module tests contient tous les tests unitaires et d'intégration pour valider <br/> 
le bon fonctionnement de la calculatrice Flask. Il utilise le framework pytest <br/> 
pour exécuter et organiser les tests, garantissant la qualité et la fiabilité du <br/> 
code avant toute mise en production.

### Structure du module

    tests/
    ├── test_app.py          # Tests de l'application Flask
    └── test_operators.py    # Tests des fonctions arithmétiques

## Fichiers principaux

### `test_app.py`

**Responsabilités**

- Teste l'application Flask définie dans `server/app.py`
- Valide la fonction `calculate()` qui parse et évalue les expressions arithmétiques
- Vérifie les routes HTTP (GET & POST) 
- Vérifie le rendu des templates
- Teste la gestion des erreurs et des expressions invalides

**Classes de tests:**

- `TestCalculateFunction` : tests de la fonction calculate()
  - Opérations valides (addition, soustraction, multiplication, division)
  - Validation des expressions (invalides, opérateurs multiples, opérandes non numériques)
- `TestIndexRoute` : tests de la route index()
  - Requêtes GET (affichage de l'interface)
  - Requêtes POST avec expressions valides
  - Requêtes POST avec expressions invalides (gestion des erreurs)

**Fixture:**
- `client()` : Configure un client de test Flask pour simuler des requêtes HTTP

### `test_operators.py`

**Responsabilités**

- Teste toutes les opérations arithmétiques définies dans `server/operators.py`
- Couvre les cas normaux, cas limites et gestion des erreurs
- Valide le comportement correct de chaque opération (addition, soustraction, multiplication, division)

**Classes de tests:**

- `TestOperators` : suite de tests pour les fonctions arithmétiques
  - `test_add()` : Addition de nombres positifs, négatifs et avec zéro
  - `test_subtract()` : Soustraction avec résultats positifs et négatifs
  - `test_multiply()` : Multiplication simple, avec grands nombres et par zéro
  - `test_divide()` : Division exacte, avec décimales et division par zéro (erreur)

## Dépendances

### Dépendances externes

- **pytest** (version 6.x ou supérieure recommandée) : Framework de tests unitaires Python
- **unittest** : Module de tests unitaires standard de Python (inclus avec Python)

### Dépendances internes

- `server.operators` : module contenant les fonctions arithmétiques à tester
- `server.app` : module contenant l'application Flask et la fonction calculate()
