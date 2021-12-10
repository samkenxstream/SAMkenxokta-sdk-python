# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from okta.models.user_factor import UserFactor  # noqa: F401,E501

class HardwareUserFactor(UserFactor):
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
        'profile': 'HardwareUserFactorProfile'
    }
    if hasattr(UserFactor, "swagger_types"):
        swagger_types.update(UserFactor.swagger_types)

    attribute_map = {
        'profile': 'profile'
    }
    if hasattr(UserFactor, "attribute_map"):
        attribute_map.update(UserFactor.attribute_map)

    def __init__(self, config=None):
        super().__init__(config)
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, profile=None, *args, **kwargs):  # noqa: E501
        """HardwareUserFactor - a model defined in Swagger"""  # noqa: E501
        self._profile = None
        self.discriminator = None
        if profile is not None:
            self.profile = profile

    @property
    def profile(self):
        """Gets the profile of this HardwareUserFactor.  # noqa: E501


        :return: The profile of this HardwareUserFactor.  # noqa: E501
        :rtype: HardwareUserFactorProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this HardwareUserFactor.


        :param profile: The profile of this HardwareUserFactor.  # noqa: E501
        :type: HardwareUserFactorProfile
        """

        self._profile = profile

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
        if issubclass(HardwareUserFactor, dict):
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
        if not isinstance(other, HardwareUserFactor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
