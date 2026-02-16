# **Module Server**

## Raison d'être
Le module client contient la logique backend de la calculatrice Flask

Il est responsable du traitement des expressions arithmétiques, du routage HTTP, <br/>
et de la coordination entre interface et opérations de calcul.

### Structure du module

    server/
    ├── __init__.py          # Fichier d'initialisation du package
    ├── app.py               # Application Flask principale avec routage
    └── operators.py         # Fonctions des opérations arithmétiques

## Fichiers principaux

### `app.py`

**Responsabilités**

- Module principal qui configure et exécute le serveur Flask.

**Fonctionnalités**

- Initialisation de l'application Flask
- Configuration du dossier de templates vers `../client/templates`
- Définition du dictionnaire `OPS` mappant les symboles aux fonctions
- Fonction `calculate()` pour évaluer les expressions
- Route `/` gérant les requêtes GET (affichage) et POST (calcul)


### `operators.py`

**Responsabilités**

- Implémente les 4 opérations arithmétiques de base.

**Fonctions disponibles**

- `add(a,b)` 
- `substract(a,b)` 
- `multiply(a,b)`
- `divide(a,b)`

## Dépendances

### Dépendances externes

- Flask
  - Fonctions importées : `Flask`, `request`, `render_template`

### Dépendances internes

- `app.py` importe les fonctions depuis `operators.py`
- Module `client` pour 
  - Template HTMl
  - Fichier statique CSS
