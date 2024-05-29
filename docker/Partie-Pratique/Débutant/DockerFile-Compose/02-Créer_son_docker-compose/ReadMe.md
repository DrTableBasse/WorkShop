# But de l'exercice

Ici, nous allons utiliser l'image que nous avons crées dans l'exercice précédent pour faire un fichier docker-compose.yml

# Etape à suivre : 
1) Lister les prérequis suivants : 
    - Quelle image on utilise ? 
    - Quel port nous allons ouvrir ? 
    - Doit-on le mettre sur un réseau virtuel privé ?
    - Doit-on avoir un stockage pour cette application conteneurisée ?

2) Création de son fichier docker-compose :
    - Créer un fichier docker-compose.yml
    - Modifier la template suivante pour s'adapter au besoin
    - Lancer le docker compose grâce à la commande suivante :  `docker compose up`

```docker
# Template à utiliser
version: '3.8' # syntaxe utilisée

services: # liste de tous les services qu'on utilise
  nginx: #nom du service
    image: nginx:latest # l'image qu'on va utiliser
    container_name: my_nginx_server # le nom de mon conteneur
    ports:
      - "80:80" # le port sur lequel je l'expose
```

Si vous arrivez à tout lancer, que vous n'avez pas d'erreur, **félicitatations !**, vous êtes maintenant un vrai crack de docker !\
On va passer à l'étape suivante qui sera d'utilisé des images que nous n'avons pas faites au préalable (**<u>à faire uniquement pour du dev</u>**).