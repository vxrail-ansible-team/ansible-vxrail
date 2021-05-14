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

class SegmentErrorSpec(object):
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
        'level': 'str',
        'field': 'str',
        'message': 'str'
    }

    attribute_map = {
        'level': 'level',
        'field': 'field',
        'message': 'message'
    }

    def __init__(self, level=None, field=None, message=None):  # noqa: E501
        """SegmentErrorSpec - a model defined in Swagger"""  # noqa: E501
        self._level = None
        self._field = None
        self._message = None
        self.discriminator = None
        self.level = level
        self.field = field
        self.message = message

    @property
    def level(self):
        """Gets the level of this SegmentErrorSpec.  # noqa: E501

        The severity level of the issue  # noqa: E501

        :return: The level of this SegmentErrorSpec.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this SegmentErrorSpec.

        The severity level of the issue  # noqa: E501

        :param level: The level of this SegmentErrorSpec.  # noqa: E501
        :type: str
        """
        if level is None:
            raise ValueError("Invalid value for `level`, must not be `None`")  # noqa: E501
        allowed_values = ["WARNING", "ERROR"]  # noqa: E501
        if level not in allowed_values:
            raise ValueError(
                "Invalid value for `level` ({0}), must be one of {1}"  # noqa: E501
                .format(level, allowed_values)
            )

        self._level = level

    @property
    def field(self):
        """Gets the field of this SegmentErrorSpec.  # noqa: E501

        The category of the issue  # noqa: E501

        :return: The field of this SegmentErrorSpec.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this SegmentErrorSpec.

        The category of the issue  # noqa: E501

        :param field: The field of this SegmentErrorSpec.  # noqa: E501
        :type: str
        """
        if field is None:
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501

        self._field = field

    @property
    def message(self):
        """Gets the message of this SegmentErrorSpec.  # noqa: E501

        The description of the issue  # noqa: E501

        :return: The message of this SegmentErrorSpec.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SegmentErrorSpec.

        The description of the issue  # noqa: E501

        :param message: The message of this SegmentErrorSpec.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

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
        if issubclass(SegmentErrorSpec, dict):
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
        if not isinstance(other, SegmentErrorSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
