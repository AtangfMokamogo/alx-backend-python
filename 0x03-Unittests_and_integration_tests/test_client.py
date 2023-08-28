#!/usr/bin/env python3
""" Unit Testing In Python """
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized
from typing import Dict
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit Testing With Magic Mock"""

    @parameterized.expand([
        ("google", {'Personal-Access-Token': "holberton-1"}),
        ("abc", {'Personal_Access_Token': "alx-se"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(
            self,
            org: str,
            mock_response: Dict,
            mocked_callable: MagicMock):
        """Mocks a request to an API

        Args:
            org (str): mock API request url
            mock_response (Dict): mock response
            mocked_callable (MagicMock): mocked method
        """

        # Arrange the required resources
        git_client = GithubOrgClient(org)
        mocked_callable.return_value = MagicMock(return_value=mock_response)

        # Assert The Results
        self.assertEqual(git_client.org(), mock_response)

        # Verify the method was called once
        mocked_callable.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mockable_cls_field: str):
        """Mock Testing a class field

        Args:
            mockable_cls_field (str): the field to mock
        """
        mock_url = {"repos_url": "https://api.github.com/orgs/holberton"}
        mockable_cls_field.return_value = mock_url

        client = GithubOrgClient("holberton")
        result = client._public_repos_url

        self.assertEqual(result, mock_url["repos_url"])

if __name__ == '__main__':
    unittest.main()
