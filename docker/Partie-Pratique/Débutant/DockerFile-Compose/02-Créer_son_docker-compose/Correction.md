# Corrections 

# 1) Première Méthode : 

```docker

version: '3.8'

services:
  web:
    image: nom_de_votre_image:version #nom de notre image avec la version que l'on souhaite (soit on met latest soit on met rien pour préciser la dernière version)
    ports: # port d'entrée de l'host vers le port du conteneur
      - "5000:5000" 
    volumes: # permet de dire que le répertoire commun équivaut au répertoire app dans le conteneur
      - .:/app


```

# 2) Deuxième Méthode :

```docker
version: '3.8'

services:
  web:
    build: # on va directement build à la suite du docker compose up. Ca permet d'être plus rapide et de ne pas build puis faire son compose.*

      context: . # quels fichier on va ajouter dans notre conteneur (. = tous dans le répertorie commun) 
      dockerfile: Dockerfile # le nom du DockerFile
    ports: # liste des ports sur lequel on expose
      - "5000:5000"
    volumes: # permet de dire que le répertoire commun équivaut au répertoire app dans le conteneur
      - .:/app 
```
