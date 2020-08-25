import unittest
from http import HTTPStatus
from unittest import mock

from api import *


class TestApi(unittest.TestCase):

    def _mock_response(self,
                       json_response,
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
        if json_response:
            mock_resp.json = mock.Mock(return_value=json_response)
        return mock_resp

    @mock.patch('requests.get')
    # patch() will clean up your code by replacing the mocked objects with their original counterparts.
    # When you substitute an object in your code, the Mock must look like the real object it is replacing.
    # Otherwise, your code will not be able to use the Mock in place of the original object.
    def test_get_recipe_by_name(self, mock_get):
        expected_response = {'tests': 'meals'}
        mock_response = self._mock_response(json_response=expected_response)
        mock_get.return_value = mock_response

        result = get_recipe_by_name(recipe_name='tests')

        self.assertEqual(result, expected_response)

    @mock.patch('requests.get')
    def test_get_recipe_by_ingredients(self, mock_get):
        expected_response = {'the best': 'meal'}
        mock_response = self._mock_response(json_response=expected_response)
        mock_get.return_value = mock_response

        result = get_recipe_by_ingredients(ingredients=['yummy', 'things'])

        self.assertEqual(result, expected_response)

    @mock.patch('requests.get')
    def test_get_recipe_by_id(self, mock_get):
        expected_response = {'the best': 'meal'}
        mock_response = self._mock_response(json_response=expected_response)
        mock_get.return_value = mock_response

        result = get_recipe_by_id(recipe_id='8080')

        self.assertEqual(result, expected_response)


if __name__ == '__main__':
    unittest.main()
