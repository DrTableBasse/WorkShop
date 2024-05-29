# Correction

## 1) Récupérer les images nécessaires
```bash
docker pull wordpress
docker pull mariadb
```

## 2) Créer le fichier docker-compose.yml

```docker
version: '3.7'

services:
  db:
    image: mariadb
    container_name: db
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: somewordpress
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
    volumes:
      - db_data:/var/lib/mysql

  wordpress:
    image: wordpress
    container_name: wordpress
    restart: always
    ports:
      - "8000:80"
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress
    volumes:
      - wordpress_data:/var/www/html

volumes:
  db_data:
  wordpress_data:
```

### Explication du fichier docker-compose.yml

Nous utilisons la version 3.7 de Docker Compose.
Nous avons deux services : db pour la base de données MariaDB et wordpress pour le site WordPress.
Le service db utilise l'image MariaDB et configure les variables d'environnement pour définir le mot de passe root, le nom de la base de données, l'utilisateur et le mot de passe.
Le service wordpress utilise l'image WordPress et configure les variables d'environnement pour indiquer à WordPress comment se connecter à la base de données MariaDB.
Les volumes sont utilisés pour persister les données de la base de données et du site WordPress entre les redémarrages des conteneurs.

## 3) Lancer l'application WordPress
```bash
docker-compose up -d
```
Cela lancera les conteneurs MariaDB et WordPress en arrière-plan.

## 4) Accéder au site WordPress

Ouvrez un navigateur web et accédez à l'adresse http://localhost:8000 pour accéder à votre site WordPress fraîchement installé.

## 5) Arrêter et supprimer les conteneurs

```bash
docker-compose down
```
Ceci arrêtera et supprimera les conteneurs, mais les données persistantes seront toujours disponibles dans les volumes créés.