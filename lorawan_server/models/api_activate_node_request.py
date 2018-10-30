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


class ApiActivateNodeRequest(object):
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
        'app_s_key': 'str',
        'dev_addr': 'str',
        'dev_eui': 'str',
        'f_cnt_down': 'int',
        'f_cnt_up': 'int',
        'nwk_s_key': 'str'
    }

    attribute_map = {
        'app_s_key': 'appSKey',
        'dev_addr': 'devAddr',
        'dev_eui': 'devEUI',
        'f_cnt_down': 'fCntDown',
        'f_cnt_up': 'fCntUp',
        'nwk_s_key': 'nwkSKey'
    }

    def __init__(self, app_s_key=None, dev_addr=None, dev_eui=None, f_cnt_down=None, f_cnt_up=None, nwk_s_key=None):  # noqa: E501
        """ApiActivateNodeRequest - a model defined in Swagger"""  # noqa: E501

        self._app_s_key = None
        self._dev_addr = None
        self._dev_eui = None
        self._f_cnt_down = None
        self._f_cnt_up = None
        self._nwk_s_key = None
        self.discriminator = None

        if app_s_key is not None:
            self.app_s_key = app_s_key
        if dev_addr is not None:
            self.dev_addr = dev_addr
        if dev_eui is not None:
            self.dev_eui = dev_eui
        if f_cnt_down is not None:
            self.f_cnt_down = f_cnt_down
        if f_cnt_up is not None:
            self.f_cnt_up = f_cnt_up
        if nwk_s_key is not None:
            self.nwk_s_key = nwk_s_key

    @property
    def app_s_key(self):
        """Gets the app_s_key of this ApiActivateNodeRequest.  # noqa: E501

        Hex encoded AppSKey.  # noqa: E501

        :return: The app_s_key of this ApiActivateNodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._app_s_key

    @app_s_key.setter
    def app_s_key(self, app_s_key):
        """Sets the app_s_key of this ApiActivateNodeRequest.

        Hex encoded AppSKey.  # noqa: E501

        :param app_s_key: The app_s_key of this ApiActivateNodeRequest.  # noqa: E501
        :type: str
        """

        self._app_s_key = app_s_key

    @property
    def dev_addr(self):
        """Gets the dev_addr of this ApiActivateNodeRequest.  # noqa: E501

        Hex encoded DevAddr.  # noqa: E501

        :return: The dev_addr of this ApiActivateNodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._dev_addr

    @dev_addr.setter
    def dev_addr(self, dev_addr):
        """Sets the dev_addr of this ApiActivateNodeRequest.

        Hex encoded DevAddr.  # noqa: E501

        :param dev_addr: The dev_addr of this ApiActivateNodeRequest.  # noqa: E501
        :type: str
        """

        self._dev_addr = dev_addr

    @property
    def dev_eui(self):
        """Gets the dev_eui of this ApiActivateNodeRequest.  # noqa: E501

        Hex encoded DevEUI of the node to activate.  # noqa: E501

        :return: The dev_eui of this ApiActivateNodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._dev_eui

    @dev_eui.setter
    def dev_eui(self, dev_eui):
        """Sets the dev_eui of this ApiActivateNodeRequest.

        Hex encoded DevEUI of the node to activate.  # noqa: E501

        :param dev_eui: The dev_eui of this ApiActivateNodeRequest.  # noqa: E501
        :type: str
        """

        self._dev_eui = dev_eui

    @property
    def f_cnt_down(self):
        """Gets the f_cnt_down of this ApiActivateNodeRequest.  # noqa: E501

        Downlink frame-counter.  # noqa: E501

        :return: The f_cnt_down of this ApiActivateNodeRequest.  # noqa: E501
        :rtype: int
        """
        return self._f_cnt_down

    @f_cnt_down.setter
    def f_cnt_down(self, f_cnt_down):
        """Sets the f_cnt_down of this ApiActivateNodeRequest.

        Downlink frame-counter.  # noqa: E501

        :param f_cnt_down: The f_cnt_down of this ApiActivateNodeRequest.  # noqa: E501
        :type: int
        """

        self._f_cnt_down = f_cnt_down

    @property
    def f_cnt_up(self):
        """Gets the f_cnt_up of this ApiActivateNodeRequest.  # noqa: E501

        Uplink frame-counter.  # noqa: E501

        :return: The f_cnt_up of this ApiActivateNodeRequest.  # noqa: E501
        :rtype: int
        """
        return self._f_cnt_up

    @f_cnt_up.setter
    def f_cnt_up(self, f_cnt_up):
        """Sets the f_cnt_up of this ApiActivateNodeRequest.

        Uplink frame-counter.  # noqa: E501

        :param f_cnt_up: The f_cnt_up of this ApiActivateNodeRequest.  # noqa: E501
        :type: int
        """

        self._f_cnt_up = f_cnt_up

    @property
    def nwk_s_key(self):
        """Gets the nwk_s_key of this ApiActivateNodeRequest.  # noqa: E501

        Hex encoded NwkSKey.  # noqa: E501

        :return: The nwk_s_key of this ApiActivateNodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._nwk_s_key

    @nwk_s_key.setter
    def nwk_s_key(self, nwk_s_key):
        """Sets the nwk_s_key of this ApiActivateNodeRequest.

        Hex encoded NwkSKey.  # noqa: E501

        :param nwk_s_key: The nwk_s_key of this ApiActivateNodeRequest.  # noqa: E501
        :type: str
        """

        self._nwk_s_key = nwk_s_key

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
        if issubclass(ApiActivateNodeRequest, dict):
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
        if not isinstance(other, ApiActivateNodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
