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

class OktaSignOnPolicyRuleSignonSessionActions(object):
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
        'max_session_idle_minutes': 'int',
        'max_session_lifetime_minutes': 'int',
        'use_persistent_cookie': 'bool'
    }

    attribute_map = {
        'max_session_idle_minutes': 'maxSessionIdleMinutes',
        'max_session_lifetime_minutes': 'maxSessionLifetimeMinutes',
        'use_persistent_cookie': 'usePersistentCookie'
    }

    def __init__(self, config=None):
        super().__init__(config)
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, max_session_idle_minutes=None, max_session_lifetime_minutes=None, use_persistent_cookie=False):  # noqa: E501
        """OktaSignOnPolicyRuleSignonSessionActions - a model defined in Swagger"""  # noqa: E501
        self._max_session_idle_minutes = None
        self._max_session_lifetime_minutes = None
        self._use_persistent_cookie = None
        self.discriminator = None
        if max_session_idle_minutes is not None:
            self.max_session_idle_minutes = max_session_idle_minutes
        if max_session_lifetime_minutes is not None:
            self.max_session_lifetime_minutes = max_session_lifetime_minutes
        if use_persistent_cookie is not None:
            self.use_persistent_cookie = use_persistent_cookie

    @property
    def max_session_idle_minutes(self):
        """Gets the max_session_idle_minutes of this OktaSignOnPolicyRuleSignonSessionActions.  # noqa: E501


        :return: The max_session_idle_minutes of this OktaSignOnPolicyRuleSignonSessionActions.  # noqa: E501
        :rtype: int
        """
        return self._max_session_idle_minutes

    @max_session_idle_minutes.setter
    def max_session_idle_minutes(self, max_session_idle_minutes):
        """Sets the max_session_idle_minutes of this OktaSignOnPolicyRuleSignonSessionActions.


        :param max_session_idle_minutes: The max_session_idle_minutes of this OktaSignOnPolicyRuleSignonSessionActions.  # noqa: E501
        :type: int
        """

        self._max_session_idle_minutes = max_session_idle_minutes

    @property
    def max_session_lifetime_minutes(self):
        """Gets the max_session_lifetime_minutes of this OktaSignOnPolicyRuleSignonSessionActions.  # noqa: E501


        :return: The max_session_lifetime_minutes of this OktaSignOnPolicyRuleSignonSessionActions.  # noqa: E501
        :rtype: int
        """
        return self._max_session_lifetime_minutes

    @max_session_lifetime_minutes.setter
    def max_session_lifetime_minutes(self, max_session_lifetime_minutes):
        """Sets the max_session_lifetime_minutes of this OktaSignOnPolicyRuleSignonSessionActions.


        :param max_session_lifetime_minutes: The max_session_lifetime_minutes of this OktaSignOnPolicyRuleSignonSessionActions.  # noqa: E501
        :type: int
        """

        self._max_session_lifetime_minutes = max_session_lifetime_minutes

    @property
    def use_persistent_cookie(self):
        """Gets the use_persistent_cookie of this OktaSignOnPolicyRuleSignonSessionActions.  # noqa: E501


        :return: The use_persistent_cookie of this OktaSignOnPolicyRuleSignonSessionActions.  # noqa: E501
        :rtype: bool
        """
        return self._use_persistent_cookie

    @use_persistent_cookie.setter
    def use_persistent_cookie(self, use_persistent_cookie):
        """Sets the use_persistent_cookie of this OktaSignOnPolicyRuleSignonSessionActions.


        :param use_persistent_cookie: The use_persistent_cookie of this OktaSignOnPolicyRuleSignonSessionActions.  # noqa: E501
        :type: bool
        """

        self._use_persistent_cookie = use_persistent_cookie

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
        if issubclass(OktaSignOnPolicyRuleSignonSessionActions, dict):
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
        if not isinstance(other, OktaSignOnPolicyRuleSignonSessionActions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
