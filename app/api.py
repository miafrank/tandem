import itertools
import logging

from flask import Flask, jsonify
from app.utils import *
from app.db import *


app = Flask(__name__)


@app.route('/tacos', methods=['GET'])
def get_all_tacos():
    return jsonify(tacos=get_recipe_by_name(MEAL))


@app.route('/tacos/ingredients/<ingredients>', methods=['GET'])
def search_by_ingredients(ingredients):
    ingredients_list = ingredients.split(',')
    return jsonify(tacos=get_recipe_by_ingredients(ingredients_list)) \
        if ingredients else jsonify(error=HTTPStatus.NOT_ACCEPTABLE)


@app.route('/tacos/diet/<diet>', methods=['GET'])
def search_by_diet(diet):
    taco_recipes = get_recipe_by_name(MEAL)
    filter_by_diet = list(itertools.chain(*get_ingredient_violations_by_diet(diet)))
    return jsonify(tacos=filter_recipes_by_diet(taco_recipes, filter_by_diet)) \
        if diet else jsonify(error=HTTPStatus.NOT_ACCEPTABLE)


if __name__ == "__main__":
    logging.info("Creating table with diet ingredients")
    diet_list = load_diets()
    cols = create_cols_from_diets(diet_list)
    create_table(cols)
    insert_diet_data(diet_list)
    logging.info("Finished creating diet ingredient table")

    app.debug = True
    app.run()
