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

class PasswordPolicyRecoveryFactors(object):
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
        'okta_call': 'PasswordPolicyRecoveryFactorSettings',
        'okta_email': 'PasswordPolicyRecoveryEmail',
        'okta_sms': 'PasswordPolicyRecoveryFactorSettings',
        'recovery_question': 'PasswordPolicyRecoveryQuestion'
    }

    attribute_map = {
        'okta_call': 'okta_call',
        'okta_email': 'okta_email',
        'okta_sms': 'okta_sms',
        'recovery_question': 'recovery_question'
    }

    def __init__(self, config=None):
        super().__init__(config)
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, okta_call=None, okta_email=None, okta_sms=None, recovery_question=None):  # noqa: E501
        """PasswordPolicyRecoveryFactors - a model defined in Swagger"""  # noqa: E501
        self._okta_call = None
        self._okta_email = None
        self._okta_sms = None
        self._recovery_question = None
        self.discriminator = None
        if okta_call is not None:
            self.okta_call = okta_call
        if okta_email is not None:
            self.okta_email = okta_email
        if okta_sms is not None:
            self.okta_sms = okta_sms
        if recovery_question is not None:
            self.recovery_question = recovery_question

    @property
    def okta_call(self):
        """Gets the okta_call of this PasswordPolicyRecoveryFactors.  # noqa: E501


        :return: The okta_call of this PasswordPolicyRecoveryFactors.  # noqa: E501
        :rtype: PasswordPolicyRecoveryFactorSettings
        """
        return self._okta_call

    @okta_call.setter
    def okta_call(self, okta_call):
        """Sets the okta_call of this PasswordPolicyRecoveryFactors.


        :param okta_call: The okta_call of this PasswordPolicyRecoveryFactors.  # noqa: E501
        :type: PasswordPolicyRecoveryFactorSettings
        """

        self._okta_call = okta_call

    @property
    def okta_email(self):
        """Gets the okta_email of this PasswordPolicyRecoveryFactors.  # noqa: E501


        :return: The okta_email of this PasswordPolicyRecoveryFactors.  # noqa: E501
        :rtype: PasswordPolicyRecoveryEmail
        """
        return self._okta_email

    @okta_email.setter
    def okta_email(self, okta_email):
        """Sets the okta_email of this PasswordPolicyRecoveryFactors.


        :param okta_email: The okta_email of this PasswordPolicyRecoveryFactors.  # noqa: E501
        :type: PasswordPolicyRecoveryEmail
        """

        self._okta_email = okta_email

    @property
    def okta_sms(self):
        """Gets the okta_sms of this PasswordPolicyRecoveryFactors.  # noqa: E501


        :return: The okta_sms of this PasswordPolicyRecoveryFactors.  # noqa: E501
        :rtype: PasswordPolicyRecoveryFactorSettings
        """
        return self._okta_sms

    @okta_sms.setter
    def okta_sms(self, okta_sms):
        """Sets the okta_sms of this PasswordPolicyRecoveryFactors.


        :param okta_sms: The okta_sms of this PasswordPolicyRecoveryFactors.  # noqa: E501
        :type: PasswordPolicyRecoveryFactorSettings
        """

        self._okta_sms = okta_sms

    @property
    def recovery_question(self):
        """Gets the recovery_question of this PasswordPolicyRecoveryFactors.  # noqa: E501


        :return: The recovery_question of this PasswordPolicyRecoveryFactors.  # noqa: E501
        :rtype: PasswordPolicyRecoveryQuestion
        """
        return self._recovery_question

    @recovery_question.setter
    def recovery_question(self, recovery_question):
        """Sets the recovery_question of this PasswordPolicyRecoveryFactors.


        :param recovery_question: The recovery_question of this PasswordPolicyRecoveryFactors.  # noqa: E501
        :type: PasswordPolicyRecoveryQuestion
        """

        self._recovery_question = recovery_question

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
        if issubclass(PasswordPolicyRecoveryFactors, dict):
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
        if not isinstance(other, PasswordPolicyRecoveryFactors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
