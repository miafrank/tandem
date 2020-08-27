from unittest.mock import MagicMock, Mock
import unittest
from unittest import mock
from sqlite3 import Cursor
from app.db import *


class TestDB(unittest.TestCase):

    def _mock_db(self, execute_statement=None, table_return_value=None):
        mock_db = mock.Mock()
        mock_db.connect = "connected successfully"
        mock_db.path = "fake path"
        mock_db.execute = "executed query"
        if execute_statement:
            mock_db.execute = execute_statement
        return mock_db

    @mock.patch('sqlite3.connect')
    def test_sql_connect(self, mock_sql):
        mock_sql.connect.return_value = "connected successfully"
        db_connect()
        self.assertTrue(mock_sql.called)

    def test_create_cols_from_diets(self):
        diet_cols = [{'violations': ''}, {'ingredient': ''}]
        expected = ['ingredient', 'violations']
        result = create_cols_from_diets(diet_cols)
        self.assertEqual(expected, result)

    @mock.patch('sqlite3.connect')
    def test_create_table(self, mock_sql):
        mock_sql.execute.return_value = ['da truth', 'the truth']
        mock_cols = [{'the truth': 'is out there'},
                     {'da truth': 'is out there, seriously'}]

        create_table(mock_cols)
        self.assertTrue(mock_sql.called)

    @mock.patch('sqlite3.connect')
    def test_insert_diet_data(self, mock_sql):
        mock_sql.executemany.return_value = ['some', 'values']
        mock_sql.commit.return_value = 'inserted successfully'

        diets = [{'ingredient': 'chicken', 'violations': ['vegetarian', 'vegan']}]

        insert_diet_data(diets)

        self.assertTrue(mock_sql.called)

    @mock.patch('sqlite3.connect')
    def test_get_ingredient_violations_by_diet(self, mock_sql):
        mock_sql.return_value.execute = ['some', 'violations']
        diet = 'no sugar'
        get_ingredient_violations_by_diet(diet)
        self.assertTrue(mock_sql.called)