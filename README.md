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
python -m server.app
```

**Accéder l'application**

Ouvrez votre navigateur à l'adresse : http://localhost:5000 .

**Utiliser la calculatrice**

1. Cliquez sur les boutons numériques pour entrer les chiffres
2. Cliquez sur un opérateur (+, -, *, /)
3. Entrez le deuxième nombre
4. Cliquez sur "=" pour calculer
5. Utilisez "C" pour effacer l'affichage

**Arrêter l'application**

Entrez `CTRL + C` dans le terminal

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

### Structure des branches

- `main`: code stable et testé
- `Issue#<nombre>--Bugfix-<nom du bug>` : corrections de bugs
- `Issue#<nombre>--Feature-<nom de la feature>` : nouvelle focntionnalité

### Flux de travail

**1. Créer une issue** <br/>
Décrivez le bug ou la fonctionnalité sur GitHub avec les étapes de reproduction.

**2. Créer une branche**

    git checkout main
    git pull origin main
    git checkout -b <nom-branche>

**3. Développer et commit**

    git add .
    git commit -m "Fix: Description de la correction"

- Conventions de commit :
  - `fix: ` pour les corrections
  - `feature: ` pour les nouvelles fonctionnalités
  - `docs: ` pour la documentation
  - `test: ` pour les tests

**4. Pousser et créer une pull request (PR)**

    git push origin bugfix/nom-du-bug
Créer une Pull Request sur GitHub vers `main` avec description des changements

**5. Revue et fusion** <br/>
Au moins 1 membre de l'équipe doit approuver.


