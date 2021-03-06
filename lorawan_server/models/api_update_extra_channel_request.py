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

from lorawan_server.models.api_modulation import ApiModulation  # noqa: F401,E501


class ApiUpdateExtraChannelRequest(object):
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
        'band_width': 'int',
        'bit_rate': 'int',
        'channel_configuration_id': 'str',
        'frequency': 'int',
        'id': 'str',
        'modulation': 'ApiModulation',
        'spread_factors': 'list[int]'
    }

    attribute_map = {
        'band_width': 'bandWidth',
        'bit_rate': 'bitRate',
        'channel_configuration_id': 'channelConfigurationID',
        'frequency': 'frequency',
        'id': 'id',
        'modulation': 'modulation',
        'spread_factors': 'spreadFactors'
    }

    def __init__(self, band_width=None, bit_rate=None, channel_configuration_id=None, frequency=None, id=None, modulation=None, spread_factors=None):  # noqa: E501
        """ApiUpdateExtraChannelRequest - a model defined in Swagger"""  # noqa: E501

        self._band_width = None
        self._bit_rate = None
        self._channel_configuration_id = None
        self._frequency = None
        self._id = None
        self._modulation = None
        self._spread_factors = None
        self.discriminator = None

        if band_width is not None:
            self.band_width = band_width
        if bit_rate is not None:
            self.bit_rate = bit_rate
        if channel_configuration_id is not None:
            self.channel_configuration_id = channel_configuration_id
        if frequency is not None:
            self.frequency = frequency
        if id is not None:
            self.id = id
        if modulation is not None:
            self.modulation = modulation
        if spread_factors is not None:
            self.spread_factors = spread_factors

    @property
    def band_width(self):
        """Gets the band_width of this ApiUpdateExtraChannelRequest.  # noqa: E501

        Bandwidth.  # noqa: E501

        :return: The band_width of this ApiUpdateExtraChannelRequest.  # noqa: E501
        :rtype: int
        """
        return self._band_width

    @band_width.setter
    def band_width(self, band_width):
        """Sets the band_width of this ApiUpdateExtraChannelRequest.

        Bandwidth.  # noqa: E501

        :param band_width: The band_width of this ApiUpdateExtraChannelRequest.  # noqa: E501
        :type: int
        """

        self._band_width = band_width

    @property
    def bit_rate(self):
        """Gets the bit_rate of this ApiUpdateExtraChannelRequest.  # noqa: E501

        Bit rate (in case of FSK modulation).  # noqa: E501

        :return: The bit_rate of this ApiUpdateExtraChannelRequest.  # noqa: E501
        :rtype: int
        """
        return self._bit_rate

    @bit_rate.setter
    def bit_rate(self, bit_rate):
        """Sets the bit_rate of this ApiUpdateExtraChannelRequest.

        Bit rate (in case of FSK modulation).  # noqa: E501

        :param bit_rate: The bit_rate of this ApiUpdateExtraChannelRequest.  # noqa: E501
        :type: int
        """

        self._bit_rate = bit_rate

    @property
    def channel_configuration_id(self):
        """Gets the channel_configuration_id of this ApiUpdateExtraChannelRequest.  # noqa: E501

        ID of the channel-configuration.  # noqa: E501

        :return: The channel_configuration_id of this ApiUpdateExtraChannelRequest.  # noqa: E501
        :rtype: str
        """
        return self._channel_configuration_id

    @channel_configuration_id.setter
    def channel_configuration_id(self, channel_configuration_id):
        """Sets the channel_configuration_id of this ApiUpdateExtraChannelRequest.

        ID of the channel-configuration.  # noqa: E501

        :param channel_configuration_id: The channel_configuration_id of this ApiUpdateExtraChannelRequest.  # noqa: E501
        :type: str
        """

        self._channel_configuration_id = channel_configuration_id

    @property
    def frequency(self):
        """Gets the frequency of this ApiUpdateExtraChannelRequest.  # noqa: E501

        Frequency.  # noqa: E501

        :return: The frequency of this ApiUpdateExtraChannelRequest.  # noqa: E501
        :rtype: int
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this ApiUpdateExtraChannelRequest.

        Frequency.  # noqa: E501

        :param frequency: The frequency of this ApiUpdateExtraChannelRequest.  # noqa: E501
        :type: int
        """

        self._frequency = frequency

    @property
    def id(self):
        """Gets the id of this ApiUpdateExtraChannelRequest.  # noqa: E501

        ID of the extra channel.  # noqa: E501

        :return: The id of this ApiUpdateExtraChannelRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiUpdateExtraChannelRequest.

        ID of the extra channel.  # noqa: E501

        :param id: The id of this ApiUpdateExtraChannelRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def modulation(self):
        """Gets the modulation of this ApiUpdateExtraChannelRequest.  # noqa: E501

        Modulation.  # noqa: E501

        :return: The modulation of this ApiUpdateExtraChannelRequest.  # noqa: E501
        :rtype: ApiModulation
        """
        return self._modulation

    @modulation.setter
    def modulation(self, modulation):
        """Sets the modulation of this ApiUpdateExtraChannelRequest.

        Modulation.  # noqa: E501

        :param modulation: The modulation of this ApiUpdateExtraChannelRequest.  # noqa: E501
        :type: ApiModulation
        """

        self._modulation = modulation

    @property
    def spread_factors(self):
        """Gets the spread_factors of this ApiUpdateExtraChannelRequest.  # noqa: E501

        Spread-factors (in case of LoRa modulation).  # noqa: E501

        :return: The spread_factors of this ApiUpdateExtraChannelRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._spread_factors

    @spread_factors.setter
    def spread_factors(self, spread_factors):
        """Sets the spread_factors of this ApiUpdateExtraChannelRequest.

        Spread-factors (in case of LoRa modulation).  # noqa: E501

        :param spread_factors: The spread_factors of this ApiUpdateExtraChannelRequest.  # noqa: E501
        :type: list[int]
        """

        self._spread_factors = spread_factors

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
        if issubclass(ApiUpdateExtraChannelRequest, dict):
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
        if not isinstance(other, ApiUpdateExtraChannelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
