import requests
from http import HTTPStatus
from config import *


def get_recipe_by_name(recipe_name: str):
    resp = requests.get(f'{API_URL}?q={recipe_name}')
    resp.raise_for_status()
    return resp.json()['results']


def get_recipe_by_ingredients(recipe_name: str, ingredients: list):
    ingredients_query = ','.join(ingredients)
    resp = requests.get(f'{API_URL}/?i={ingredients_query}&q={recipe_name}')
    resp.raise_for_status()
    return resp.json()['results']


def filter_recipes_by_diet(recipes, filter_by_diet):
    result = []
    if filter_by_diet:
        for tacos in range(len(recipes)):
            ingredient_list = [ele.strip() for ele in recipes[tacos]['ingredients'].split(',')]
            if not any(set(ingredient_list).intersection(set(filter_by_diet))):
                result.append(recipes[tacos])
        return result
    return recipes
