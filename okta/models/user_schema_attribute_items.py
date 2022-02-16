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

class UserSchemaAttributeItems(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    swagger_types['enum'] = 'list[str]'
    swagger_types['one_of'] = 'list[UserSchemaAttributeEnum]'
    swagger_types['type'] = 'str'

    attribute_map = {
        'enum': 'enum',
        'one_of': 'oneOf',
        'type': 'type'
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

    def set_attributes(self, enum=None, one_of=None, type=None, **kwargs):  # noqa: E501
        """UserSchemaAttributeItems - a model defined in Swagger"""  # noqa: E501
        self._enum = None
        self._one_of = None
        self._type = None
        self.discriminator = None
        if enum is not None:
            if hasattr(models, self.swagger_types['enum']):
                nested_class = getattr(models, self.swagger_types['enum'])
                if isinstance(enum, nested_class):
                    self.enum = enum
                elif isinstance(enum, dict):
                    self.enum = nested_class.from_kwargs(**enum)
                else:
                    self.enum = enum
            else:
                self.enum = enum
        if one_of is not None:
            if hasattr(models, self.swagger_types['one_of']):
                nested_class = getattr(models, self.swagger_types['one_of'])
                if isinstance(one_of, nested_class):
                    self.one_of = one_of
                elif isinstance(one_of, dict):
                    self.one_of = nested_class.from_kwargs(**one_of)
                else:
                    self.one_of = one_of
            else:
                self.one_of = one_of
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

    @property
    def enum(self):
        """Gets the enum of this UserSchemaAttributeItems.  # noqa: E501


        :return: The enum of this UserSchemaAttributeItems.  # noqa: E501
        :rtype: list[str]
        """
        return self._enum

    @enum.setter
    def enum(self, enum):
        """Sets the enum of this UserSchemaAttributeItems.


        :param enum: The enum of this UserSchemaAttributeItems.  # noqa: E501
        :type: list[str]
        """

        self._enum = enum

    @property
    def one_of(self):
        """Gets the one_of of this UserSchemaAttributeItems.  # noqa: E501


        :return: The one_of of this UserSchemaAttributeItems.  # noqa: E501
        :rtype: list[UserSchemaAttributeEnum]
        """
        return self._one_of

    @one_of.setter
    def one_of(self, one_of):
        """Sets the one_of of this UserSchemaAttributeItems.


        :param one_of: The one_of of this UserSchemaAttributeItems.  # noqa: E501
        :type: list[UserSchemaAttributeEnum]
        """

        self._one_of = one_of

    @property
    def type(self):
        """Gets the type of this UserSchemaAttributeItems.  # noqa: E501


        :return: The type of this UserSchemaAttributeItems.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UserSchemaAttributeItems.


        :param type: The type of this UserSchemaAttributeItems.  # noqa: E501
        :type: str
        """

        self._type = type

    def as_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.as_dict() if hasattr(x, "as_dict") else x,
                    value
                ))
            elif hasattr(value, "as_dict"):
                result[attr] = value.as_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].as_dict())
                    if hasattr(item[1], "as_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UserSchemaAttributeItems, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.as_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserSchemaAttributeItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
