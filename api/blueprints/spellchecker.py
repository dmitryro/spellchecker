#################
#### imports ####
#################
from datetime import datetime
import logging

from flask import Blueprint, Flask, json, jsonify, render_template, request, url_for, make_response
from flask import current_app
from flasgger import Swagger
from flask_api import status    # HTTP Status Codes
from werkzeug.local import LocalProxy
from utils.words import spellcheck, word_found


spell_blueprint = Blueprint('spell', __name__, template_folder='templates')

logger = LocalProxy(lambda: current_app.logger)

@spell_blueprint.route("/spell/<string:word>", methods=['GET'])
def check_spelling(word):
    """
    Retrieve a list of Actions for given profile key
    This endpoint will return all Actions unless a query parameter is specificed
    ---
    tags:
      - Spell
    description: The Spell Checking Endpoint
    definitions:
      Action:
        type: object
        properties:
            word:
              type: string
              description: Word to check
    responses:
      404:
        description: Word is not found
      200:
        description: A list of suggestions and word found status
    """
        
    found, suggestions = spellcheck(word)
    result = {"suggestions":suggestions, "correct": found}

    # Return 200 if word is not suggested (it was found) or suggested and misspeled
    if not suggestions or word_found(word, suggestions):
        response_status = status.HTTP_200_OK
    else:
        response_status = status.HTTP_400_BAD_REQUEST
                   
    return make_response(jsonify(result), response_status)



