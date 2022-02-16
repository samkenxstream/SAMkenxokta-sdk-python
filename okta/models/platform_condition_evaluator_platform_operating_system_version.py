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

class PlatformConditionEvaluatorPlatformOperatingSystemVersion(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    swagger_types['match_type'] = 'PlatformConditionOperatingSystemVersionMatchType'
    swagger_types['value'] = 'str'

    attribute_map = {
        'match_type': 'matchType',
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

    def set_attributes(self, match_type=None, value=None, **kwargs):  # noqa: E501
        """PlatformConditionEvaluatorPlatformOperatingSystemVersion - a model defined in Swagger"""  # noqa: E501
        self._match_type = None
        self._value = None
        self.discriminator = None
        if match_type is not None:
            if hasattr(models, self.swagger_types['match_type']):
                nested_class = getattr(models, self.swagger_types['match_type'])
                if isinstance(match_type, nested_class):
                    self.match_type = match_type
                elif isinstance(match_type, dict):
                    self.match_type = nested_class.from_kwargs(**match_type)
                else:
                    self.match_type = match_type
            else:
                self.match_type = match_type
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
    def match_type(self):
        """Gets the match_type of this PlatformConditionEvaluatorPlatformOperatingSystemVersion.  # noqa: E501


        :return: The match_type of this PlatformConditionEvaluatorPlatformOperatingSystemVersion.  # noqa: E501
        :rtype: PlatformConditionOperatingSystemVersionMatchType
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """Sets the match_type of this PlatformConditionEvaluatorPlatformOperatingSystemVersion.


        :param match_type: The match_type of this PlatformConditionEvaluatorPlatformOperatingSystemVersion.  # noqa: E501
        :type: PlatformConditionOperatingSystemVersionMatchType
        """

        self._match_type = match_type

    @property
    def value(self):
        """Gets the value of this PlatformConditionEvaluatorPlatformOperatingSystemVersion.  # noqa: E501


        :return: The value of this PlatformConditionEvaluatorPlatformOperatingSystemVersion.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PlatformConditionEvaluatorPlatformOperatingSystemVersion.


        :param value: The value of this PlatformConditionEvaluatorPlatformOperatingSystemVersion.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(PlatformConditionEvaluatorPlatformOperatingSystemVersion, dict):
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
        if not isinstance(other, PlatformConditionEvaluatorPlatformOperatingSystemVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
