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

class IdentityProviderPolicyRuleCondition(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    swagger_types['idp_ids'] = 'list[str]'
    swagger_types['provider'] = 'IdentityProviderPolicyProvider'

    attribute_map = {
        'idp_ids': 'idpIds',
        'provider': 'provider'
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

    def set_attributes(self, idp_ids=None, provider=None, **kwargs):  # noqa: E501
        """IdentityProviderPolicyRuleCondition - a model defined in Swagger"""  # noqa: E501
        self._idp_ids = None
        self._provider = None
        self.discriminator = None
        if idp_ids is not None:
            if hasattr(models, self.swagger_types['idp_ids']):
                nested_class = getattr(models, self.swagger_types['idp_ids'])
                if isinstance(idp_ids, nested_class):
                    self.idp_ids = idp_ids
                elif isinstance(idp_ids, dict):
                    self.idp_ids = nested_class.from_kwargs(**idp_ids)
                else:
                    self.idp_ids = idp_ids
            else:
                self.idp_ids = idp_ids
        if provider is not None:
            if hasattr(models, self.swagger_types['provider']):
                nested_class = getattr(models, self.swagger_types['provider'])
                if isinstance(provider, nested_class):
                    self.provider = provider
                elif isinstance(provider, dict):
                    self.provider = nested_class.from_kwargs(**provider)
                else:
                    self.provider = provider
            else:
                self.provider = provider

    @property
    def idp_ids(self):
        """Gets the idp_ids of this IdentityProviderPolicyRuleCondition.  # noqa: E501


        :return: The idp_ids of this IdentityProviderPolicyRuleCondition.  # noqa: E501
        :rtype: list[str]
        """
        return self._idp_ids

    @idp_ids.setter
    def idp_ids(self, idp_ids):
        """Sets the idp_ids of this IdentityProviderPolicyRuleCondition.


        :param idp_ids: The idp_ids of this IdentityProviderPolicyRuleCondition.  # noqa: E501
        :type: list[str]
        """

        self._idp_ids = idp_ids

    @property
    def provider(self):
        """Gets the provider of this IdentityProviderPolicyRuleCondition.  # noqa: E501


        :return: The provider of this IdentityProviderPolicyRuleCondition.  # noqa: E501
        :rtype: IdentityProviderPolicyProvider
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this IdentityProviderPolicyRuleCondition.


        :param provider: The provider of this IdentityProviderPolicyRuleCondition.  # noqa: E501
        :type: IdentityProviderPolicyProvider
        """

        self._provider = provider

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
        if issubclass(IdentityProviderPolicyRuleCondition, dict):
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
        if not isinstance(other, IdentityProviderPolicyRuleCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
