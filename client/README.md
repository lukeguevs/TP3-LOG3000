# **Module Client**

## Raison d'être
Le module client contient l'interface utilisateur de la calculatrice.

Il est responsable de la présentation visuelle et de l'interaction avec l'utilisateur dans le navigateur web.

### Structure du module

    client/
    ├── templates/
    │   └── index.html       # HTML de la calculatrice
    └── static/
        └── style.css        # Feuille de style CSS

## Fichiers principaux

### `templates/index.html`

**Responsabilités**

- Définit la structure HTMl de l'interface utilisateur de la calculatrice.

**Fonctionnalités**

- Affichage de l'expression et du résultat dans un champ de texte en lecture seule
- Grille de boutons pour les chiffres 0-9 et les opérateurs (+,-,*,/)
- Bouton Clear (C) pour effacer l'affichage
- Bouton égal (=) qui soumet le formulaire au serveur pour le calcul
- Fonctions JavaScript pour manipuler l'affichage côté client


### `static/style.css`

**Responsabilités**

- Définit l'apparence visuelle de tous les éléments de l'interface

**Styles principaux**

- Centrage de la calculatrice sur la page avec flexbox
- Design sombre moderne (fond gris foncé #333)
- Grille de bouton responsive
- Différentiation visuelle des opérateurs (couleur orange #ff9500)
- Effets hover et active pour une meilleure expérience utilisateur

## Dépendances

### Dépendances externes

- Flask
- Navigateur web moderne

### Dépendances internes

- Module `server` pour
  - Le traitement des calculs soumis via POST
  - Le routage Flask
