# coding: utf-8

"""
    OpenDota API

    # Introduction The OpenDota API provides Dota 2 related data including advanced match data extracted from match replays. Please keep request rate to approximately 1/s.  **Begining 4/22/2018, the OpenDota API will be limited to 50,000 free calls per month.** We'll be offering a Premium Tier with unlimited API calls and higher rate limits. Check out the [API page](https://www.opendota.com/api-keys) to learn more. 

    OpenAPI spec version: 17.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import od_python
from od_python.rest import ApiException
from od_python.apis.scenarios_api import ScenariosApi


class TestScenariosApi(unittest.TestCase):
    """ ScenariosApi unit test stubs """

    def setUp(self):
        self.api = od_python.apis.scenarios_api.ScenariosApi()

    def tearDown(self):
        pass

    def test_scenarios_item_timings_get(self):
        """
        Test case for scenarios_item_timings_get

        GET /scenarios/itemTimings
        """
        pass

    def test_scenarios_lane_roles_get(self):
        """
        Test case for scenarios_lane_roles_get

        GET /scenarios/laneRoles
        """
        pass

    def test_scenarios_misc_get(self):
        """
        Test case for scenarios_misc_get

        GET /scenarios/misc
        """
        pass


if __name__ == '__main__':
    unittest.main()