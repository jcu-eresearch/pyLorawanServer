# coding: utf-8

"""
    LoRa App Server REST API

     For more information about the usage of the LoRa App Server (REST) API, see [https://docs.loraserver.io/lora-app-server/api/](https://docs.loraserver.io/lora-app-server/api/).   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ApiGetOrganizationResponse(object):
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
        'can_have_gateways': 'bool',
        'created_at': 'str',
        'display_name': 'str',
        'id': 'str',
        'name': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'can_have_gateways': 'canHaveGateways',
        'created_at': 'createdAt',
        'display_name': 'displayName',
        'id': 'id',
        'name': 'name',
        'updated_at': 'updatedAt'
    }

    def __init__(self, can_have_gateways=None, created_at=None, display_name=None, id=None, name=None, updated_at=None):  # noqa: E501
        """ApiGetOrganizationResponse - a model defined in Swagger"""  # noqa: E501

        self._can_have_gateways = None
        self._created_at = None
        self._display_name = None
        self._id = None
        self._name = None
        self._updated_at = None
        self.discriminator = None

        if can_have_gateways is not None:
            self.can_have_gateways = can_have_gateways
        if created_at is not None:
            self.created_at = created_at
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def can_have_gateways(self):
        """Gets the can_have_gateways of this ApiGetOrganizationResponse.  # noqa: E501

        Can the organization create and \"own\" Gateways?  # noqa: E501

        :return: The can_have_gateways of this ApiGetOrganizationResponse.  # noqa: E501
        :rtype: bool
        """
        return self._can_have_gateways

    @can_have_gateways.setter
    def can_have_gateways(self, can_have_gateways):
        """Sets the can_have_gateways of this ApiGetOrganizationResponse.

        Can the organization create and \"own\" Gateways?  # noqa: E501

        :param can_have_gateways: The can_have_gateways of this ApiGetOrganizationResponse.  # noqa: E501
        :type: bool
        """

        self._can_have_gateways = can_have_gateways

    @property
    def created_at(self):
        """Gets the created_at of this ApiGetOrganizationResponse.  # noqa: E501

        When the user was created.  # noqa: E501

        :return: The created_at of this ApiGetOrganizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ApiGetOrganizationResponse.

        When the user was created.  # noqa: E501

        :param created_at: The created_at of this ApiGetOrganizationResponse.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def display_name(self):
        """Gets the display_name of this ApiGetOrganizationResponse.  # noqa: E501

        Organization display name.  # noqa: E501

        :return: The display_name of this ApiGetOrganizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ApiGetOrganizationResponse.

        Organization display name.  # noqa: E501

        :param display_name: The display_name of this ApiGetOrganizationResponse.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this ApiGetOrganizationResponse.  # noqa: E501

        ID of the user.  # noqa: E501

        :return: The id of this ApiGetOrganizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiGetOrganizationResponse.

        ID of the user.  # noqa: E501

        :param id: The id of this ApiGetOrganizationResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ApiGetOrganizationResponse.  # noqa: E501

        Organization name.  # noqa: E501

        :return: The name of this ApiGetOrganizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiGetOrganizationResponse.

        Organization name.  # noqa: E501

        :param name: The name of this ApiGetOrganizationResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def updated_at(self):
        """Gets the updated_at of this ApiGetOrganizationResponse.  # noqa: E501

        When the user was last updated (excludes changes in application access).  # noqa: E501

        :return: The updated_at of this ApiGetOrganizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ApiGetOrganizationResponse.

        When the user was last updated (excludes changes in application access).  # noqa: E501

        :param updated_at: The updated_at of this ApiGetOrganizationResponse.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if issubclass(ApiGetOrganizationResponse, dict):
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
        if not isinstance(other, ApiGetOrganizationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other