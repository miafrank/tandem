import requests

from config import *


def get_recipe_by_name(recipe_name: str, url=MEAL_DB_URL):
    resp = requests.get(f'{url}/search.php?s={recipe_name}')
    resp.raise_for_status()
    return resp.json()


def get_recipe_by_ingredients(ingredients: list):
    ingredients_list = ','.join(ingredients)
    resp = requests.get(f'{MEAL_DB_URL}/filter.php?i={ingredients_list}')
    resp.raise_for_status()
    return resp.json()


def get_recipe_by_id(recipe_id: str):
    resp = requests.get(f'{MEAL_DB_URL}/lookup.php?i={recipe_id}')
    resp.raise_for_status()
    return resp.json()
