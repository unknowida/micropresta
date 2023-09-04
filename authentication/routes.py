from flask import request, jsonify  # Importation des fonctions nécessaires de Flask
from flask_jwt_extended import create_access_token, jwt_required  # Outils JWT pour la gestion des tokens
from app import app, db  # Importation de l'application et de la base de données
from models import User  # Importation du modèle utilisateur
from wtforms import Form, StringField, PasswordField, validators
# Se protéger contre les attaques par force brute, vous pouvez ajouter une limite de taux aux routes sensibles.
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address



#Validation des Entrées Utilisateur : Il est important de valider les données envoyées par l'utilisateur lors de l'inscription et de la connexion pour se protéger contre les attaques comme l'injection SQL.
class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=20)])
    password = PasswordField('Password', [validators.DataRequired()])

# Fonctionnalité pour permettre aux utilisateurs de réinitialiser leur mot de passe.
@app.route('/reset_password', methods=['POST'])
def reset_password():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user:
        token = create_access_token(identity=user.username)
        return jsonify({"access_token": token}), 200
    return jsonify({"message": "Invalid credentials!"}), 401

#La tenue de journaux d'audit peut être utile pour suivre les activités des utilisateurs et pour le débogage.
import logging

logging.basicConfig(level=logging.INFO)

def log_event(event_message):
    logging.info(event_message)
    


limiter = Limiter(get_remote_address, app=app)

@app.route('/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        token = create_access_token(identity=user.username)
        return jsonify({"access_token": token}), 200
    return jsonify({"message": "Invalid credentials!"}), 401



@app.route('/')
def index():
    return "Service d'authentification en cours d'exécution"

# Route d'enregistrement
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()  # Récupération des données envoyées
    user = User(username=data['username'])  # Création d'un nouvel utilisateur
    user.set_password(data['password'])  # Définition du mot de passe
    db.session.add(user)  # Ajout de l'utilisateur à la session
    db.session.commit()  # Enregistrement des modifications
    return jsonify({"message": "User registered successfully!"}), 201  # Retourne un message de succès

# Route de connexion
# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()  # Récupération des données envoyées
#     user = User.query.filter_by(username=data['username']).first()  # Recherche de l'utilisateur par nom d'utilisateur
#     # Vérification du mot de passe et création du token
#     if user and user.check_password(data['password']):
#         token = create_access_token(identity=user.username)  # Création d'un token d'accès
#         return jsonify({"access_token": token}), 200  # Retourne le token
#     return jsonify({"message": "Invalid credentials!"}), 401  # Retourne un message d'erreur en cas d'échec

# Route de profil
@app.route('/profile', methods=['GET'])
@jwt_required()  # Nécessite un token valide
def profile():
    current_user = get_jwt_identity()  # Récupère l'identité de l'utilisateur actuel
    user = User.query.filter_by(username=current_user).first()  # Recherche de l'utilisateur par nom d'utilisateur
    return jsonify({"username": user.username}), 200  # Retourne le nom d'utilisateur

