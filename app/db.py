import json
import os
import sqlite3

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')


def load_diets():
    with open('guac_is_extra_data.json') as f:
        diet_dict = json.load(f)
    if diet_dict:
        return diet_dict


def db_connect(db_path=DEFAULT_PATH):
    return sqlite3.connect(db_path)


def create_table():
    diets = load_diets()
    cols = sorted(list(set([col for diet in diets for col in list(diet.keys())])))

    create_statement = f'create table if not exists diets (' \
                       f'{list(cols)[0]} text NOT NULL, ' \
                       f'{list(cols)[1]} text NOT NULL)'
    cursor = db_connect()
    cursor.execute(create_statement)


def insert_diet_data():
    con = db_connect()
    cur = con.cursor()
    table_exists = cur.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()

    if table_exists:
        # load diets from json file and insert into db
        diets = load_diets()
        diet_values = [list(diet.values()) for diet in diets]
        for items in diet_values:
            insert_statement = f'INSERT INTO diets VALUES(?,?)'
            strict = ', '.join(items[1])
            cur.executemany(insert_statement, [(str(items[0]), strict)])
    con.commit()


def get_ingredient_violations_by_diet(diet: str):
    con = db_connect()
    cur = con.cursor()
    filter_statement = f'SELECT ingredient FROM diets WHERE violations LIKE "%{diet}%"'
    return cur.execute(filter_statement).fetchall()