# coding: utf-8

"""
    VxRail Disk and Cluster Management

    APIs for disk and cluster management  # noqa: E501

    OpenAPI spec version: 7.0.240
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class HostDiskGroupInfoSpec(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'hosts': 'list[HostDGInfoSpec]'
    }

    attribute_map = {
        'hosts': 'hosts'
    }

    def __init__(self, hosts=None):  # noqa: E501
        """HostDiskGroupInfoSpec - a model defined in Swagger"""  # noqa: E501
        self._hosts = None
        self.discriminator = None
        self.hosts = hosts

    @property
    def hosts(self):
        """Gets the hosts of this HostDiskGroupInfoSpec.  # noqa: E501

        Information about the hosts  # noqa: E501

        :return: The hosts of this HostDiskGroupInfoSpec.  # noqa: E501
        :rtype: list[HostDGInfoSpec]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this HostDiskGroupInfoSpec.

        Information about the hosts  # noqa: E501

        :param hosts: The hosts of this HostDiskGroupInfoSpec.  # noqa: E501
        :type: list[HostDGInfoSpec]
        """
        if hosts is None:
            raise ValueError("Invalid value for `hosts`, must not be `None`")  # noqa: E501

        self._hosts = hosts

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(HostDiskGroupInfoSpec, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HostDiskGroupInfoSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
