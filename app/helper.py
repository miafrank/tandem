import itertools

import requests

from app.config import *
from app.db import get_ingredient_violations_by_diet


def get_recipe_by_name(recipe_name: str):
    resp = requests.get(f'{API_URL}?q={recipe_name}')
    resp.raise_for_status()
    return resp.json()['results']


def get_recipe_by_ingredients(ingredients: list):
    ingredients_query = ','.join(ingredients)
    resp = requests.get(f'{API_URL}/?i={ingredients_query}')
    resp.raise_for_status()
    print(resp.json())
    return resp.json()


# def get_recipe_by_diet(unsafe_ingredient: str):
#     # # todo break this out, needs to be better tested
#     # taco_recipes = get_recipe_by_name(MEAL)
#     # # get list of all ingredients that violate diet
#     # filter_by_diet = list(itertools.chain(*get_ingredient_violations_by_diet(unsafe_ingredient)))
#     # print(taco_recipes)
#     # for taco_recipe in taco_recipes:
#     #     ingredient_list = [ingredient for ingredient in taco_recipe['ingredients'].split(',')]
#     #     for unsafe_ingredient in filter_by_diet:
#     #         if unsafe_ingredient in ingredient_list:
#     #             taco_recipes.remove(taco_recipe)
#     #
#     # # return  if taco_recipes else []
#     # todo break this out, needs to be better tested
#     taco_recipes = get_recipe_by_name(MEAL)
#     # get list of all ingredients that violate diet
#     filter_by_diet = list(itertools.chain(*get_ingredient_violations_by_diet(diet)))
#     print(','.join(filter_by_diet))
#     return [tacos for tacos in taco_recipes if
#             ','.join(*filter_by_diet) not in tacos['ingredients']] if taco_recipes else []
def get_recipe_by_diet(diet: str):
    # todo break this out, needs to be better tested, doesn't work really
    taco_recipes = get_recipe_by_name(MEAL)
    # get list of all ingredients that violate diet
    filter_by_diet = list(itertools.chain(*get_ingredient_violations_by_diet(diet)))
    return [tacos for tacos in taco_recipes if ','.join(filter_by_diet) not in tacos['ingredients']] if taco_recipes else []
