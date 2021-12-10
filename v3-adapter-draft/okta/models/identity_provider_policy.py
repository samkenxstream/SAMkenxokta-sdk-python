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
from okta.models.policy import Policy  # noqa: F401,E501

class IdentityProviderPolicy(Policy):
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
        'account_link': 'PolicyAccountLink',
        'max_clock_skew': 'int',
        'provisioning': 'Provisioning',
        'subject': 'PolicySubject'
    }
    if hasattr(Policy, "swagger_types"):
        swagger_types.update(Policy.swagger_types)

    attribute_map = {
        'account_link': 'accountLink',
        'max_clock_skew': 'maxClockSkew',
        'provisioning': 'provisioning',
        'subject': 'subject'
    }
    if hasattr(Policy, "attribute_map"):
        attribute_map.update(Policy.attribute_map)

    def __init__(self, config=None):
        super().__init__(config)
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, account_link=None, max_clock_skew=None, provisioning=None, subject=None, *args, **kwargs):  # noqa: E501
        """IdentityProviderPolicy - a model defined in Swagger"""  # noqa: E501
        self._account_link = None
        self._max_clock_skew = None
        self._provisioning = None
        self._subject = None
        self.discriminator = None
        if account_link is not None:
            self.account_link = account_link
        if max_clock_skew is not None:
            self.max_clock_skew = max_clock_skew
        if provisioning is not None:
            self.provisioning = provisioning
        if subject is not None:
            self.subject = subject

    @property
    def account_link(self):
        """Gets the account_link of this IdentityProviderPolicy.  # noqa: E501


        :return: The account_link of this IdentityProviderPolicy.  # noqa: E501
        :rtype: PolicyAccountLink
        """
        return self._account_link

    @account_link.setter
    def account_link(self, account_link):
        """Sets the account_link of this IdentityProviderPolicy.


        :param account_link: The account_link of this IdentityProviderPolicy.  # noqa: E501
        :type: PolicyAccountLink
        """

        self._account_link = account_link

    @property
    def max_clock_skew(self):
        """Gets the max_clock_skew of this IdentityProviderPolicy.  # noqa: E501


        :return: The max_clock_skew of this IdentityProviderPolicy.  # noqa: E501
        :rtype: int
        """
        return self._max_clock_skew

    @max_clock_skew.setter
    def max_clock_skew(self, max_clock_skew):
        """Sets the max_clock_skew of this IdentityProviderPolicy.


        :param max_clock_skew: The max_clock_skew of this IdentityProviderPolicy.  # noqa: E501
        :type: int
        """

        self._max_clock_skew = max_clock_skew

    @property
    def provisioning(self):
        """Gets the provisioning of this IdentityProviderPolicy.  # noqa: E501


        :return: The provisioning of this IdentityProviderPolicy.  # noqa: E501
        :rtype: Provisioning
        """
        return self._provisioning

    @provisioning.setter
    def provisioning(self, provisioning):
        """Sets the provisioning of this IdentityProviderPolicy.


        :param provisioning: The provisioning of this IdentityProviderPolicy.  # noqa: E501
        :type: Provisioning
        """

        self._provisioning = provisioning

    @property
    def subject(self):
        """Gets the subject of this IdentityProviderPolicy.  # noqa: E501


        :return: The subject of this IdentityProviderPolicy.  # noqa: E501
        :rtype: PolicySubject
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this IdentityProviderPolicy.


        :param subject: The subject of this IdentityProviderPolicy.  # noqa: E501
        :type: PolicySubject
        """

        self._subject = subject

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
        if issubclass(IdentityProviderPolicy, dict):
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
        if not isinstance(other, IdentityProviderPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
