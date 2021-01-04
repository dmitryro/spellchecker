from flask import Blueprint, jsonify, make_response, request
from flask_api import status    # HTTP Status Codes
from utils.words import spellcheck, word_found, in_legitimate_format


spell_blueprint = Blueprint('spell', __name__, template_folder='templates')


@spell_blueprint.route("/")
def index():
    """ Home Page """
    return make_response(jsonify(name='Spellchecker REST API Service',
                                 version='1.0',
                                 docs=request.base_url + 'apidocs/index.html'), 
                         status.HTTP_200_OK)


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
    correct, suggestions = spellcheck(word)

    # Check if the word is capital case or all upper case but still found
    if word_found(word, suggestions) and in_legitimate_format(word):
        suggestions = []
    if not suggestions and not correct:
        response_status = status.HTTP_404_NOT_FOUND
    else:
        response_status = status.HTTP_200_OK

    result = {"suggestions": suggestions, "correct": correct}
    return make_response(jsonify(result), response_status)
