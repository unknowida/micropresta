import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///products.db'  # URI de la base de données pour les produits
    PRESTASHOP_API_URL = os.environ.get('PRESTASHOP_API_URL')  # URL de l'API PrestaShop
    PRESTASHOP_API_KEY = os.environ.get('PRESTASHOP_API_KEY')  # Clé API de PrestaShop
