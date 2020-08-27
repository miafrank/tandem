import unittest
from unittest import mock

from utils import *


class TestApi(unittest.TestCase):

    def _mock_response(self,
                       json,
                       status=HTTPStatus.OK,
                       raise_for_status=None):
        """
        helper function for creating mock requests/responses
        """
        mock_resp = mock.Mock()
        # mock raise_for_status call w/optional error
        mock_resp.raise_for_status = mock.Mock()
        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status
        # set status code
        mock_resp.status_code = status
        # include mock json response in Mock() return value
        if json:
            mock_resp.json = mock.Mock(return_value=json)
        return mock_resp

    @mock.patch('requests.get')
    # patch() will clean up your code by replacing the mocked objects with their original counterparts.
    # when you substitute an object in your code, the Mock must look like the real object it is replacing.
    # otherwise, your code will not be able to use the Mock in place of the original object.
    def test_get_recipe_by_name(self, mock_get):
        expected_response = [{'the best': 'meal'}]
        mock_response = self._mock_response(json={'results': [{'the best': 'meal'}]})
        mock_get.return_value = mock_response

        result = get_recipe_by_name(recipe_name='a cool one')

        self.assertEqual(expected_response, result)

    @mock.patch('requests.get')
    def test_get_recipe_by_ingredients(self, mock_get):
        expected_response = [{'the best': 'meal'}]
        mock_response = self._mock_response(json={'results': [{'the best': 'meal'}]})
        mock_get.return_value = mock_response

        result = get_recipe_by_ingredients(ingredients=['yummy', 'things'])

        self.assertEqual(expected_response, result)

    def test_get_recipes_by_diet_vegetarian(self):
        chicken_taco_recipe = [
            {
                "href": "http://www.recipezaar.com/Chicken-Tacos-the-Tahiti-Way-94613",
                "ingredients": "black pepper, chicken, cilantro, corn tortillas, garlic, onions, pepperoncini pepper",
                "thumbnail": "",
                "title": "Chicken Tacos - the Tahiti Way"
            },
        ]
        vegetarian_violations = ['chicken', 'beef', 'steak', 'pork', 'tuna']

        expected = []

        result = filter_recipes_by_diet(chicken_taco_recipe, vegetarian_violations)
        self.assertEqual(result, expected)

    def test_get_recipes_by_diet_no_diet(self):
        chicken_taco_recipe = [
            {
                "href": "http://www.recipezaar.com/Chicken-Tacos-the-Tahiti-Way-94613",
                "ingredients": "black pepper, chicken, cilantro, corn tortillas, garlic, onions, pepperoncini "
                               "pepper",
                "thumbnail": "",
                "title": "Chicken Tacos - the Tahiti Way"
            },
        ]
        vegetarian_violations = []

        expected = chicken_taco_recipe

        result = filter_recipes_by_diet(chicken_taco_recipe, vegetarian_violations)
        self.assertEqual(expected, result)

    def test_get_recipes_by_diet_no_peanut_allergy(self):
        peanut_recipe = [
            {
                "href": "http://www.epicurious.com/recipes/food/views/Chocolate-Cups-with-Ice-Cream-and-Peanuts-108905",
                "ingredients": "peanuts, semisweet chocolate, ice cream, vegetable oil",
                "thumbnail": "http://img.recipepuppy.com/132916.jpg",
                "title": "Chocolate Cups with Ice Cream and Peanuts"
            }
        ]
        vegetarian_violations = ['peanuts']

        expected = []

        result = filter_recipes_by_diet(peanut_recipe, vegetarian_violations)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
