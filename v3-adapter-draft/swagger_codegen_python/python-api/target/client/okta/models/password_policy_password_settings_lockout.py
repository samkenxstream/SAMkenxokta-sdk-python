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

class PasswordPolicyPasswordSettingsLockout(object):
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
        'auto_unlock_minutes': 'int',
        'max_attempts': 'int',
        'show_lockout_failures': 'bool',
        'user_lockout_notification_channels': 'list[str]'
    }

    attribute_map = {
        'auto_unlock_minutes': 'autoUnlockMinutes',
        'max_attempts': 'maxAttempts',
        'show_lockout_failures': 'showLockoutFailures',
        'user_lockout_notification_channels': 'userLockoutNotificationChannels'
    }

    def __init__(self, config=None):
        super().__init__(config)
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, auto_unlock_minutes=None, max_attempts=None, show_lockout_failures=None, user_lockout_notification_channels=None):  # noqa: E501
        """PasswordPolicyPasswordSettingsLockout - a model defined in Swagger"""  # noqa: E501
        self._auto_unlock_minutes = None
        self._max_attempts = None
        self._show_lockout_failures = None
        self._user_lockout_notification_channels = None
        self.discriminator = None
        if auto_unlock_minutes is not None:
            self.auto_unlock_minutes = auto_unlock_minutes
        if max_attempts is not None:
            self.max_attempts = max_attempts
        if show_lockout_failures is not None:
            self.show_lockout_failures = show_lockout_failures
        if user_lockout_notification_channels is not None:
            self.user_lockout_notification_channels = user_lockout_notification_channels

    @property
    def auto_unlock_minutes(self):
        """Gets the auto_unlock_minutes of this PasswordPolicyPasswordSettingsLockout.  # noqa: E501


        :return: The auto_unlock_minutes of this PasswordPolicyPasswordSettingsLockout.  # noqa: E501
        :rtype: int
        """
        return self._auto_unlock_minutes

    @auto_unlock_minutes.setter
    def auto_unlock_minutes(self, auto_unlock_minutes):
        """Sets the auto_unlock_minutes of this PasswordPolicyPasswordSettingsLockout.


        :param auto_unlock_minutes: The auto_unlock_minutes of this PasswordPolicyPasswordSettingsLockout.  # noqa: E501
        :type: int
        """

        self._auto_unlock_minutes = auto_unlock_minutes

    @property
    def max_attempts(self):
        """Gets the max_attempts of this PasswordPolicyPasswordSettingsLockout.  # noqa: E501


        :return: The max_attempts of this PasswordPolicyPasswordSettingsLockout.  # noqa: E501
        :rtype: int
        """
        return self._max_attempts

    @max_attempts.setter
    def max_attempts(self, max_attempts):
        """Sets the max_attempts of this PasswordPolicyPasswordSettingsLockout.


        :param max_attempts: The max_attempts of this PasswordPolicyPasswordSettingsLockout.  # noqa: E501
        :type: int
        """

        self._max_attempts = max_attempts

    @property
    def show_lockout_failures(self):
        """Gets the show_lockout_failures of this PasswordPolicyPasswordSettingsLockout.  # noqa: E501


        :return: The show_lockout_failures of this PasswordPolicyPasswordSettingsLockout.  # noqa: E501
        :rtype: bool
        """
        return self._show_lockout_failures

    @show_lockout_failures.setter
    def show_lockout_failures(self, show_lockout_failures):
        """Sets the show_lockout_failures of this PasswordPolicyPasswordSettingsLockout.


        :param show_lockout_failures: The show_lockout_failures of this PasswordPolicyPasswordSettingsLockout.  # noqa: E501
        :type: bool
        """

        self._show_lockout_failures = show_lockout_failures

    @property
    def user_lockout_notification_channels(self):
        """Gets the user_lockout_notification_channels of this PasswordPolicyPasswordSettingsLockout.  # noqa: E501


        :return: The user_lockout_notification_channels of this PasswordPolicyPasswordSettingsLockout.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_lockout_notification_channels

    @user_lockout_notification_channels.setter
    def user_lockout_notification_channels(self, user_lockout_notification_channels):
        """Sets the user_lockout_notification_channels of this PasswordPolicyPasswordSettingsLockout.


        :param user_lockout_notification_channels: The user_lockout_notification_channels of this PasswordPolicyPasswordSettingsLockout.  # noqa: E501
        :type: list[str]
        """

        self._user_lockout_notification_channels = user_lockout_notification_channels

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
        if issubclass(PasswordPolicyPasswordSettingsLockout, dict):
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
        if not isinstance(other, PasswordPolicyPasswordSettingsLockout):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
