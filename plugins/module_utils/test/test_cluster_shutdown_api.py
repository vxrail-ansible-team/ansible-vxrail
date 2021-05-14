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
from vxrail_ansible_utility.api.cluster_shutdown_api import ClusterShutdownApi  # noqa: E501
from vxrail_ansible_utility.rest import ApiException


class TestClusterShutdownApi(unittest.TestCase):
    """ClusterShutdownApi unit test stubs"""

    def setUp(self):
        self.api = ClusterShutdownApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_cluster_shutdown_post(self):
        """Test case for v1_cluster_shutdown_post

        Shuts down a cluster or performs a shutdown dry run.  # noqa: E501
        """
        pass

    def test_v1_requests_id_get(self):
        """Test case for v1_requests_id_get

        Gets the status and progress of cluster shutdown.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
