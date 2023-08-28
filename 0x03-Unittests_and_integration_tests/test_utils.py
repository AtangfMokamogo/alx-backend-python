#!/usr/bin/env python3
""" Unit testing in Python """
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


class TestAccessNestedMap(unittest.TestCase):
    """ This is implements the test cases for the utils.py module

    Args:
        unittest (callable): base unittest Test class
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            result_exp: Any):
        """ Tests if the fuction correctly returns the nested
            maps as requested

        Args:
            nested_map (Mapping): the nested dictionary
            path (Sequence): the list of keys to map to in the dictionary @nested_map
            result_exp (Any): the values stored in nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), result_exp)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping,
            path: Sequence,
            exception_exp: Any):
        """ This tests calling the method with an exception

        Args:
            nested_map (Mapping): the dictionary of keys to map
            path (Sequence): the keys to extract the mapped values from
            exception_exp (Any): the expected output of the function
                                        (an exception string in this case)
        """
        with self.assertRaises(exception_exp) as context:
            access_nested_map(nested_map, path)
        if exception_exp is KeyError:
            self.assertEqual(str(context.exception), "'{}'".format(path[-1]))


class TestGetJson(unittest.TestCase):
    """Unit testing with mock and patch """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(
            self,
            test_url: str,
            mock_payload: Mapping,
            mock_get: Dict):
        """Tests a request with a mock object

        Args:
            test_url (str): the url to send the request to
            mock_payload (Mapping): the request payload
            mock_get (Dict): the response object as a dictionary
        """
        # Create an Instance of the Mock class to mock
        mocked_response = Mock()

        mocked_response.json.return_value = mock_payload
        mock_get.return_value = mocked_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, mock_payload)


class TestMemoize(unittest.TestCase):
    """Unit Testing With Memoisation"""

    class TestClass:
        """ A Test Class"""

        def a_method(self):
            """ Return Testing Value """
            return 42

        @memoize
        def a_property(self):
            """ Cache The Returns"""
            return self.a_method()

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mocked_callable: Callable):
        """ Mocks a method while implementing memoise

        Args:
            mocked_callable (Callable): the method to mock
        """
        test_case = self.TestClass()

        mocked_callable.return_value = 42

        test_1 = test_case.a_property
        test_2 = test_case.a_property

        # Assert that the callable was indeed called once
        mocked_callable.assert_called_once()

        # Assert the results
        self.assertEqual(test_1, 42)
        self.assertEqual(test_2, 42)


if __name__ == '__main__':
    unittest.main()
