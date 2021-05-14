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

class ClusterMigrationTargetVcSpec(object):
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
        'admin_account': 'Account',
        'management_account': 'Account',
        'hostname': 'str',
        'ip': 'str'
    }

    attribute_map = {
        'admin_account': 'admin_account',
        'management_account': 'management_account',
        'hostname': 'hostname',
        'ip': 'ip'
    }

    def __init__(self, admin_account=None, management_account=None, hostname=None, ip=None):  # noqa: E501
        """ClusterMigrationTargetVcSpec - a model defined in Swagger"""  # noqa: E501
        self._admin_account = None
        self._management_account = None
        self._hostname = None
        self._ip = None
        self.discriminator = None
        self.admin_account = admin_account
        self.management_account = management_account
        self.hostname = hostname
        self.ip = ip

    @property
    def admin_account(self):
        """Gets the admin_account of this ClusterMigrationTargetVcSpec.  # noqa: E501


        :return: The admin_account of this ClusterMigrationTargetVcSpec.  # noqa: E501
        :rtype: Account
        """
        return self._admin_account

    @admin_account.setter
    def admin_account(self, admin_account):
        """Sets the admin_account of this ClusterMigrationTargetVcSpec.


        :param admin_account: The admin_account of this ClusterMigrationTargetVcSpec.  # noqa: E501
        :type: Account
        """
        if admin_account is None:
            raise ValueError("Invalid value for `admin_account`, must not be `None`")  # noqa: E501

        self._admin_account = admin_account

    @property
    def management_account(self):
        """Gets the management_account of this ClusterMigrationTargetVcSpec.  # noqa: E501


        :return: The management_account of this ClusterMigrationTargetVcSpec.  # noqa: E501
        :rtype: Account
        """
        return self._management_account

    @management_account.setter
    def management_account(self, management_account):
        """Sets the management_account of this ClusterMigrationTargetVcSpec.


        :param management_account: The management_account of this ClusterMigrationTargetVcSpec.  # noqa: E501
        :type: Account
        """
        if management_account is None:
            raise ValueError("Invalid value for `management_account`, must not be `None`")  # noqa: E501

        self._management_account = management_account

    @property
    def hostname(self):
        """Gets the hostname of this ClusterMigrationTargetVcSpec.  # noqa: E501


        :return: The hostname of this ClusterMigrationTargetVcSpec.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this ClusterMigrationTargetVcSpec.


        :param hostname: The hostname of this ClusterMigrationTargetVcSpec.  # noqa: E501
        :type: str
        """
        if hostname is None:
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501

        self._hostname = hostname

    @property
    def ip(self):
        """Gets the ip of this ClusterMigrationTargetVcSpec.  # noqa: E501


        :return: The ip of this ClusterMigrationTargetVcSpec.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ClusterMigrationTargetVcSpec.


        :param ip: The ip of this ClusterMigrationTargetVcSpec.  # noqa: E501
        :type: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

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
        if issubclass(ClusterMigrationTargetVcSpec, dict):
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
        if not isinstance(other, ClusterMigrationTargetVcSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
