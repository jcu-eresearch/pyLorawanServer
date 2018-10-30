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


class ApiEnqueueDownlinkQueueItemRequest(object):
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
        'confirmed': 'bool',
        'data': 'str',
        'dev_eui': 'str',
        'f_port': 'int',
        'reference': 'str'
    }

    attribute_map = {
        'confirmed': 'confirmed',
        'data': 'data',
        'dev_eui': 'devEUI',
        'f_port': 'fPort',
        'reference': 'reference'
    }

    def __init__(self, confirmed=None, data=None, dev_eui=None, f_port=None, reference=None):  # noqa: E501
        """ApiEnqueueDownlinkQueueItemRequest - a model defined in Swagger"""  # noqa: E501

        self._confirmed = None
        self._data = None
        self._dev_eui = None
        self._f_port = None
        self._reference = None
        self.discriminator = None

        if confirmed is not None:
            self.confirmed = confirmed
        if data is not None:
            self.data = data
        if dev_eui is not None:
            self.dev_eui = dev_eui
        if f_port is not None:
            self.f_port = f_port
        if reference is not None:
            self.reference = reference

    @property
    def confirmed(self):
        """Gets the confirmed of this ApiEnqueueDownlinkQueueItemRequest.  # noqa: E501

        Is an ACK required from the node.  # noqa: E501

        :return: The confirmed of this ApiEnqueueDownlinkQueueItemRequest.  # noqa: E501
        :rtype: bool
        """
        return self._confirmed

    @confirmed.setter
    def confirmed(self, confirmed):
        """Sets the confirmed of this ApiEnqueueDownlinkQueueItemRequest.

        Is an ACK required from the node.  # noqa: E501

        :param confirmed: The confirmed of this ApiEnqueueDownlinkQueueItemRequest.  # noqa: E501
        :type: bool
        """

        self._confirmed = confirmed

    @property
    def data(self):
        """Gets the data of this ApiEnqueueDownlinkQueueItemRequest.  # noqa: E501

        Base64 encoded data.  # noqa: E501

        :return: The data of this ApiEnqueueDownlinkQueueItemRequest.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ApiEnqueueDownlinkQueueItemRequest.

        Base64 encoded data.  # noqa: E501

        :param data: The data of this ApiEnqueueDownlinkQueueItemRequest.  # noqa: E501
        :type: str
        """
        if data is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', data):  # noqa: E501
            raise ValueError("Invalid value for `data`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._data = data

    @property
    def dev_eui(self):
        """Gets the dev_eui of this ApiEnqueueDownlinkQueueItemRequest.  # noqa: E501

        Hex encoded DevEUI of the node.  # noqa: E501

        :return: The dev_eui of this ApiEnqueueDownlinkQueueItemRequest.  # noqa: E501
        :rtype: str
        """
        return self._dev_eui

    @dev_eui.setter
    def dev_eui(self, dev_eui):
        """Sets the dev_eui of this ApiEnqueueDownlinkQueueItemRequest.

        Hex encoded DevEUI of the node.  # noqa: E501

        :param dev_eui: The dev_eui of this ApiEnqueueDownlinkQueueItemRequest.  # noqa: E501
        :type: str
        """

        self._dev_eui = dev_eui

    @property
    def f_port(self):
        """Gets the f_port of this ApiEnqueueDownlinkQueueItemRequest.  # noqa: E501

        FPort used (must be >0)  # noqa: E501

        :return: The f_port of this ApiEnqueueDownlinkQueueItemRequest.  # noqa: E501
        :rtype: int
        """
        return self._f_port

    @f_port.setter
    def f_port(self, f_port):
        """Sets the f_port of this ApiEnqueueDownlinkQueueItemRequest.

        FPort used (must be >0)  # noqa: E501

        :param f_port: The f_port of this ApiEnqueueDownlinkQueueItemRequest.  # noqa: E501
        :type: int
        """

        self._f_port = f_port

    @property
    def reference(self):
        """Gets the reference of this ApiEnqueueDownlinkQueueItemRequest.  # noqa: E501

        Random reference (used on ack notification).  # noqa: E501

        :return: The reference of this ApiEnqueueDownlinkQueueItemRequest.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this ApiEnqueueDownlinkQueueItemRequest.

        Random reference (used on ack notification).  # noqa: E501

        :param reference: The reference of this ApiEnqueueDownlinkQueueItemRequest.  # noqa: E501
        :type: str
        """

        self._reference = reference

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
        if issubclass(ApiEnqueueDownlinkQueueItemRequest, dict):
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
        if not isinstance(other, ApiEnqueueDownlinkQueueItemRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
