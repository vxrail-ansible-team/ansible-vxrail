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

class Layer3ManagementNetworkPreviewSpec(object):
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
        'host': 'list[str]'
    }

    attribute_map = {
        'host': 'host'
    }

    def __init__(self, host=None):  # noqa: E501
        """Layer3ManagementNetworkPreviewSpec - a model defined in Swagger"""  # noqa: E501
        self._host = None
        self.discriminator = None
        if host is not None:
            self.host = host

    @property
    def host(self):
        """Gets the host of this Layer3ManagementNetworkPreviewSpec.  # noqa: E501


        :return: The host of this Layer3ManagementNetworkPreviewSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this Layer3ManagementNetworkPreviewSpec.


        :param host: The host of this Layer3ManagementNetworkPreviewSpec.  # noqa: E501
        :type: list[str]
        """

        self._host = host

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
        if issubclass(Layer3ManagementNetworkPreviewSpec, dict):
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
        if not isinstance(other, Layer3ManagementNetworkPreviewSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other