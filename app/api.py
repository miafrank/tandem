from flask import Flask, jsonify, request, make_response
from flask_cors import CORS

from app.helper import *
from app.config import MEAL

app = Flask(__name__)
CORS(app)


@app.route('/tacos', methods=['GET'])
def get_all_tacos():
    params = request.args
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    if 'ingredients' in params:
        ingredients_list = params['ingredients'].split(',')
        return jsonify(tacos=get_recipe_by_ingredients(ingredients_list))
    if 'diet' in params:
        return jsonify(tacos=get_recipe_by_diet(params['diet']))
    return jsonify(tacos=get_recipe_by_name(MEAL))


if __name__ == "__main__":
    app.debug = True
    app.run()
