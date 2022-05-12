# P3_Recommandation_Film
L’objectif est de mettre à disposition une API qui renverra les 5 films les plus proches d'un film choisi

## Analyse
28 dimensions de types quantitatives et qualitatives ou catégorielles

## Préprocessing
* One Hot Encoder pour traiter les données catégorielles
* Pour certaines catégories conservation uniquement des occurences les plus citées
* ACP : Réduction de dimensions
* T-SNE : Réduction de dimensions

## Modèle
* KNN : Plus proche voisin
* KMEANS : Création de groupe de films proches
* GOWER

## API
* Création d'une API avec FLASK
* Serialization du modèle
