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

class ChassisBasicInfo(object):
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
        'id': 'str',
        'psnt': 'str',
        'model': 'str',
        'render_category': 'str',
        'generation': 'int',
        'health': 'str',
        'missing': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'psnt': 'psnt',
        'model': 'model',
        'render_category': 'render_category',
        'generation': 'generation',
        'health': 'health',
        'missing': 'missing'
    }

    def __init__(self, id=None, psnt=None, model=None, render_category=None, generation=None, health=None, missing=None):  # noqa: E501
        """ChassisBasicInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._psnt = None
        self._model = None
        self._render_category = None
        self._generation = None
        self._health = None
        self._missing = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if psnt is not None:
            self.psnt = psnt
        if model is not None:
            self.model = model
        if render_category is not None:
            self.render_category = render_category
        if generation is not None:
            self.generation = generation
        if health is not None:
            self.health = health
        if missing is not None:
            self.missing = missing

    @property
    def id(self):
        """Gets the id of this ChassisBasicInfo.  # noqa: E501

        ID of the chassis  # noqa: E501

        :return: The id of this ChassisBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChassisBasicInfo.

        ID of the chassis  # noqa: E501

        :param id: The id of this ChassisBasicInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def psnt(self):
        """Gets the psnt of this ChassisBasicInfo.  # noqa: E501

        PSNT of the chassis  # noqa: E501

        :return: The psnt of this ChassisBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._psnt

    @psnt.setter
    def psnt(self, psnt):
        """Sets the psnt of this ChassisBasicInfo.

        PSNT of the chassis  # noqa: E501

        :param psnt: The psnt of this ChassisBasicInfo.  # noqa: E501
        :type: str
        """

        self._psnt = psnt

    @property
    def model(self):
        """Gets the model of this ChassisBasicInfo.  # noqa: E501

        Model of the chassis  # noqa: E501

        :return: The model of this ChassisBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ChassisBasicInfo.

        Model of the chassis  # noqa: E501

        :param model: The model of this ChassisBasicInfo.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def render_category(self):
        """Gets the render_category of this ChassisBasicInfo.  # noqa: E501

        The chassis render category  # noqa: E501

        :return: The render_category of this ChassisBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._render_category

    @render_category.setter
    def render_category(self, render_category):
        """Sets the render_category of this ChassisBasicInfo.

        The chassis render category  # noqa: E501

        :param render_category: The render_category of this ChassisBasicInfo.  # noqa: E501
        :type: str
        """

        self._render_category = render_category

    @property
    def generation(self):
        """Gets the generation of this ChassisBasicInfo.  # noqa: E501

        Generation of the chassis  # noqa: E501

        :return: The generation of this ChassisBasicInfo.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this ChassisBasicInfo.

        Generation of the chassis  # noqa: E501

        :param generation: The generation of this ChassisBasicInfo.  # noqa: E501
        :type: int
        """

        self._generation = generation

    @property
    def health(self):
        """Gets the health of this ChassisBasicInfo.  # noqa: E501

        Status of the health of the chassis. Supported values are Critical, Error, Warning, and Healthy.  # noqa: E501

        :return: The health of this ChassisBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this ChassisBasicInfo.

        Status of the health of the chassis. Supported values are Critical, Error, Warning, and Healthy.  # noqa: E501

        :param health: The health of this ChassisBasicInfo.  # noqa: E501
        :type: str
        """

        self._health = health

    @property
    def missing(self):
        """Gets the missing of this ChassisBasicInfo.  # noqa: E501

        Whether the host health status is critical. Supported values are false (not critical) and true (critical).  # noqa: E501

        :return: The missing of this ChassisBasicInfo.  # noqa: E501
        :rtype: bool
        """
        return self._missing

    @missing.setter
    def missing(self, missing):
        """Sets the missing of this ChassisBasicInfo.

        Whether the host health status is critical. Supported values are false (not critical) and true (critical).  # noqa: E501

        :param missing: The missing of this ChassisBasicInfo.  # noqa: E501
        :type: bool
        """

        self._missing = missing

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
        if issubclass(ChassisBasicInfo, dict):
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
        if not isinstance(other, ChassisBasicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
