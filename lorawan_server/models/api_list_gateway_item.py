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


class ApiListGatewayItem(object):
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
        'created_at': 'str',
        'description': 'str',
        'mac': 'str',
        'name': 'str',
        'organization_id': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'description': 'description',
        'mac': 'mac',
        'name': 'name',
        'organization_id': 'organizationID',
        'updated_at': 'updatedAt'
    }

    def __init__(self, created_at=None, description=None, mac=None, name=None, organization_id=None, updated_at=None):  # noqa: E501
        """ApiListGatewayItem - a model defined in Swagger"""  # noqa: E501

        self._created_at = None
        self._description = None
        self._mac = None
        self._name = None
        self._organization_id = None
        self._updated_at = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if mac is not None:
            self.mac = mac
        if name is not None:
            self.name = name
        if organization_id is not None:
            self.organization_id = organization_id
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this ApiListGatewayItem.  # noqa: E501

        Creation timestamp of the record  # noqa: E501

        :return: The created_at of this ApiListGatewayItem.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ApiListGatewayItem.

        Creation timestamp of the record  # noqa: E501

        :param created_at: The created_at of this ApiListGatewayItem.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this ApiListGatewayItem.  # noqa: E501

        A description for the gateway  # noqa: E501

        :return: The description of this ApiListGatewayItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiListGatewayItem.

        A description for the gateway  # noqa: E501

        :param description: The description of this ApiListGatewayItem.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def mac(self):
        """Gets the mac of this ApiListGatewayItem.  # noqa: E501

        Hex encoded mac address.  # noqa: E501

        :return: The mac of this ApiListGatewayItem.  # noqa: E501
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this ApiListGatewayItem.

        Hex encoded mac address.  # noqa: E501

        :param mac: The mac of this ApiListGatewayItem.  # noqa: E501
        :type: str
        """

        self._mac = mac

    @property
    def name(self):
        """Gets the name of this ApiListGatewayItem.  # noqa: E501

        A name for the gateway  # noqa: E501

        :return: The name of this ApiListGatewayItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiListGatewayItem.

        A name for the gateway  # noqa: E501

        :param name: The name of this ApiListGatewayItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def organization_id(self):
        """Gets the organization_id of this ApiListGatewayItem.  # noqa: E501

        ID of the organization to which this gateway belongs.  # noqa: E501

        :return: The organization_id of this ApiListGatewayItem.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this ApiListGatewayItem.

        ID of the organization to which this gateway belongs.  # noqa: E501

        :param organization_id: The organization_id of this ApiListGatewayItem.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def updated_at(self):
        """Gets the updated_at of this ApiListGatewayItem.  # noqa: E501

        Last update timestamp of the record  # noqa: E501

        :return: The updated_at of this ApiListGatewayItem.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ApiListGatewayItem.

        Last update timestamp of the record  # noqa: E501

        :param updated_at: The updated_at of this ApiListGatewayItem.  # noqa: E501
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
        if issubclass(ApiListGatewayItem, dict):
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
        if not isinstance(other, ApiListGatewayItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
