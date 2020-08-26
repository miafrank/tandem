import requests

from config import *


def get_recipe_by_name(recipe_name: str):
    resp = requests.get(f'{MEAL_DB_URL}/search.php?s={recipe_name}')
    resp.raise_for_status()
    return resp.json()


def get_recipe_by_ingredients(ingredients: list):
    ingredients_query = ','.join(ingredients)
    resp = requests.get(f'{MEAL_DB_URL}/filter.php?i={ingredients_query}')
    resp.raise_for_status()
    return resp.json()


def get_recipe_by_id(recipe_id: str):
    resp = requests.get(f'{MEAL_DB_URL}/lookup.php?i={recipe_id}')
    resp.raise_for_status()
    return resp.json()


def get_recipe_by_diet(diet: str):
    resp = requests.get(f'{MEAL_DB_URL}/filter.php?c={diet}')
    resp.raise_for_status()
    return resp.json()


def get_random_recipes():
    resp = requests.get(f'{MEAL_DB_URL}/randomselection.php')
    resp.raise_for_status()
    return resp.json()
