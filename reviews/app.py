from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Initialiser l'application Flask
app = Flask(__name__)
app.config.from_object(Config)

# Initialiser SQLAlchemy pour la gestion de la base de données
db = SQLAlchemy(app)

# Importer les routes après l'initialisation de l'app
from routes import *

if __name__ == '__main__':
    with app.app_context():  # Création d'un contexte d'application
        db.create_all()  # Créer la base de données si elle n'existe pas
    app.run()  # Démarrer l'application
