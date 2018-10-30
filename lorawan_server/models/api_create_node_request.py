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

from lorawan_server.models.api_rx_window import ApiRXWindow  # noqa: F401,E501


class ApiCreateNodeRequest(object):
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
        'adr_interval': 'int',
        'app_eui': 'str',
        'app_key': 'str',
        'application_id': 'str',
        'description': 'str',
        'dev_eui': 'str',
        'installation_margin': 'float',
        'is_abp': 'bool',
        'is_class_c': 'bool',
        'name': 'str',
        'relax_f_cnt': 'bool',
        'rx1_dr_offset': 'int',
        'rx2_dr': 'int',
        'rx_delay': 'int',
        'rx_window': 'ApiRXWindow',
        'use_application_settings': 'bool'
    }

    attribute_map = {
        'adr_interval': 'adrInterval',
        'app_eui': 'appEUI',
        'app_key': 'appKey',
        'application_id': 'applicationID',
        'description': 'description',
        'dev_eui': 'devEUI',
        'installation_margin': 'installationMargin',
        'is_abp': 'isABP',
        'is_class_c': 'isClassC',
        'name': 'name',
        'relax_f_cnt': 'relaxFCnt',
        'rx1_dr_offset': 'rx1DROffset',
        'rx2_dr': 'rx2DR',
        'rx_delay': 'rxDelay',
        'rx_window': 'rxWindow',
        'use_application_settings': 'useApplicationSettings'
    }

    def __init__(self, adr_interval=None, app_eui=None, app_key=None, application_id=None, description=None, dev_eui=None, installation_margin=None, is_abp=None, is_class_c=None, name=None, relax_f_cnt=None, rx1_dr_offset=None, rx2_dr=None, rx_delay=None, rx_window=None, use_application_settings=None):  # noqa: E501
        """ApiCreateNodeRequest - a model defined in Swagger"""  # noqa: E501

        self._adr_interval = None
        self._app_eui = None
        self._app_key = None
        self._application_id = None
        self._description = None
        self._dev_eui = None
        self._installation_margin = None
        self._is_abp = None
        self._is_class_c = None
        self._name = None
        self._relax_f_cnt = None
        self._rx1_dr_offset = None
        self._rx2_dr = None
        self._rx_delay = None
        self._rx_window = None
        self._use_application_settings = None
        self.discriminator = None

        if adr_interval is not None:
            self.adr_interval = adr_interval
        if app_eui is not None:
            self.app_eui = app_eui
        if app_key is not None:
            self.app_key = app_key
        if application_id is not None:
            self.application_id = application_id
        if description is not None:
            self.description = description
        if dev_eui is not None:
            self.dev_eui = dev_eui
        if installation_margin is not None:
            self.installation_margin = installation_margin
        if is_abp is not None:
            self.is_abp = is_abp
        if is_class_c is not None:
            self.is_class_c = is_class_c
        if name is not None:
            self.name = name
        if relax_f_cnt is not None:
            self.relax_f_cnt = relax_f_cnt
        if rx1_dr_offset is not None:
            self.rx1_dr_offset = rx1_dr_offset
        if rx2_dr is not None:
            self.rx2_dr = rx2_dr
        if rx_delay is not None:
            self.rx_delay = rx_delay
        if rx_window is not None:
            self.rx_window = rx_window
        if use_application_settings is not None:
            self.use_application_settings = use_application_settings

    @property
    def adr_interval(self):
        """Gets the adr_interval of this ApiCreateNodeRequest.  # noqa: E501

        Interval (in frames) in which the ADR engine may adapt the data-rate of the node (0 = disabled).  # noqa: E501

        :return: The adr_interval of this ApiCreateNodeRequest.  # noqa: E501
        :rtype: int
        """
        return self._adr_interval

    @adr_interval.setter
    def adr_interval(self, adr_interval):
        """Sets the adr_interval of this ApiCreateNodeRequest.

        Interval (in frames) in which the ADR engine may adapt the data-rate of the node (0 = disabled).  # noqa: E501

        :param adr_interval: The adr_interval of this ApiCreateNodeRequest.  # noqa: E501
        :type: int
        """

        self._adr_interval = adr_interval

    @property
    def app_eui(self):
        """Gets the app_eui of this ApiCreateNodeRequest.  # noqa: E501

        Hex encoded AppEUI.  # noqa: E501

        :return: The app_eui of this ApiCreateNodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._app_eui

    @app_eui.setter
    def app_eui(self, app_eui):
        """Sets the app_eui of this ApiCreateNodeRequest.

        Hex encoded AppEUI.  # noqa: E501

        :param app_eui: The app_eui of this ApiCreateNodeRequest.  # noqa: E501
        :type: str
        """

        self._app_eui = app_eui

    @property
    def app_key(self):
        """Gets the app_key of this ApiCreateNodeRequest.  # noqa: E501

        Hex encoded AppKey. When isABP is set to true, this field is not needed.  # noqa: E501

        :return: The app_key of this ApiCreateNodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        """Sets the app_key of this ApiCreateNodeRequest.

        Hex encoded AppKey. When isABP is set to true, this field is not needed.  # noqa: E501

        :param app_key: The app_key of this ApiCreateNodeRequest.  # noqa: E501
        :type: str
        """

        self._app_key = app_key

    @property
    def application_id(self):
        """Gets the application_id of this ApiCreateNodeRequest.  # noqa: E501

        ID of the application to which the node must be added.  # noqa: E501

        :return: The application_id of this ApiCreateNodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ApiCreateNodeRequest.

        ID of the application to which the node must be added.  # noqa: E501

        :param application_id: The application_id of this ApiCreateNodeRequest.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def description(self):
        """Gets the description of this ApiCreateNodeRequest.  # noqa: E501

        Description of the node.  # noqa: E501

        :return: The description of this ApiCreateNodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiCreateNodeRequest.

        Description of the node.  # noqa: E501

        :param description: The description of this ApiCreateNodeRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def dev_eui(self):
        """Gets the dev_eui of this ApiCreateNodeRequest.  # noqa: E501

        Hex encoded DevEUI.  # noqa: E501

        :return: The dev_eui of this ApiCreateNodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._dev_eui

    @dev_eui.setter
    def dev_eui(self, dev_eui):
        """Sets the dev_eui of this ApiCreateNodeRequest.

        Hex encoded DevEUI.  # noqa: E501

        :param dev_eui: The dev_eui of this ApiCreateNodeRequest.  # noqa: E501
        :type: str
        """

        self._dev_eui = dev_eui

    @property
    def installation_margin(self):
        """Gets the installation_margin of this ApiCreateNodeRequest.  # noqa: E501

        Installation-margin to use for ADR calculation.  # noqa: E501

        :return: The installation_margin of this ApiCreateNodeRequest.  # noqa: E501
        :rtype: float
        """
        return self._installation_margin

    @installation_margin.setter
    def installation_margin(self, installation_margin):
        """Sets the installation_margin of this ApiCreateNodeRequest.

        Installation-margin to use for ADR calculation.  # noqa: E501

        :param installation_margin: The installation_margin of this ApiCreateNodeRequest.  # noqa: E501
        :type: float
        """

        self._installation_margin = installation_margin

    @property
    def is_abp(self):
        """Gets the is_abp of this ApiCreateNodeRequest.  # noqa: E501

        Node is activated by ABP.  # noqa: E501

        :return: The is_abp of this ApiCreateNodeRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_abp

    @is_abp.setter
    def is_abp(self, is_abp):
        """Sets the is_abp of this ApiCreateNodeRequest.

        Node is activated by ABP.  # noqa: E501

        :param is_abp: The is_abp of this ApiCreateNodeRequest.  # noqa: E501
        :type: bool
        """

        self._is_abp = is_abp

    @property
    def is_class_c(self):
        """Gets the is_class_c of this ApiCreateNodeRequest.  # noqa: E501

        Node operates in Class-C.  # noqa: E501

        :return: The is_class_c of this ApiCreateNodeRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_class_c

    @is_class_c.setter
    def is_class_c(self, is_class_c):
        """Sets the is_class_c of this ApiCreateNodeRequest.

        Node operates in Class-C.  # noqa: E501

        :param is_class_c: The is_class_c of this ApiCreateNodeRequest.  # noqa: E501
        :type: bool
        """

        self._is_class_c = is_class_c

    @property
    def name(self):
        """Gets the name of this ApiCreateNodeRequest.  # noqa: E501

        Name of the node (if left blank, it will be set to the DevEUI).  # noqa: E501

        :return: The name of this ApiCreateNodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiCreateNodeRequest.

        Name of the node (if left blank, it will be set to the DevEUI).  # noqa: E501

        :param name: The name of this ApiCreateNodeRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def relax_f_cnt(self):
        """Gets the relax_f_cnt of this ApiCreateNodeRequest.  # noqa: E501

        Relax frame-counter mode is enabled.  # noqa: E501

        :return: The relax_f_cnt of this ApiCreateNodeRequest.  # noqa: E501
        :rtype: bool
        """
        return self._relax_f_cnt

    @relax_f_cnt.setter
    def relax_f_cnt(self, relax_f_cnt):
        """Sets the relax_f_cnt of this ApiCreateNodeRequest.

        Relax frame-counter mode is enabled.  # noqa: E501

        :param relax_f_cnt: The relax_f_cnt of this ApiCreateNodeRequest.  # noqa: E501
        :type: bool
        """

        self._relax_f_cnt = relax_f_cnt

    @property
    def rx1_dr_offset(self):
        """Gets the rx1_dr_offset of this ApiCreateNodeRequest.  # noqa: E501

        RX1 data-rate offset.  # noqa: E501

        :return: The rx1_dr_offset of this ApiCreateNodeRequest.  # noqa: E501
        :rtype: int
        """
        return self._rx1_dr_offset

    @rx1_dr_offset.setter
    def rx1_dr_offset(self, rx1_dr_offset):
        """Sets the rx1_dr_offset of this ApiCreateNodeRequest.

        RX1 data-rate offset.  # noqa: E501

        :param rx1_dr_offset: The rx1_dr_offset of this ApiCreateNodeRequest.  # noqa: E501
        :type: int
        """

        self._rx1_dr_offset = rx1_dr_offset

    @property
    def rx2_dr(self):
        """Gets the rx2_dr of this ApiCreateNodeRequest.  # noqa: E501

        Data-rate to use for RX2.  # noqa: E501

        :return: The rx2_dr of this ApiCreateNodeRequest.  # noqa: E501
        :rtype: int
        """
        return self._rx2_dr

    @rx2_dr.setter
    def rx2_dr(self, rx2_dr):
        """Sets the rx2_dr of this ApiCreateNodeRequest.

        Data-rate to use for RX2.  # noqa: E501

        :param rx2_dr: The rx2_dr of this ApiCreateNodeRequest.  # noqa: E501
        :type: int
        """

        self._rx2_dr = rx2_dr

    @property
    def rx_delay(self):
        """Gets the rx_delay of this ApiCreateNodeRequest.  # noqa: E501

        RX delay.  # noqa: E501

        :return: The rx_delay of this ApiCreateNodeRequest.  # noqa: E501
        :rtype: int
        """
        return self._rx_delay

    @rx_delay.setter
    def rx_delay(self, rx_delay):
        """Sets the rx_delay of this ApiCreateNodeRequest.

        RX delay.  # noqa: E501

        :param rx_delay: The rx_delay of this ApiCreateNodeRequest.  # noqa: E501
        :type: int
        """

        self._rx_delay = rx_delay

    @property
    def rx_window(self):
        """Gets the rx_window of this ApiCreateNodeRequest.  # noqa: E501

        RX window to use.  # noqa: E501

        :return: The rx_window of this ApiCreateNodeRequest.  # noqa: E501
        :rtype: ApiRXWindow
        """
        return self._rx_window

    @rx_window.setter
    def rx_window(self, rx_window):
        """Sets the rx_window of this ApiCreateNodeRequest.

        RX window to use.  # noqa: E501

        :param rx_window: The rx_window of this ApiCreateNodeRequest.  # noqa: E501
        :type: ApiRXWindow
        """

        self._rx_window = rx_window

    @property
    def use_application_settings(self):
        """Gets the use_application_settings of this ApiCreateNodeRequest.  # noqa: E501

        When set to true, the application settings will be used to populate the node network settings.  # noqa: E501

        :return: The use_application_settings of this ApiCreateNodeRequest.  # noqa: E501
        :rtype: bool
        """
        return self._use_application_settings

    @use_application_settings.setter
    def use_application_settings(self, use_application_settings):
        """Sets the use_application_settings of this ApiCreateNodeRequest.

        When set to true, the application settings will be used to populate the node network settings.  # noqa: E501

        :param use_application_settings: The use_application_settings of this ApiCreateNodeRequest.  # noqa: E501
        :type: bool
        """

        self._use_application_settings = use_application_settings

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
        if issubclass(ApiCreateNodeRequest, dict):
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
        if not isinstance(other, ApiCreateNodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
