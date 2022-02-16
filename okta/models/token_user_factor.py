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
from okta.models.user_factor import UserFactor  # noqa: F401,E501

import okta.models as models  # noqa
from okta.helpers import to_snake_case

class TokenUserFactor(UserFactor):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    if hasattr(UserFactor, "swagger_types"):
        swagger_types.update(UserFactor.swagger_types)
    swagger_types['profile'] = 'TokenUserFactorProfile'

    attribute_map = {
        'profile': 'profile'
    }
    if hasattr(UserFactor, "attribute_map"):
        attribute_map.update(UserFactor.attribute_map)

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
        else:
            config = {}
        self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, profile=None, **kwargs):  # noqa: E501
        """TokenUserFactor - a model defined in Swagger"""  # noqa: E501
        config = {}
        if kwargs is not None:
            config = {to_snake_case(key): value for key, value in kwargs.items()}
        super().set_attributes(**config)
        self._profile = None
        self.discriminator = None
        if profile is not None:
            if hasattr(models, self.swagger_types['profile']):
                nested_class = getattr(models, self.swagger_types['profile'])
                if isinstance(profile, nested_class):
                    self.profile = profile
                elif isinstance(profile, dict):
                    self.profile = nested_class.from_kwargs(**profile)
                else:
                    self.profile = profile
            else:
                self.profile = profile

    @property
    def profile(self):
        """Gets the profile of this TokenUserFactor.  # noqa: E501


        :return: The profile of this TokenUserFactor.  # noqa: E501
        :rtype: TokenUserFactorProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this TokenUserFactor.


        :param profile: The profile of this TokenUserFactor.  # noqa: E501
        :type: TokenUserFactorProfile
        """

        self._profile = profile

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
        if issubclass(TokenUserFactor, dict):
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
        if not isinstance(other, TokenUserFactor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
