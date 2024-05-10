# Exercice 1
## Objectifs
- Créer sa propre image docker faisant tourner un serveur web en python
- Utiliser les fichiers fournis dans le répertoire (app.py et requirements.txt)
- Faire tourner le conteneur sur le port 5000
- Avoir une page par défaut affichant "Hello + <prénom>"

Vous devez avoir le résultat suivant :\
![alt text](src/Image%20collée.png)

### Procéder aux tests
#### Avec python sur votre PC
- Installer python et penser à cocher la case pour le path (bien suivre l'installation de python)
- Installer [pip](https://www.guru99.com/fr/how-to-install-pip-on-windows.html)
- Faire la commande suivante dans le répertoire de l'exercice :
```python
pip install -r requirements.txt
```
- Tester si votre application fonctionne :
```python
python app.py
```
Vous aurez le résultat suivant dans votre terminal 
```bash
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.27.65:5000
Press CTRL+C to quit
```

## Méthodes pour faire l'exercice
- Faire via la commande `docker init`
- Faire le DockerFile à la main
