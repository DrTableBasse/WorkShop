# DockerFile
```docker
# Utilisation de l'image Python officielle comme base
FROM python:3.9-slim

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copie du fichier requirements.txt contenant les dépendances
COPY requirements.txt .

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source de l'application dans le conteneur
COPY . .

# Commande de démarrage pour exécuter l'application avec Flask
CMD ["python", "app.py"]
```

# Docker init 

```bash
# ouvrir son terminal dans le répertoire courant
docker init

# répondre aux questions en se basant sur le DockerFile
```

# Lancer le conteneur
```bash
docker build -t testworkshop .

docker run -p 5000:5000 testworkshop #ajouter la verbose -d pour l'avoir en arrière plan
```

# Vérification
Aller sur votre navigateur et taper [`localhost:5000`](http://localhost:5000)