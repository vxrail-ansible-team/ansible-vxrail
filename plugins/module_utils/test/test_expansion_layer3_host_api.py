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
from vxrail_ansible_utility.api.expansion_layer3_host_api import ExpansionLayer3HostApi  # noqa: E501
from vxrail_ansible_utility.rest import ApiException


class TestExpansionLayer3HostApi(unittest.TestCase):
    """ExpansionLayer3HostApi unit test stubs"""

    def setUp(self):
        self.api = ExpansionLayer3HostApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_private_cluster_layer3_add_host_post(self):
        """Test case for private_cluster_layer3_add_host_post

        Start a cluster expansion job based on the provided specs  # noqa: E501
        """
        pass

    def test_private_cluster_layer3_add_proxy_post(self):
        """Test case for private_cluster_layer3_add_proxy_post

        Add a proxy node to the VxRail cluster. The proxy node represents a L3 segment.  # noqa: E501
        """
        pass

    def test_private_cluster_layer3_network_topology_get(self):
        """Test case for private_cluster_layer3_network_topology_get

        Get the network type (DIFF_SUBNET, SAME_SUBNET or UNDECIDED) for different traffics (management, vSAN, vMotion).  # noqa: E501
        """
        pass

    def test_private_cluster_layer3_network_topology_put(self):
        """Test case for private_cluster_layer3_network_topology_put

        Change the network type (DIFF_SUBNET, SAME_SUBNET or UNDECIDED) for different traffics (management, vSAN, vMotion).  # noqa: E501
        """
        pass

    def test_private_cluster_layer3_proxy_node_segment_label_network_get(self):
        """Test case for private_cluster_layer3_proxy_node_segment_label_network_get

        Get network info of an unconfigured host by ip, insist of netmask, vlanId, gateway and network type topology.  # noqa: E501
        """
        pass

    def test_private_cluster_layer3_segment_label_post(self):
        """Test case for private_cluster_layer3_segment_label_post

        Generate a default segment label for the newly added segment.  # noqa: E501
        """
        pass

    def test_private_cluster_layer3_segments_get(self):
        """Test case for private_cluster_layer3_segments_get

        Get a list of Layer 3 segments that are recognized by VxRail Manager. This information is from VxM DB.  # noqa: E501
        """
        pass

    def test_private_cluster_layer3_segments_initial_segment_get(self):
        """Test case for private_cluster_layer3_segments_initial_segment_get

        Information about if initial segment information is needed.  # noqa: E501
        """
        pass

    def test_private_cluster_layer3_segments_initial_segment_post(self):
        """Test case for private_cluster_layer3_segments_initial_segment_post

        Provide netmask and gateway for vSAN and vMotion traffic of segment one.  # noqa: E501
        """
        pass

    def test_private_cluster_layer3_segments_segment_label_available_hosts_get(self):
        """Test case for private_cluster_layer3_segments_segment_label_available_hosts_get

        Get a list of unconfigured hosts from a specific L3 segment.  # noqa: E501
        """
        pass

    def test_private_cluster_layer3_segments_segment_label_network_get(self):
        """Test case for private_cluster_layer3_segments_segment_label_network_get

        Get the existing network configutration for selected L3 segment. Network information like ip pools, subnet mask, gateway, etc. will be given for different traffic types.  # noqa: E501
        """
        pass

    def test_private_cluster_layer3_segments_segment_label_network_management_post(self):
        """Test case for private_cluster_layer3_segments_segment_label_network_management_post

        Provide network information for management network of the new L3 segment  # noqa: E501
        """
        pass

    def test_private_cluster_layer3_segments_segment_label_network_management_preview_post(self):
        """Test case for private_cluster_layer3_segments_segment_label_network_management_preview_post

        Provide management network information for preview.  # noqa: E501
        """
        pass

    def test_private_cluster_layer3_segments_segment_label_network_vsan_vmotion_preview_post(self):
        """Test case for private_cluster_layer3_segments_segment_label_network_vsan_vmotion_preview_post

        Provide vsan/vmotion network information for preview.  # noqa: E501
        """
        pass

    def test_private_cluster_layer3_segments_segment_label_put(self):
        """Test case for private_cluster_layer3_segments_segment_label_put

        Change the segment label for the current segment.  # noqa: E501
        """
        pass

    def test_private_cluster_layer3_validate_post(self):
        """Test case for private_cluster_layer3_validate_post

        Validate data for Layer 3 cluster expansion  # noqa: E501
        """
        pass

    def test_private_v2_cluster_layer3_add_host_post(self):
        """Test case for private_v2_cluster_layer3_add_host_post

        Start a cluster expansion job based on the provided specs to support two vds  # noqa: E501
        """
        pass

    def test_private_v2_cluster_layer3_validate_post(self):
        """Test case for private_v2_cluster_layer3_validate_post

        Validate data for Layer 3 cluster expansion  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()