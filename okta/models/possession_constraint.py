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
from okta.models.access_policy_constraint import AccessPolicyConstraint  # noqa: F401,E501

import okta.models as models  # noqa
from okta.helpers import to_snake_case

class PossessionConstraint(AccessPolicyConstraint):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    if hasattr(AccessPolicyConstraint, "swagger_types"):
        swagger_types.update(AccessPolicyConstraint.swagger_types)
    swagger_types['device_bound'] = 'str'
    swagger_types['hardware_protection'] = 'str'
    swagger_types['phishing_resistant'] = 'str'
    swagger_types['user_presence'] = 'str'

    attribute_map = {
        'device_bound': 'deviceBound',
        'hardware_protection': 'hardwareProtection',
        'phishing_resistant': 'phishingResistant',
        'user_presence': 'userPresence'
    }
    if hasattr(AccessPolicyConstraint, "attribute_map"):
        attribute_map.update(AccessPolicyConstraint.attribute_map)

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
        else:
            config = {}
        self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, device_bound=None, hardware_protection=None, phishing_resistant=None, user_presence=None, **kwargs):  # noqa: E501
        """PossessionConstraint - a model defined in Swagger"""  # noqa: E501
        config = {}
        if kwargs is not None:
            config = {to_snake_case(key): value for key, value in kwargs.items()}
        super().set_attributes(**config)
        self._device_bound = None
        self._hardware_protection = None
        self._phishing_resistant = None
        self._user_presence = None
        self.discriminator = None
        if device_bound is not None:
            if hasattr(models, self.swagger_types['device_bound']):
                nested_class = getattr(models, self.swagger_types['device_bound'])
                if isinstance(device_bound, nested_class):
                    self.device_bound = device_bound
                elif isinstance(device_bound, dict):
                    self.device_bound = nested_class.from_kwargs(**device_bound)
                else:
                    self.device_bound = device_bound
            else:
                self.device_bound = device_bound
        if hardware_protection is not None:
            if hasattr(models, self.swagger_types['hardware_protection']):
                nested_class = getattr(models, self.swagger_types['hardware_protection'])
                if isinstance(hardware_protection, nested_class):
                    self.hardware_protection = hardware_protection
                elif isinstance(hardware_protection, dict):
                    self.hardware_protection = nested_class.from_kwargs(**hardware_protection)
                else:
                    self.hardware_protection = hardware_protection
            else:
                self.hardware_protection = hardware_protection
        if phishing_resistant is not None:
            if hasattr(models, self.swagger_types['phishing_resistant']):
                nested_class = getattr(models, self.swagger_types['phishing_resistant'])
                if isinstance(phishing_resistant, nested_class):
                    self.phishing_resistant = phishing_resistant
                elif isinstance(phishing_resistant, dict):
                    self.phishing_resistant = nested_class.from_kwargs(**phishing_resistant)
                else:
                    self.phishing_resistant = phishing_resistant
            else:
                self.phishing_resistant = phishing_resistant
        if user_presence is not None:
            if hasattr(models, self.swagger_types['user_presence']):
                nested_class = getattr(models, self.swagger_types['user_presence'])
                if isinstance(user_presence, nested_class):
                    self.user_presence = user_presence
                elif isinstance(user_presence, dict):
                    self.user_presence = nested_class.from_kwargs(**user_presence)
                else:
                    self.user_presence = user_presence
            else:
                self.user_presence = user_presence

    @property
    def device_bound(self):
        """Gets the device_bound of this PossessionConstraint.  # noqa: E501


        :return: The device_bound of this PossessionConstraint.  # noqa: E501
        :rtype: str
        """
        return self._device_bound

    @device_bound.setter
    def device_bound(self, device_bound):
        """Sets the device_bound of this PossessionConstraint.


        :param device_bound: The device_bound of this PossessionConstraint.  # noqa: E501
        :type: str
        """

        self._device_bound = device_bound

    @property
    def hardware_protection(self):
        """Gets the hardware_protection of this PossessionConstraint.  # noqa: E501


        :return: The hardware_protection of this PossessionConstraint.  # noqa: E501
        :rtype: str
        """
        return self._hardware_protection

    @hardware_protection.setter
    def hardware_protection(self, hardware_protection):
        """Sets the hardware_protection of this PossessionConstraint.


        :param hardware_protection: The hardware_protection of this PossessionConstraint.  # noqa: E501
        :type: str
        """

        self._hardware_protection = hardware_protection

    @property
    def phishing_resistant(self):
        """Gets the phishing_resistant of this PossessionConstraint.  # noqa: E501


        :return: The phishing_resistant of this PossessionConstraint.  # noqa: E501
        :rtype: str
        """
        return self._phishing_resistant

    @phishing_resistant.setter
    def phishing_resistant(self, phishing_resistant):
        """Sets the phishing_resistant of this PossessionConstraint.


        :param phishing_resistant: The phishing_resistant of this PossessionConstraint.  # noqa: E501
        :type: str
        """

        self._phishing_resistant = phishing_resistant

    @property
    def user_presence(self):
        """Gets the user_presence of this PossessionConstraint.  # noqa: E501


        :return: The user_presence of this PossessionConstraint.  # noqa: E501
        :rtype: str
        """
        return self._user_presence

    @user_presence.setter
    def user_presence(self, user_presence):
        """Sets the user_presence of this PossessionConstraint.


        :param user_presence: The user_presence of this PossessionConstraint.  # noqa: E501
        :type: str
        """

        self._user_presence = user_presence

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
        if issubclass(PossessionConstraint, dict):
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
        if not isinstance(other, PossessionConstraint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
