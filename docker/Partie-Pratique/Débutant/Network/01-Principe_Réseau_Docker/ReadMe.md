# Explication

Docker utilise des réseaux pour permettre aux conteneurs de communiquer entre eux et avec l'extérieur. La gestion des réseaux dans Docker est un aspect crucial pour orchestrer les conteneurs et garantir une communication sécurisée et efficace. Docker propose plusieurs types de réseaux, chacun ayant des caractéristiques et des cas d'utilisation spécifiques.

## Types de Réseaux Docker

### 1. Bridge Network

Le réseau par défaut pour les conteneurs Docker. Les conteneurs connectés à un réseau bridge peuvent communiquer entre eux, mais, à moins d’être explicitement configurés, ils ne peuvent pas être accessibles depuis l'extérieur.

- **Utilisation** : Idéal pour les configurations simples où plusieurs conteneurs doivent communiquer sur une même machine.
- **Commandes** :
  ```bash
  docker network create --driver bridge mon_bridge
  docker run -d --name mon_conteneur --network mon_bridge nginx
    ```
### 2. Host Network

Le réseau host permet à un conteneur de partager directement le réseau de l'hôte Docker. Cela signifie qu'il n'y a pas de couche d'abstraction réseau entre le conteneur et l'hôte.

- **Utilisation** :\
    Utile pour les applications nécessitant une performance réseau maximale et moins d'isolation.
    
- **Commandes** :
    ```bash
    docker run -d --network host nginx
    ```

### 3. None Network

Un conteneur sur un réseau none n'a aucun accès réseau. Cela isole complètement le conteneur du réseau.

- **Utilisation** :\
    Utile pour les tâches qui ne nécessitent pas de connectivité réseau.
    
- **Commandes** :
    ```bash
    docker run -d --network none nginx
    ```

#### 4. Overlay Network

Les réseaux overlay sont utilisés pour créer des réseaux qui s'étendent sur plusieurs hôtes Docker. Ils sont principalement utilisés dans les environnements Docker Swarm pour permettre aux conteneurs sur différents hôtes de communiquer de manière sécurisée.

- **Utilisation** :\
Idéal pour les déploiements distribués et les clusters Docker Swarm.
- **Commandes** :
```bash
docker network create -d overlay mon_overlay
docker service create --name mon_service --network mon_overlay nginx
```

#### 5. Macvlan Network

Les réseaux Macvlan permettent d'attribuer une adresse MAC unique à chaque conteneur, faisant apparaître chaque conteneur comme un appareil physique sur le réseau.

- **Utilisation** :\
Utile lorsque des configurations réseau traditionnelles sont nécessaires.
- **Commandes** :
```bash
docker network create -d macvlan \
  --subnet=192.168.1.0/24 \
  --gateway=192.168.1.1 \
  -o parent=eth0 mon_macvlan
docker run -d --network mon_macvlan --name mon_conteneur nginx
```


## Gestion des Réseaux Docker

### Liste des Réseaux

Pour lister tous les réseaux Docker sur la machine, utilisez :
```bash
docker network ls
```
### Inspection d'un Réseau

Pour obtenir des détails sur un réseau spécifique, utilisez :

```bash
docker network inspect mon_reseau
```
### Suppression d'un Réseau

Pour supprimer un réseau Docker, utilisez :
```bash
docker network rm mon_reseau
```

### Connexion et Déconnexion de Conteneurs à des Réseaux

Pour connecter un conteneur à un réseau existant :
```bash
docker network connect mon_reseau mon_conteneur
```

### Pour déconnecter un conteneur d'un réseau :

```bash
docker network disconnect mon_reseau mon_conteneur
```

## Conclusion

La gestion des réseaux dans Docker est essentielle pour orchestrer les conteneurs de manière efficace et sécurisée. Comprendre les différents types de réseaux et leurs cas d'utilisation permet de concevoir des architectures conteneurisées robustes et performantes.


# Exercice sur les Réseaux Docker

Comprendre les concepts de base des réseaux Docker, comment les utiliser pour connecter des conteneurs entre eux, et comment configurer manuellement les adresses IP des conteneurs.

**Instructions** :

    Créez un réseau Docker nommé "mon_reseau" avec un sous-réseau spécifique.
    Lancez deux conteneurs :
        Le premier conteneur doit être un conteneur NGINX nommé "nginx1", connecté au réseau "mon_reseau" avec l'adresse IP "172.18.0.10".
        Le deuxième conteneur doit être un conteneur MySQL nommé "mysql1", également connecté au réseau "mon_reseau" avec l'adresse IP "172.18.0.11".
    Vérifiez que les deux conteneurs sont correctement connectés au réseau "mon_reseau" et ont les adresses IP attribuées.
    Vérifiez que les conteneurs peuvent se pinguer entre eux sur le réseau en utilisant les adresses IP attribuées.
    Supprimez le réseau "mon_reseau" et les deux conteneurs.

**Conseils** :

    Utilisez les commandes docker network create, docker run, docker network connect, docker network inspect, et docker exec.
    Assurez-vous de bien comprendre la configuration des sous-réseaux et des adresses IP dans Docker.
    Utilisez la documentation Docker pour vous guider dans la configuration des adresses IP.

**Ressources** :
- Documentation Docker sur les réseaux : [Docker Networking](https://docs.docker.com/network/)
- Documentation Docker sur les commandes : [Docker CLI](https://docs.docker.com/engine/reference/commandline/cli/)

Cet exercice permettra aux débutants de se familiariser non seulement avec la création et la gestion de réseaux Docker, mais aussi avec la configuration manuelle des adresses IP pour les conteneurs.