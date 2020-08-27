import json


def load_diets():
    with open('guac_is_extra.json') as f:
        diet_dict = json.load(f)
    if diet_dict:
        return diet_dict
