from app import db  # Importation de l'objet db depuis app

# Modèle avis
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # ID unique pour chaque avis
    product_id = db.Column(db.Integer, nullable=False)  # ID du produit associé
    content = db.Column(db.String(500), nullable=False)  # Contenu de l'avis
    rating = db.Column(db.Integer, nullable=False)  # Note donnée
    user_id = db.Column(db.Integer, nullable=False)  # ID de l'utilisateur ayant donné l'avis
