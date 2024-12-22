from flask import Flask, render_template
import requests
app = Flask(__name__, template_folder='templates')

@app.route("/retrieve_wikidata/<string:id>")
def retrieve_wikidata(id:str):
    try:
        result = requests.get(f"https://www.wikidata.org/wiki/Special:EntityData/{id}.json",params={"format": "json"})
        http_response = result.status_code
        content_type = result.headers.get('Content-Type')
        data = result.json()
        if data and "entities" in data and id in data["entities"]:
            return render_template("retrieve_wikidata.html",http_code=f"{http_response}",content_type=f"{content_type}",entity=data)
        else:
            return render_template("retrieve_wikidata.html",http_code=f"{http_response}",content_type=f"{content_type}",error_message=f"Aucune donnée valide n'a été retournée pour l'id {id}")
    except:
        return render_template("retrieve_wikidata.html",http_code="none",content_type="none",error_message=f"Aucune donnée valide n'a été retournée pour l'id {id}")
app.run()