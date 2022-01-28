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

class PasswordPolicyRecoveryEmailProperties(object):
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
    swagger_types['recovery_token'] = 'PasswordPolicyRecoveryEmailRecoveryToken'

    attribute_map = {
        'recovery_token': 'recoveryToken'
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

    def set_attributes(self, recovery_token=None, **kwargs):  # noqa: E501
        """PasswordPolicyRecoveryEmailProperties - a model defined in Swagger"""  # noqa: E501
        self._recovery_token = None
        self.discriminator = None
        if recovery_token is not None:
            if hasattr(models, self.swagger_types['recovery_token']):
                nested_class = getattr(models, self.swagger_types['recovery_token'])
                if isinstance(recovery_token, nested_class):
                    self.recovery_token = recovery_token
                elif isinstance(recovery_token, dict):
                    self.recovery_token = nested_class.from_kwargs(**recovery_token)
                else:
                    self.recovery_token = recovery_token
            else:
                self.recovery_token = recovery_token

    @property
    def recovery_token(self):
        """Gets the recovery_token of this PasswordPolicyRecoveryEmailProperties.  # noqa: E501


        :return: The recovery_token of this PasswordPolicyRecoveryEmailProperties.  # noqa: E501
        :rtype: PasswordPolicyRecoveryEmailRecoveryToken
        """
        return self._recovery_token

    @recovery_token.setter
    def recovery_token(self, recovery_token):
        """Sets the recovery_token of this PasswordPolicyRecoveryEmailProperties.


        :param recovery_token: The recovery_token of this PasswordPolicyRecoveryEmailProperties.  # noqa: E501
        :type: PasswordPolicyRecoveryEmailRecoveryToken
        """

        self._recovery_token = recovery_token

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
        if issubclass(PasswordPolicyRecoveryEmailProperties, dict):
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
        if not isinstance(other, PasswordPolicyRecoveryEmailProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
