#Importer les modules nécessaires
from flask import Flask
from routes import configure_routes

# Création de l'application Flask
app = Flask(__name__, template_folder='templates')

# Configuration des routes
configure_routes(app)

# Lancer l'application
if __name__ == "__main__":
    app.run()
