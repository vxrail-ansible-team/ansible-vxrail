# coding: utf-8

"""
    VxRail Disk and Cluster Management

    APIs for disk and cluster management  # noqa: E501

    OpenAPI spec version: 7.0.240
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import vxrail_ansible_utility
from vxrail_ansible_utility.api.expansion_host_api import ExpansionHostApi  # noqa: E501
from vxrail_ansible_utility.rest import ApiException


class TestExpansionHostApi(unittest.TestCase):
    """ExpansionHostApi unit test stubs"""

    def setUp(self):
        self.api = ExpansionHostApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_private_cluster_add_host_post(self):
        """Test case for private_cluster_add_host_post

        Host expansion validation, starts an expansion job based on the provided ExpansionSpec And this endpoint should only be called after validation has passed on  # noqa: E501
        """
        pass

    def test_private_cluster_expansion_preview_get(self):
        """Test case for private_cluster_expansion_preview_get

        Host expansion preview, return domain name.  # noqa: E501
        """
        pass

    def test_private_v1_cluster_expansion_post(self):
        """Test case for private_v1_cluster_expansion_post

        Host expansion, starts an expansion job based on the provided expansion spec  # noqa: E501
        """
        pass

    def test_private_v2_cluster_add_host_post(self):
        """Test case for private_v2_cluster_add_host_post

        Host expansion validation, starts an expansion job based on the provided ExpansionSpec And this endpoint should only be called after validation has passed on  # noqa: E501
        """
        pass

    def test_private_v2_cluster_expansion_validate_post(self):
        """Test case for private_v2_cluster_expansion_validate_post

        Host expansion validation, validate form data for expansion  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()