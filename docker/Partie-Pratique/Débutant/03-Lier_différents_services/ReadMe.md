# Explications

Il est bien de pouvoir créer des services à la volet et les conteneuriser MAIS comment faire pour relié des services entre eux ? Nous allons voir ça ici\
*Pour plus de simplicité, nous allons utiliser une image wordpress fournie par Wordpress eux même.*
\
\
Parfois, les images docker sur internet (comme celle de Wordpress) ont des variables d'environnement (une présentation va être faite car on a aussi quelques point à voir) qu'il faut préciser. Ca permet, suivant les cas, de faire un gros travail pré-déploiement.\
Par chance, docker fait très bien les choses, on a plusieurs instructions dans docker-compose permettant de relier un service à un autre.\


### Différences entre variables d'environnement dans Docker Compose

1. **environment :**
   - `environment` est une option de Docker Compose qui permet de définir des variables d'environnement spécifiques à un service.
   - Ces variables d'environnement sont définies dans le fichier Docker Compose et sont passées au conteneur lorsqu'il est démarré.
   - Les valeurs des variables d'environnement peuvent être des chaînes de caractères, des nombres ou d'autres types de données.
   - Utilisé pour fournir des configurations spécifiques au service, telles que les informations de connexion à une base de données ou les paramètres de configuration de l'application.

2. **env_file :**
   - `env_file` est une autre option de Docker Compose qui permet de charger des variables d'environnement à partir d'un fichier externe.
   - Le fichier spécifié par `env_file` peut contenir plusieurs variables d'environnement, chaque ligne représentant une variable dans le format `NOM_VARIABLE=valeur`.
   - Les variables d'environnement définies dans le fichier `env_file` sont également passées au conteneur lorsqu'il est démarré, en plus de celles définies dans la section `environment`.
   - Utile pour séparer les variables d'environnement du fichier Docker Compose principal et pour éviter de stocker des informations sensibles dans le fichier de configuration principal.

3. **.env file :**
   - En plus de `env_file`, Docker Compose prend également en charge un fichier spécial nommé `.env` situé dans le même répertoire que votre fichier Docker Compose.
   - Les variables d'environnement définies dans le fichier `.env` sont automatiquement chargées dans l'environnement Docker Compose lorsqu'il est démarré.
   - Cela permet de définir des variables d'environnement par défaut qui seront utilisées par toutes les commandes Docker Compose dans ce répertoire, à moins qu'elles ne soient explicitement définies dans d'autres fichiers de configuration.
   - Pratique pour définir des variables d'environnement globales ou par défaut pour votre projet Docker Compose.

### Différences entre depends_on et links dans Docker Compose

1. **depends_on :**
   - `depends_on` est une option de Docker Compose qui permet de spécifier l'ordre dans lequel les services doivent être démarrés.
   - Il contrôle l'ordre de démarrage des services mais ne garantit pas que le service dépendant est prêt à recevoir des connexions lorsque le service sur lequel il dépend est démarré.
   - Principalement utilisé pour orchestrer l'ordre de démarrage des services.

2. **links :**
   - `links` est une option de Docker Compose qui permet de créer des connexions réseau entre les conteneurs Docker.
   - Permet de créer des liens unidirectionnels entre les services, permettant à un service d'accéder à un autre service en utilisant le nom du service comme nom d'hôte.
   - Utilisé pour établir des connexions réseau entre les services afin de faciliter la communication entre eux.


# Partie pratique 

## But de l'exercice

Héberger sur sa machine un site Wordpress relié à une base de données <u>**MariaDB**</u>

## 1) Récupérer les différentes images
*Cette étape n'est pas obligatoire du faire que lorsqu'on veut utiliser docker compose, si l'image n'est pas trouvée, votre machine le prendra directement sur docker hub en se basant sur un indice de confiance*\
Rien de plus simple, cherchez les images sur [docker hub](https://hub.docker.com/) (il vous faut un compte au cas où)\
Ensuite, faite la commande suivante : 
```bash
docker pull <nom de l'image>
```
On va aller récupérer sur docker hub l'image avec le même nom et on va la télécharger sur notre machine.

## 2) Créer son fichier `compose.yml`

On va reprendre les fichiers qu'on avait fait en changeant bien sûr les différentes informations pour correspondre à ce que l'on souhaite faire.\
Pensez à créer des volumes avec la commande suivante : 
```bash
docker volume create <nom du volume>
```

Pour un peu vous aider, voici tous les environnements suivants les services : 

#### Maria DB
```docker
    environment:
      - MYSQL_ROOT_PASSWORD=somewordpress
      - MYSQL_DATABASE=wordpress
      - MYSQL_USER=wordpress
      - MYSQL_PASSWORD=wordpress
```

#### Wordpress
```docker
    environment:
      - WORDPRESS_DB_HOST=db
      - WORDPRESS_DB_USER=wordpress
      - WORDPRESS_DB_PASSWORD=wordpress
      - WORDPRESS_DB_NAME=wordpress
```