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

class PushUserFactor(UserFactor):
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
        'expires_at': 'datetime',
        'factor_result': 'FactorResultType',
        'profile': 'PushUserFactorProfile'
    }
    if hasattr(UserFactor, "swagger_types"):
        swagger_types.update(UserFactor.swagger_types)

    attribute_map = {
        'expires_at': 'expiresAt',
        'factor_result': 'factorResult',
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

    def set_attributes(self, expires_at=None, factor_result=None, profile=None, *args, **kwargs):  # noqa: E501
        """PushUserFactor - a model defined in Swagger"""  # noqa: E501
        self._expires_at = None
        self._factor_result = None
        self._profile = None
        self.discriminator = None
        if expires_at is not None:
            self.expires_at = expires_at
        if factor_result is not None:
            self.factor_result = factor_result
        if profile is not None:
            self.profile = profile

    @property
    def expires_at(self):
        """Gets the expires_at of this PushUserFactor.  # noqa: E501


        :return: The expires_at of this PushUserFactor.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this PushUserFactor.


        :param expires_at: The expires_at of this PushUserFactor.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def factor_result(self):
        """Gets the factor_result of this PushUserFactor.  # noqa: E501


        :return: The factor_result of this PushUserFactor.  # noqa: E501
        :rtype: FactorResultType
        """
        return self._factor_result

    @factor_result.setter
    def factor_result(self, factor_result):
        """Sets the factor_result of this PushUserFactor.


        :param factor_result: The factor_result of this PushUserFactor.  # noqa: E501
        :type: FactorResultType
        """

        self._factor_result = factor_result

    @property
    def profile(self):
        """Gets the profile of this PushUserFactor.  # noqa: E501


        :return: The profile of this PushUserFactor.  # noqa: E501
        :rtype: PushUserFactorProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this PushUserFactor.


        :param profile: The profile of this PushUserFactor.  # noqa: E501
        :type: PushUserFactorProfile
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
        if issubclass(PushUserFactor, dict):
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
        if not isinstance(other, PushUserFactor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
