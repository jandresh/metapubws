#!/usr/bin/env python
#
# Este scriptmuestra como consumir un *endpoint*  que 
# accede a un web service que consulta por artículos de 
# la base de datos pubmed.
#
# Para ejecutar este script debe ejecutar los siguientes pasos:
#  virtualenv venv
#  . venv/bin/activate
#  sudo apt-get install libxml2-dev libxslt-dev python-dev
#  pip3 install Flask metapub
#  export FLASK_APP=metapubws.py
#  export NCBI_API_KEY=”CLAVE_PUBMED”
#  flask run --host=0.0.0.0
#
# Author: Jaime Hurtado - jaime.hurtado@correounivalle.edu.co
# Fecha: 2021-03-02
#
from flask import Flask, jsonify, request
from metapub import PubMedFetcher

app = Flask(__name__)

#
# Este metodo retorna la cadena 'hello world'
#
@app.route('/')
def helloworld():
    return 'hello world'

#
# Este metodo es invocado de esta forma
#
# curl -X POST -H "Content-type: application/json" -d '{ "id": "2020202" }' http://localhost:5000/title
#
@app.route("/title",methods=['POST'])
def consultametapub():
  fetch = PubMedFetcher()
  if not request.json:
    abort(400)
  pmid = request.json['id']
  article = fetch.article_by_pmid(pmid)
  return jsonify(output=article.title)
