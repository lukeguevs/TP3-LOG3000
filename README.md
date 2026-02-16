# TP3 LOG3000

### Nom du projet : TP3 LOG3000 
### Numéro d'équipe: 33
- Lucas Guevremont
- Marianne Bédard-Brosseau
- Nicolas Champagne


## Objectif

L'objectif de ce projet est de développer une calculatrice disponbile sur le web, qui peut effectuer des calculs de base. 
<br/> La calculatrice doit être facile à utiliser et accessible à tous les utilisateurs.

## Architecture du projet
    TP3_LOG3000/
    ├── client/                      # Module frontend
    │   ├── templates/
    │   │   └── index.html           # Interface HTML
    │   └── static/
    │       └── style.css            # Styles CSS
    ├── server/                      # Module backend
    │   ├── app.py                   # Application Flask
    │   └── operators.py             # Opérations arithmétiques
    ├── tests/                       # Tests unitaires
    │   └── test_operators.py
    └── requirements.txt             # Dépendances Python

## Prérequis d'installation

- Posséder Python et pip.
- Git installé localement.
- Un compte GitHub pour le dépôt du projet.
- Un éditeur de code (comme Visual Studio Code, PyCharm, etc.).

### Vérifier les installations
    python --version
    pip --version
    git --version

## Guide d'installation

### 1. Cloner le dépôt
```text 
git clone <url>
cd TP3_LOG3000
```

### 2. Installer les dépendances
```text 
pip install flask pytest
```

## Instructions d'utilisation
**Lancer l'application**

```
python server/app.py
```

## Tests

Afin d'exécuter les tests, assurez-vous d'avoir installé pytest. <br/> Si vous ne l'avez pas encore fait, vous pouvez l'installer en utilisant pip : <br/>
```text 
pip install pytest
```
Ensuite, pour exécuter les tests, ouvrez votre terminal, naviguez jusqu'au répertoire de votre projet et lancez la commande suivante à partir de la racine du projet :
```text 
python -m pytest
```

## Flux de contribution


