from flask import Flask

# Création de l'instance de l'application Flask
app = Flask(__name__)

# Définition d'une route pour afficher "Hello, World!"
@app.route('/')
def hello_world():
    return 'Hello, Samuel'

# Point d'entrée pour exécuter l'application Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0')
