import requests
from http import HTTPStatus
from config import *


def get_recipe_by_name(recipe_name: str):
    resp = requests.get(f'{API_URL}?q={recipe_name}')
    resp.raise_for_status()
    return resp.json()['results']


def get_recipe_by_ingredients(ingredients: list):
    ingredients_query = ','.join(ingredients)
    resp = requests.get(f'{API_URL}/?i={ingredients_query}')
    resp.raise_for_status()
    return resp.json()['results']


def filter_recipes_by_diet(taco_recipes, filter_by_diet):
    result = []
    if filter_by_diet:
        for tacos in range(len(taco_recipes)):
            ingredient_list = [ele.strip() for ele in taco_recipes[tacos]['ingredients'].split(',')]
            if not any(set(ingredient_list).intersection(set(filter_by_diet))):
                result.append(taco_recipes[tacos])
        return result
    return taco_recipes
