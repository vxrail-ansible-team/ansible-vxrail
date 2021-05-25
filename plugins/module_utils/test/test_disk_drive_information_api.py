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
from vxrail_ansible_utility.api.disk_drive_information_api import DiskDriveInformationApi  # noqa: E501
from vxrail_ansible_utility.rest import ApiException


class TestDiskDriveInformationApi(unittest.TestCase):
    """DiskDriveInformationApi unit test stubs"""

    def setUp(self):
        self.api = DiskDriveInformationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_disks_disk_sn_get(self):
        """Test case for v1_disks_disk_sn_get

        Retrieves information about a specific disk.  # noqa: E501
        """
        pass

    def test_v1_disks_get(self):
        """Test case for v1_disks_get

        Retrieves a list of disks and their associated information.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()