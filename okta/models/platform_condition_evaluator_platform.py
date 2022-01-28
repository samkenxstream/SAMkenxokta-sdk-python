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

class PlatformConditionEvaluatorPlatform(object):
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
    swagger_types['os'] = 'PlatformConditionEvaluatorPlatformOperatingSystem'
    swagger_types['type'] = 'PolicyPlatformType'

    attribute_map = {
        'os': 'os',
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

    def set_attributes(self, os=None, type=None, **kwargs):  # noqa: E501
        """PlatformConditionEvaluatorPlatform - a model defined in Swagger"""  # noqa: E501
        self._os = None
        self._type = None
        self.discriminator = None
        if os is not None:
            if hasattr(models, self.swagger_types['os']):
                nested_class = getattr(models, self.swagger_types['os'])
                if isinstance(os, nested_class):
                    self.os = os
                elif isinstance(os, dict):
                    self.os = nested_class.from_kwargs(**os)
                else:
                    self.os = os
            else:
                self.os = os
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
    def os(self):
        """Gets the os of this PlatformConditionEvaluatorPlatform.  # noqa: E501


        :return: The os of this PlatformConditionEvaluatorPlatform.  # noqa: E501
        :rtype: PlatformConditionEvaluatorPlatformOperatingSystem
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this PlatformConditionEvaluatorPlatform.


        :param os: The os of this PlatformConditionEvaluatorPlatform.  # noqa: E501
        :type: PlatformConditionEvaluatorPlatformOperatingSystem
        """

        self._os = os

    @property
    def type(self):
        """Gets the type of this PlatformConditionEvaluatorPlatform.  # noqa: E501


        :return: The type of this PlatformConditionEvaluatorPlatform.  # noqa: E501
        :rtype: PolicyPlatformType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PlatformConditionEvaluatorPlatform.


        :param type: The type of this PlatformConditionEvaluatorPlatform.  # noqa: E501
        :type: PolicyPlatformType
        """

        self._type = type

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
        if issubclass(PlatformConditionEvaluatorPlatform, dict):
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
        if not isinstance(other, PlatformConditionEvaluatorPlatform):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
