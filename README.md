# MatrixEngine for Gauss & Laplace Method

MatrixEngine est une application Python avancée conçue pour explorer et appliquer des méthodes mathématiques complexes dans le domaine des opérations matricielles. Ce projet se distingue par sa capacité à comparer l'efficacité de la méthode de Gauss et de la méthode de Laplace dans l'inversion de matrices, offrant aux utilisateurs des insights précieux sur la performance algorithmique.

## Aperçu de MatrixEngine
![Aperçu de MatrixEngine](https://i.ibb.co/m0WMy17/Screenshot-2.png "Aperçu de MatrixEngine")

## Performance et Comparaison

MatrixEngine démontre la supériorité de la méthode de Gauss, avec une complexité algorithmique de l'ordre de ``(n^3)``, par rapport à la méthode de Laplace, dont la complexité est de l'ordre de ``(n^2(n-1)!``. Ces analyses permettent aux utilisateurs de déterminer la taille maximale des matrices inversibles en fonction du délai de calcul, qui peut être ajusté au nombre de secondes choisi par l'utilisateur, offrant ainsi une flexibilité optimale dans l'évaluation des performances.

## Caractéristiques Principales

- **Comparaison de Performance** : Analyse et compare la rapidité des méthodes de Gauss et de Laplace pour l'inversion de matrices.
- **Détermination de la Taille Maximale** : Identifie la taille maximale des matrices pouvant être inversées en fonction du temps de calcul spécifié par l'utilisateur.
- **Présentation des Résultats** : Affiche les temps de calcul dans un tableau comparatif, offrant une visualisation claire des performances relatives et de l'impact du temps de calcul défini par l'utilisateur.

## Technologies Utilisées

- **Python** : Le cœur du développement, choisi pour sa flexibilité et son large éventail de bibliothèques scientifiques.
- **Bibliothèques Python Intégrées** : 
  - `tkinter` pour la création de l'interface utilisateur graphique.
  - `threading` pour permettre l'exécution de plusieurs processus en parallèle.
  - `time` et `random` pour les fonctionnalités liées au temps et à la génération de nombres aléatoires.
  - Utilisation de `ttk` et `scrolledtext` de tkinter pour des composants d'interface avancés.

Ces bibliothèques intégrées facilitent la création d'une interface utilisateur riche et interactive, tout en gérant efficacement les opérations en arrière-plan et les fonctionnalités liées au temps.

## Structure du Projet

- `Interface` : Contient les composants de l'interface utilisateur pour la visualisation des données.
- `Matrice` : Modules dédiés aux opérations sur les matrices.
- `Method` : Implémente les algorithmes de Gauss et de Laplace, optimisés pour la performance.
- `main.py` : Script principal pour l'exécution et la gestion de l'application.

## Gestion des Erreurs

### Matrice Singulière

Lors de l'utilisation de MatrixEngine, vous pourriez rencontrer une erreur indiquant qu'une **matrice singulière** a été générée. Une matrice est dite singulière lorsqu'elle n'est pas inversible, ce qui peut poser problème lors de l'application des méthodes de Gauss ou de Laplace.

**Solution** : Si une telle erreur survient, il est recommandé de **relancer l'application**. À chaque redémarrage, MatrixEngine génère une nouvelle matrice de manière aléatoire.


## Installation

Pour installer et exécuter MatrixEngine :

```bash
# Cloner le dépôt
git clone https://github.com/sami-db/MatrixEngine.git
cd MatrixEngine

# Lancer l'application
python main.py
```
