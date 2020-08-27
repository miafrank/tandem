from flask import Flask, jsonify, request

from app.helper import *
from app.config import MEAL

app = Flask(__name__)


@app.route('/tacos', methods=['GET'])
def get_all_tacos():
    return jsonify(tacos=get_recipe_by_name(MEAL))


@app.route('/tacos/ingredients/<ingredients>', methods=['GET'])
def search_by_ingredients(ingredients):
    ingredients_list = ingredients.split(',')
    return jsonify(tacos=get_recipe_by_ingredients(ingredients_list))


@app.route('/tacos/diet/<diet>', methods=['GET'])
def search_by_diet(diet):
    taco_recipes = get_recipe_by_name(MEAL)
    filter_by_diet = list(itertools.chain(*get_ingredient_violations_by_diet(diet)))
    return jsonify(tacos=filter_recipes_by_diet(taco_recipes, filter_by_diet))


if __name__ == "__main__":
    app.debug = True
    app.run()
