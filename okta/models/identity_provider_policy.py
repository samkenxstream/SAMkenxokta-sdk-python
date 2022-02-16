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
from okta.models.policy import Policy  # noqa: F401,E501

import okta.models as models  # noqa
from okta.helpers import to_snake_case

class IdentityProviderPolicy(Policy):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    if hasattr(Policy, "swagger_types"):
        swagger_types.update(Policy.swagger_types)
    swagger_types['account_link'] = 'PolicyAccountLink'
    swagger_types['max_clock_skew'] = 'int'
    swagger_types['provisioning'] = 'Provisioning'
    swagger_types['subject'] = 'PolicySubject'

    attribute_map = {
        'account_link': 'accountLink',
        'max_clock_skew': 'maxClockSkew',
        'provisioning': 'provisioning',
        'subject': 'subject'
    }
    if hasattr(Policy, "attribute_map"):
        attribute_map.update(Policy.attribute_map)

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
        else:
            config = {}
        self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, account_link=None, max_clock_skew=None, provisioning=None, subject=None, **kwargs):  # noqa: E501
        """IdentityProviderPolicy - a model defined in Swagger"""  # noqa: E501
        config = {}
        if kwargs is not None:
            config = {to_snake_case(key): value for key, value in kwargs.items()}
        super().set_attributes(**config)
        self._account_link = None
        self._max_clock_skew = None
        self._provisioning = None
        self._subject = None
        self.discriminator = None
        if account_link is not None:
            if hasattr(models, self.swagger_types['account_link']):
                nested_class = getattr(models, self.swagger_types['account_link'])
                if isinstance(account_link, nested_class):
                    self.account_link = account_link
                elif isinstance(account_link, dict):
                    self.account_link = nested_class.from_kwargs(**account_link)
                else:
                    self.account_link = account_link
            else:
                self.account_link = account_link
        if max_clock_skew is not None:
            if hasattr(models, self.swagger_types['max_clock_skew']):
                nested_class = getattr(models, self.swagger_types['max_clock_skew'])
                if isinstance(max_clock_skew, nested_class):
                    self.max_clock_skew = max_clock_skew
                elif isinstance(max_clock_skew, dict):
                    self.max_clock_skew = nested_class.from_kwargs(**max_clock_skew)
                else:
                    self.max_clock_skew = max_clock_skew
            else:
                self.max_clock_skew = max_clock_skew
        if provisioning is not None:
            if hasattr(models, self.swagger_types['provisioning']):
                nested_class = getattr(models, self.swagger_types['provisioning'])
                if isinstance(provisioning, nested_class):
                    self.provisioning = provisioning
                elif isinstance(provisioning, dict):
                    self.provisioning = nested_class.from_kwargs(**provisioning)
                else:
                    self.provisioning = provisioning
            else:
                self.provisioning = provisioning
        if subject is not None:
            if hasattr(models, self.swagger_types['subject']):
                nested_class = getattr(models, self.swagger_types['subject'])
                if isinstance(subject, nested_class):
                    self.subject = subject
                elif isinstance(subject, dict):
                    self.subject = nested_class.from_kwargs(**subject)
                else:
                    self.subject = subject
            else:
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
        if issubclass(IdentityProviderPolicy, dict):
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
        if not isinstance(other, IdentityProviderPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
