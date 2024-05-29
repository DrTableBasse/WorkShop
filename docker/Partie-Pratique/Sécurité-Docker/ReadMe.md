# Cours sur la Sécurité avec Docker

La sécurité est un aspect crucial de la gestion des conteneurs Docker. Ce cours couvre les meilleures pratiques et stratégies pour sécuriser vos environnements Docker.

## 1. Utiliser des Images Sûres et Vérifiées
Utilisation d'Images Officielles

Les images officielles sur Docker Hub sont généralement maintenues par les éditeurs de logiciels ou par des mainteneurs de confiance. Elles sont régulièrement mises à jour et vérifiées pour les vulnérabilités.

**Exemple** :

```bash
docker pull nginx:latest
docker pull mysql:latest
```

### Scanner les Images pour les Vulnérabilités

Utilisez des outils comme Trivy, Clair, ou Anchore pour scanner les images Docker à la recherche de vulnérabilités.

**Installation de Trivy** :

```bash
sudo apt-get install wget apt-transport-https gnupg lsb-release
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee -a /etc/apt/sources.list.d/trivy.list
sudo apt-get update
sudo apt-get install trivy
```
**Scanner une image avec Trivy** :
```bash
trivy image nom_de_limage
```
*PS : il existe de nombreux outils comme [Docker Scout](https://docs.docker.com/scout/) et [Snyk](https://snyk.io/fr/) pour faire des scans d'images*

## 2. Limiter les Permissions et les Privilèges

**Ne pas Exécuter les Conteneurs en tant que Root**

Exécuter les conteneurs en tant qu'utilisateur non root réduit les risques en cas de compromission du conteneur.

**Exemple dans un Dockerfile** :

```docker
FROM nginx:latest
USER nginx
```

### Utiliser les Capabilities Linux

Réduisez les privilèges en utilisant les capabilities Linux pour donner au conteneur seulement les permissions nécessaires.

**Exemple** :

```bash
docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE nginx:latest
```


## 3. Isolation des Espaces de Montage (mnt) dans Docker

L'isolation des espaces de montage (mnt) est une caractéristique importante de Docker qui permet de limiter l'accès des conteneurs aux systèmes de fichiers de l'hôte. En sécurisant les montages, vous pouvez éviter que des conteneurs compromis n'aient accès à des fichiers sensibles de l'hôte ou d'autres conteneurs.

**1. Limiter les Montages de Volumes**

Limitez les volumes montés aux répertoires strictement nécessaires au bon fonctionnement de votre application. Évitez de monter des volumes en lecture-écriture sauf si nécessaire.

**Exemple** :
```yaml
version: '3.7'

services:
  app:
    image: myapp:latest
    volumes:
      - /path/to/data:/data:ro   # Lecture seule
      - /path/to/config:/config:rw  # Lecture-écriture
```

**2. Utiliser des Volumes Només**

Les volumes nommés offrent une meilleure isolation que les montages de répertoires hôtes. Ils sont gérés par Docker et permettent d'éviter l'accès direct aux fichiers système de l'hôte.

**Exemple** :

```yaml
version: '3.7'

services:
  db:
    image: mysql:latest
    volumes:
      - db_data:/var/lib/mysql

volumes:
  db_data:
```

**3. Utiliser les Options de Montage "noexec", "nosuid", et "nodev"**

Appliquez les options de montage pour limiter les permissions sur les volumes montés. Cela peut empêcher l'exécution de binaires ou de scripts malveillants.

**Exemple** :
```yaml
version: '3.7'

services:
  app:
    image: myapp:latest
    volumes:
      - /path/to/data:/data:ro,noexec,nosuid,nodev
```

**4. Utiliser des Espaces de Montage Isolés avec les namespaces**

Docker utilise les namespaces pour fournir une isolation forte entre les conteneurs et l'hôte. Le namespace mnt permet de créer des espaces de montage distincts pour chaque conteneur.

**Exemple de script pour vérifier les namespaces** :

```bash
# Voir les namespaces montés pour un conteneur
docker inspect --format='{{.State.Pid}}' my_container | xargs -I {} lsns | grep mnt
```

**5. Utiliser tmpfs pour des Volumes Temporaires**

Pour des données temporaires, utilisez des volumes tmpfs, qui sont stockés en mémoire et ne persistent pas sur le disque. Cela améliore la sécurité en évitant d'écrire des données sensibles sur le disque.

**Exemple** :

```yaml
version: '3.7'

services:
  app:
    image: myapp:latest
    tmpfs:
      - /run
      - /tmp
```


## 4. Utiliser des Politiques de Réseau et des Firewalls

**Isoler les Conteneurs**

Utilisez des réseaux Docker pour isoler les conteneurs et limiter leur communication.\
**Création d'un Réseau Isolé** :

```bash
docker network create secure_network
docker run -d --network secure_network nginx
```

**Configurer des Firewalls**

Configurez des règles de firewall pour limiter l'accès aux conteneurs.\
**Exemple avec iptables** :

```bash
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT
iptables -A INPUT -p tcp --dport 3306 -j DROP
```

## 5. Mettre en Place des Contrôles d'Accès

**Utiliser des Secrets et des Variables d'Environnement Sécurisées**

Stockez les secrets de manière sécurisée en utilisant Docker secrets ou des gestionnaires de secrets comme HashiCorp Vault.
Exemple avec Docker Secrets :

**1) Créez un secret** :
```bash
echo "my_secret_password" | docker secret create db_password -
```
**2) Utilisez le secret dans un service Docker Compose** :

```yaml
version: '3.7'

services:
  db:
    image: mysql:latest
    secrets:
      - db_password

secrets:
  db_password:
    external: true
```
**Contrôler l'Accès aux Daemons Docker**

Limitez l'accès au daemon Docker uniquement aux utilisateurs autorisés.

**Exemple avec TLS** :

*1) Créez des certificats TLS pour sécuriser l'accès :*
```bash
openssl genrsa -aes256 -out ca-key.pem 4096
openssl req -new -x509 -days 365 -key ca-key.pem -sha256 -out ca.pem
```

*2) Configurez le daemon Docker pour utiliser les certificats TLS :*

```json
{
  "tls": true,
  "tlsverify": true,
  "tlscacert": "/path/to/ca.pem",
  "tlscert": "/path/to/server-cert.pem",
  "tlskey": "/path/to/server-key.pem",
  "hosts": ["tcp://0.0.0.0:2376"]
}
```

## 6. Monitorer et Logger les Activités
**Utiliser des Outils de Monitoring**

Intégrez des outils de monitoring comme Prometheus et Grafana pour surveiller l'activité des conteneurs et détecter des comportements anormaux.

**Exemple avec Docker Compose** :
```yaml
version: '3.7'

services:
  prometheus:
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
```

**Configurer des Logs**

Assurez-vous que les logs des conteneurs sont stockés et analysés.

**Exemple avec une configuration de logging JSON :**
```yaml
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  }
}
```

## 7. Garder Docker à Jour

### Mise à Jour Régulière

Maintenez Docker à jour pour bénéficier des dernières fonctionnalités et correctifs de sécurité.

**Exemple de mise à jour sur Ubuntu** :
```bash
sudo apt-get update
sudo apt-get upgrade docker-ce
```
