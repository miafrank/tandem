import requests

from config import *


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
    resp = requests.get(f'{API_URL}/filter.php?c={diet}')
    resp.raise_for_status()
    return resp.json()
