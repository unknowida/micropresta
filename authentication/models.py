from app import db  # Importation de l'objet db depuis app
from werkzeug.security import generate_password_hash, check_password_hash  # Outils pour gérer les mots de passe

# Modèle utilisateur
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # ID unique pour chaque utilisateur
    username = db.Column(db.String(80), unique=True, nullable=False)  # Nom d'utilisateur unique
    password_hash = db.Column(db.String(128))  # Hash du mot de passe

    # Méthode pour définir le mot de passe
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Méthode pour vérifier le mot de passe
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
