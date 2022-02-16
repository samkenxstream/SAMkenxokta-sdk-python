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
from okta.models.application_settings import ApplicationSettings  # noqa: F401,E501

import okta.models as models  # noqa
from okta.helpers import to_snake_case

class OpenIdConnectApplicationSettings(ApplicationSettings):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    if hasattr(ApplicationSettings, "swagger_types"):
        swagger_types.update(ApplicationSettings.swagger_types)
    swagger_types['oauth_client'] = 'OpenIdConnectApplicationSettingsClient'

    attribute_map = {
        'oauth_client': 'oauthClient'
    }
    if hasattr(ApplicationSettings, "attribute_map"):
        attribute_map.update(ApplicationSettings.attribute_map)

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
        else:
            config = {}
        self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, oauth_client=None, **kwargs):  # noqa: E501
        """OpenIdConnectApplicationSettings - a model defined in Swagger"""  # noqa: E501
        config = {}
        if kwargs is not None:
            config = {to_snake_case(key): value for key, value in kwargs.items()}
        super().set_attributes(**config)
        self._oauth_client = None
        self.discriminator = None
        if oauth_client is not None:
            if hasattr(models, self.swagger_types['oauth_client']):
                nested_class = getattr(models, self.swagger_types['oauth_client'])
                if isinstance(oauth_client, nested_class):
                    self.oauth_client = oauth_client
                elif isinstance(oauth_client, dict):
                    self.oauth_client = nested_class.from_kwargs(**oauth_client)
                else:
                    self.oauth_client = oauth_client
            else:
                self.oauth_client = oauth_client

    @property
    def oauth_client(self):
        """Gets the oauth_client of this OpenIdConnectApplicationSettings.  # noqa: E501


        :return: The oauth_client of this OpenIdConnectApplicationSettings.  # noqa: E501
        :rtype: OpenIdConnectApplicationSettingsClient
        """
        return self._oauth_client

    @oauth_client.setter
    def oauth_client(self, oauth_client):
        """Sets the oauth_client of this OpenIdConnectApplicationSettings.


        :param oauth_client: The oauth_client of this OpenIdConnectApplicationSettings.  # noqa: E501
        :type: OpenIdConnectApplicationSettingsClient
        """

        self._oauth_client = oauth_client

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
        if issubclass(OpenIdConnectApplicationSettings, dict):
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
        if not isinstance(other, OpenIdConnectApplicationSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
