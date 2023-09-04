from flask import request, jsonify  # Importation des fonctions nécessaires de Flask
from app import app, db  # Importation de l'application et de la base de données
from models import Review  # Importation du modèle avis

# Route pour gérer les avis
@app.route('/reviews', methods=['GET', 'POST'])
def manage_reviews():
    if request.method == 'POST':  # Si la méthode est POST
        data = request.get_json()  # Récupération des données envoyées
        review = Review(
            product_id=data['product_id'],
            content=data['content'],
            rating=data['rating'],
            user_id=data['user_id']
        )
        db.session.add(review)  # Ajout de l'avis à la session
        db.session.commit()  # Enregistrement des modifications
        return jsonify({"message": "Review added successfully!"}), 201  # Retourne un message de succès
    reviews = Review.query.all()  # Récupération de tous les avis
    return jsonify([r.serialize for r in reviews]), 200  # Retourne les avis au format JSON
