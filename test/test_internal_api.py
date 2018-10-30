# coding: utf-8

"""
    LoRa App Server REST API

     For more information about the usage of the LoRa App Server (REST) API, see [https://docs.loraserver.io/lora-app-server/api/](https://docs.loraserver.io/lora-app-server/api/).   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import lorawan_server
from lorawan_server.api.internal_api import InternalApi  # noqa: E501
from lorawan_server.rest import ApiException


class TestInternalApi(unittest.TestCase):
    """InternalApi unit test stubs"""

    def setUp(self):
        self.api = lorawan_server.api.internal_api.InternalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_branding(self):
        """Test case for branding

        Get the branding for the UI  # noqa: E501
        """
        pass

    def test_login(self):
        """Test case for login

        Log in a user  # noqa: E501
        """
        pass

    def test_profile(self):
        """Test case for profile

        Get the current user's profile  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()