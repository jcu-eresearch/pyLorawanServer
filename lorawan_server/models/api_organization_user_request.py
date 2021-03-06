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


class ApiOrganizationUserRequest(object):
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
        'is_admin': 'bool',
        'user_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'is_admin': 'isAdmin',
        'user_id': 'userID'
    }

    def __init__(self, id=None, is_admin=None, user_id=None):  # noqa: E501
        """ApiOrganizationUserRequest - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._is_admin = None
        self._user_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if is_admin is not None:
            self.is_admin = is_admin
        if user_id is not None:
            self.user_id = user_id

    @property
    def id(self):
        """Gets the id of this ApiOrganizationUserRequest.  # noqa: E501

        The organization id.  # noqa: E501

        :return: The id of this ApiOrganizationUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiOrganizationUserRequest.

        The organization id.  # noqa: E501

        :param id: The id of this ApiOrganizationUserRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_admin(self):
        """Gets the is_admin of this ApiOrganizationUserRequest.  # noqa: E501

        The user's admin status for the organization  # noqa: E501

        :return: The is_admin of this ApiOrganizationUserRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        """Sets the is_admin of this ApiOrganizationUserRequest.

        The user's admin status for the organization  # noqa: E501

        :param is_admin: The is_admin of this ApiOrganizationUserRequest.  # noqa: E501
        :type: bool
        """

        self._is_admin = is_admin

    @property
    def user_id(self):
        """Gets the user_id of this ApiOrganizationUserRequest.  # noqa: E501

        The user's id.  # noqa: E501

        :return: The user_id of this ApiOrganizationUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ApiOrganizationUserRequest.

        The user's id.  # noqa: E501

        :param user_id: The user_id of this ApiOrganizationUserRequest.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

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
        if issubclass(ApiOrganizationUserRequest, dict):
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
        if not isinstance(other, ApiOrganizationUserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
