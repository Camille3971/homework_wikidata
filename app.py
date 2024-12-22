#Importer les modules nécessaires
from flask import Flask, render_template
import requests

#Création de l'application Flask
app = Flask(__name__, template_folder='templates')

#Définition d'une route Flask pour accéder à une URL spécifique
@app.route("/retrieve_wikidata/<string:id>")
def retrieve_wikidata(id:str):
    """
    Cette fonction récupère les données de Wikidata pour un ID spécifique et les affiche dans un modèle HTML.
    """
    try:
        # Effectuer une requête GET à l'API de Wikidata avec l'ID donné
        result = requests.get(f"https://www.wikidata.org/wiki/Special:EntityData/{id}.json",params={"format": "json"})
        http_response = result.status_code
        content_type = result.headers.get('Content-Type')
        
        #Extraire les données JSON de la réponse
        data = result.json()

        # Vérifier si les données contiennent l'entité associée à l'ID
        if data and "entities" in data and id in data["entities"]:
            # Rendre le modèle HTML avec les données et les métadonnées
            return render_template(
                  "retrieve_wikidata.html",
                  http_code=f"{http_response}",
                  content_type=f"{content_type}",
                  entity=data,
                  id=id)
        else:
            # Rendre le modèle HTML en cas d'absence de données valides
            return render_template(
                  "retrieve_wikidata.html",
                  http_code=f"{http_response}",
                  content_type=f"{content_type}",
                  error_message=f"Aucune donnée valide n'a été retournée pour l'id {id}",
                  id=id)
    except:
        # Gérer les erreurs (par exemple, échec de la requête ou JSON invalide)
        return render_template(
              "retrieve_wikidata.html",
              http_code="none",
              content_type="none",
              error_message=f"Aucune donnée valide n'a été retournée pour l'id {id}",
              id=id)
# Lancer l'application Flask sur le port par défaut (5000)
app.run()
