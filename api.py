import itertools
from pprint import pprint

import requests

from config import *
from db import get_ingredient_violations_by_diet


def get_recipe_by_name(recipe_name: str):
    resp = requests.get(f'{API_URL}?q={recipe_name}')
    resp.raise_for_status()
    return resp.json()


def get_recipe_by_ingredients(ingredients: list):
    ingredients_query = ','.join(ingredients)
    resp = requests.get(f'{API_URL}/?i={ingredients_query}')
    resp.raise_for_status()
    return resp.json()


def get_recipe_by_diet(diet: str):
    taco_recipes = get_recipe_by_name(MEAL)['results']
    # get list of all ingredients that violate diet
    filter_by_diet = list(itertools.chain(*get_ingredient_violations_by_diet(diet)))
    return [tacos
            for tacos in taco_recipes
            if ','.join(filter_by_diet) not in tacos['ingredients']] \
        if taco_recipes \
        else []


pprint(get_recipe_by_diet('halal'))
