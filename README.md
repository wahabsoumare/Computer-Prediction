# Prédiction des prix des ordinateurs

Ce projet vise à créer un système de prédiction des prix des ordinateurs basé sur une analyse approfondie des données historiques des prix, des caractéristiques des produits et des tendances du marché. Le modèle prédictif sera capable de fournir des estimations précises des prix futurs, aidant ainsi les acheteurs à déterminer le meilleur moment pour acheter et les revendeurs à ajuster leurs stratégies de prix.

## Description du projet

### Objectifs
1. Collecter les données historiques des prix des ordinateurs.
2. Nettoyer, exploiter et normaliser ces données.
3. Analyser les données pour identifier les tendances et les corrélations entre les variables d'entrée et la sortie (prix).
4. Entraîner et valider plusieurs modèles de machine learning pour prédire les prix des ordinateurs.
5. Déployer le modèle sélectionné via une API construite avec Flask, accompagnée d'une interface utilisateur en HTML avec Bootstrap.

### Modèles utilisés
Plusieurs modèles ont été testés pour prédire les prix des ordinateurs, incluant :
- Régression linéaire
- Rigde
- Forêts aléatoires
- KNN
- Support Vector Machine

Le modèle ayant la meilleure performance, en termes de précision et d'efficacité, a été sélectionné pour le déploiement.

## Déploiement

Le système de prédiction des prix des ordinateurs a été déployé en utilisant Flask pour créer une API et un formulaire HTML avec Bootstrap pour l'interface utilisateur. 

### Prérequis
Avant de commencer, assurez-vous d'avoir toutes les dépendances requises dans le fichier `requirements.txt`. Vous pouvez installer les dépendances avec la commande suivante :

```bash
pip install -r requirements.txt

Lancer l'application :

    - Clonez ce repository sur votre machine locale.
    - Assurez-vous que toutes les dépendances sont installées (voir ci-dessus).
    - Dans votre terminal, exécutez le fichier main.py pour démarrer l'application Flask :
    ```python
    python main.py
    - Accédez à l'application via votre navigateur à l'adresse suivante : http://127.0.0.1:8000.

Vous pourrez alors saisir les caractéristiques de l'ordinateur dans le formulaire HTML et obtenir une prédiction du prix.

## Structure du projet : 
.
├── Data/                     # Dossier contenant le jeu de données
│   └── laptop_data.csv       # Jeu de données des prix des ordinateurs portables
├── Deploiement/              # Dossier contenant le code source du déploiement
│   ├── main.py               # Fichier principal pour lancer l'API Flask
│   └── templates/            # Dossier contenant les fichiers HTML
│       └── index.html        # Interface utilisateur avec formulaire Bootstrap
├── requirements.txt          # Liste des dépendances nécessaires
├── script.ipynb              # Notebook contenant les scripts d'entraînement et le modèle
└── README.md                 # Documentation du projet

Étapes du projet

    Collecte des données : Télécharger le jeu de données nécessaire.
    Nettoyage et exploitation des données : Traitement des valeurs manquantes et création de variables dérivées.
    Exploration et analyse des données : Identification des tendances et des corrélations entre les caractéristiques des produits et les prix.
    Entraînement et validation des modèles : Sélection des modèles et évaluation de leur performance avec des métriques telles que MAE, RMSE et R².
    Déploiement : Mise en place d'une API avec Flask et d'un formulaire HTML pour une interface utilisateur interactive.

Critères d'évaluation

Le projet sera évalué en fonction des critères suivants :

    Efficacité et précision du modèle entraîné.
    Qualité et convivialité de l'interface utilisateur.
    Fiabilité et performance du système en déploiement.

Conclusion

Ce projet permet de prédire le prix d'un ordinateur en fonction de ses caractéristiques, en utilisant plusieurs modèles de machine learning. L'application déployée permet aux utilisateurs d'entrer les spécifications d'un ordinateur et de recevoir une estimation précise de son prix sur la base des modèles entraînés.