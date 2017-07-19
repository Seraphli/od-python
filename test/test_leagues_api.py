# coding: utf-8

"""
    OpenDota API

    # Introduction This API provides Dota 2 related data. Please keep request rate to approximately 3/s. 

    OpenAPI spec version: 15.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import od_python
from od_python.rest import ApiException
from od_python.apis.leagues_api import LeaguesApi


class TestLeaguesApi(unittest.TestCase):
    """ LeaguesApi unit test stubs """

    def setUp(self):
        self.api = od_python.apis.leagues_api.LeaguesApi()

    def tearDown(self):
        pass

    def test_leagues_get(self):
        """
        Test case for leagues_get

        GET /leagues
        """
        pass


if __name__ == '__main__':
    unittest.main()