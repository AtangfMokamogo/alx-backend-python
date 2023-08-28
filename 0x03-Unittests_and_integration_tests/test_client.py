#!/usr/bin/env python3
""" Unit Testing In Python """
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized, parameterized_class
from typing import Dict, Callable
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @patch("client.get_json")
    @patch("client.GithubOrgClient._public_repos_url", new_callable=PropertyMock)
    def test_public_repos(self, mock_repos_url: str, mock_get_json:str):
        """Mocks class properties

        Args:
            mock_repos_url (str): mock url
            mock_get_json (str): mock JSON response
        """
        # Set up the mock data and return values
        mock_repos_url.return_value = "https://api.github.com/holberton/repos"
        mock_get_json.return_value = [
            {"name": "alx-backend_python", "license": {"key": "MIT"}},
            {"name": "alx-backend_javascript", "license": {"key": "Apache"}},
            {"name": "alx-backend", "license": None},
        ]

        # Create an instance of the class and collect resources for test
        org_client = GithubOrgClient("holberton")
        repos = org_client.public_repos(license="MIT")

        # Assert the results and one time calls to callbles and properties
        expected_repos = ["alx-backend_python"]
        self.assertEqual(repos, expected_repos)
        mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "my_license"}}, "my_license", True),
        ({'license': {'key': "other_license"}}, "my_license", False),
    ])
    def test_has_license(
            self,
            repo: Dict,
            key: str,
            expected_result: bool) -> None:
        """mocks class properties

        Args:
            repo (Dict): mock JSON response
            key (str): mock json key
            expected_result (bool): mock results
        """
        client = GithubOrgClient("google")
        mocked_callable = client.has_license(repo, key)
        self.assertEqual(mocked_callable, expected_result)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Intergration Testing in Python """

    @classmethod
    def setUpClass(mock_reponse: Callable):
        """This set up the resorces needed for testing """
        mock_reponse.route_payload = {
            'https://api.github.com/orgs/google': mock_reponse.org_payload,
            'https://api.github.com/orgs/google/repos': mock_reponse.repos_payload,
        }

        def get_json_payload(url: str) -> str:
            """Parses the mock response to JSON

            Args:
                url (str): the url to mock

            Returns:
                str: JSON Response
            """
            if url in mock_reponse.route_payload:
                return mock_reponse.route_payload[url]
            return None

        mock_reponse.get_json_patcher = patch('client.get_json')
        mock_reponse.mock_get_json = mock_reponse.get_json_patcher.start()
        mock_reponse.mock_get_json.side_effect = get_json_payload

    @classmethod
    def tearDownClass(mock_reponse):
        """ Cleans up resources"""
        mock_reponse.get_json_patcher.stop()


if __name__ == '__main__':
    unittest.main()
