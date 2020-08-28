import itertools
import logging
from http import HTTPStatus

from flask import Flask, jsonify

from db import *
from diets import load_diets
from utils import *

app = Flask(__name__)
app.logger.setLevel(level=logging.INFO)


@app.route('/recipes/<name>', methods=['GET'])
def view_recipes_by_name(name):
    return jsonify(tacos=get_recipe_by_name(name))


@app.route('/recipes/<name>/ingredients/<ingredients>', methods=['GET'])
def search_by_ingredients(name, ingredients):
    ingredients_list = ingredients.split(',')
    return jsonify(tacos=get_recipe_by_ingredients(name, ingredients_list)) \
        if ingredients else jsonify(error=HTTPStatus.NOT_ACCEPTABLE)


@app.route('/recipes/<name>/diet/<diet>', methods=['GET'])
def search_by_diet(name, diet):
    recipes = get_recipe_by_name(name)
    filter_by_diet = list(itertools.chain(*get_ingredient_violations_by_diet(diet)))
    return jsonify(tacos=filter_recipes_by_diet(recipes, filter_by_diet)) \
        if diet else jsonify(error=HTTPStatus.NOT_ACCEPTABLE)


if __name__ == "__main__":
    app.logger.info("Creating table with diet ingredients")
    diet_list = load_diets()
    cols = create_cols_from_diets(diet_list)
    create_table(cols)
    insert_diet_data(diet_list)
    app.logger.info("Finished creating diet ingredient table")

    app.debug = True
    app.run()
