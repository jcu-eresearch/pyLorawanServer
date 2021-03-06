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


class ApiApplicationLink(object):
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
        'application_id': 'str',
        'application_name': 'str',
        'created_at': 'str',
        'is_admin': 'bool',
        'updated_at': 'str'
    }

    attribute_map = {
        'application_id': 'applicationID',
        'application_name': 'applicationName',
        'created_at': 'createdAt',
        'is_admin': 'isAdmin',
        'updated_at': 'updatedAt'
    }

    def __init__(self, application_id=None, application_name=None, created_at=None, is_admin=None, updated_at=None):  # noqa: E501
        """ApiApplicationLink - a model defined in Swagger"""  # noqa: E501

        self._application_id = None
        self._application_name = None
        self._created_at = None
        self._is_admin = None
        self._updated_at = None
        self.discriminator = None

        if application_id is not None:
            self.application_id = application_id
        if application_name is not None:
            self.application_name = application_name
        if created_at is not None:
            self.created_at = created_at
        if is_admin is not None:
            self.is_admin = is_admin
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def application_id(self):
        """Gets the application_id of this ApiApplicationLink.  # noqa: E501


        :return: The application_id of this ApiApplicationLink.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ApiApplicationLink.


        :param application_id: The application_id of this ApiApplicationLink.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def application_name(self):
        """Gets the application_name of this ApiApplicationLink.  # noqa: E501


        :return: The application_name of this ApiApplicationLink.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this ApiApplicationLink.


        :param application_name: The application_name of this ApiApplicationLink.  # noqa: E501
        :type: str
        """

        self._application_name = application_name

    @property
    def created_at(self):
        """Gets the created_at of this ApiApplicationLink.  # noqa: E501


        :return: The created_at of this ApiApplicationLink.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ApiApplicationLink.


        :param created_at: The created_at of this ApiApplicationLink.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def is_admin(self):
        """Gets the is_admin of this ApiApplicationLink.  # noqa: E501


        :return: The is_admin of this ApiApplicationLink.  # noqa: E501
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        """Sets the is_admin of this ApiApplicationLink.


        :param is_admin: The is_admin of this ApiApplicationLink.  # noqa: E501
        :type: bool
        """

        self._is_admin = is_admin

    @property
    def updated_at(self):
        """Gets the updated_at of this ApiApplicationLink.  # noqa: E501


        :return: The updated_at of this ApiApplicationLink.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ApiApplicationLink.


        :param updated_at: The updated_at of this ApiApplicationLink.  # noqa: E501
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
        if issubclass(ApiApplicationLink, dict):
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
        if not isinstance(other, ApiApplicationLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
