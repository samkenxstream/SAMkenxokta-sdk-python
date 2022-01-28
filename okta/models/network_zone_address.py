# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.10.0
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

import okta.models as models  # noqa
from okta.helpers import to_snake_case

class NetworkZoneAddress(object):
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
    swagger_types = {}
    swagger_types['type'] = 'NetworkZoneAddressType'
    swagger_types['value'] = 'str'

    attribute_map = {
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
        else:
            config = {}
        self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, type=None, value=None, **kwargs):  # noqa: E501
        """NetworkZoneAddress - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._value = None
        self.discriminator = None
        if type is not None:
            if hasattr(models, self.swagger_types['type']):
                nested_class = getattr(models, self.swagger_types['type'])
                if isinstance(type, nested_class):
                    self.type = type
                elif isinstance(type, dict):
                    self.type = nested_class.from_kwargs(**type)
                else:
                    self.type = type
            else:
                self.type = type
        if value is not None:
            if hasattr(models, self.swagger_types['value']):
                nested_class = getattr(models, self.swagger_types['value'])
                if isinstance(value, nested_class):
                    self.value = value
                elif isinstance(value, dict):
                    self.value = nested_class.from_kwargs(**value)
                else:
                    self.value = value
            else:
                self.value = value

    @property
    def type(self):
        """Gets the type of this NetworkZoneAddress.  # noqa: E501


        :return: The type of this NetworkZoneAddress.  # noqa: E501
        :rtype: NetworkZoneAddressType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NetworkZoneAddress.


        :param type: The type of this NetworkZoneAddress.  # noqa: E501
        :type: NetworkZoneAddressType
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this NetworkZoneAddress.  # noqa: E501


        :return: The value of this NetworkZoneAddress.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this NetworkZoneAddress.


        :param value: The value of this NetworkZoneAddress.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(NetworkZoneAddress, dict):
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
        if not isinstance(other, NetworkZoneAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
