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

class ProvisioningConnection(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    swagger_types['links'] = 'dict(str, object)'
    swagger_types['auth_scheme'] = 'ProvisioningConnectionAuthScheme'
    swagger_types['status'] = 'ProvisioningConnectionStatus'

    attribute_map = {
        'links': '_links',
        'auth_scheme': 'authScheme',
        'status': 'status'
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

    def set_attributes(self, links=None, auth_scheme=None, status=None, **kwargs):  # noqa: E501
        """ProvisioningConnection - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._auth_scheme = None
        self._status = None
        self.discriminator = None
        if links is not None:
            if hasattr(models, self.swagger_types['links']):
                nested_class = getattr(models, self.swagger_types['links'])
                if isinstance(links, nested_class):
                    self.links = links
                elif isinstance(links, dict):
                    self.links = nested_class.from_kwargs(**links)
                else:
                    self.links = links
            else:
                self.links = links
        if auth_scheme is not None:
            if hasattr(models, self.swagger_types['auth_scheme']):
                nested_class = getattr(models, self.swagger_types['auth_scheme'])
                if isinstance(auth_scheme, nested_class):
                    self.auth_scheme = auth_scheme
                elif isinstance(auth_scheme, dict):
                    self.auth_scheme = nested_class.from_kwargs(**auth_scheme)
                else:
                    self.auth_scheme = auth_scheme
            else:
                self.auth_scheme = auth_scheme
        if status is not None:
            if hasattr(models, self.swagger_types['status']):
                nested_class = getattr(models, self.swagger_types['status'])
                if isinstance(status, nested_class):
                    self.status = status
                elif isinstance(status, dict):
                    self.status = nested_class.from_kwargs(**status)
                else:
                    self.status = status
            else:
                self.status = status

    @property
    def links(self):
        """Gets the links of this ProvisioningConnection.  # noqa: E501


        :return: The links of this ProvisioningConnection.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ProvisioningConnection.


        :param links: The links of this ProvisioningConnection.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def auth_scheme(self):
        """Gets the auth_scheme of this ProvisioningConnection.  # noqa: E501


        :return: The auth_scheme of this ProvisioningConnection.  # noqa: E501
        :rtype: ProvisioningConnectionAuthScheme
        """
        return self._auth_scheme

    @auth_scheme.setter
    def auth_scheme(self, auth_scheme):
        """Sets the auth_scheme of this ProvisioningConnection.


        :param auth_scheme: The auth_scheme of this ProvisioningConnection.  # noqa: E501
        :type: ProvisioningConnectionAuthScheme
        """

        self._auth_scheme = auth_scheme

    @property
    def status(self):
        """Gets the status of this ProvisioningConnection.  # noqa: E501


        :return: The status of this ProvisioningConnection.  # noqa: E501
        :rtype: ProvisioningConnectionStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProvisioningConnection.


        :param status: The status of this ProvisioningConnection.  # noqa: E501
        :type: ProvisioningConnectionStatus
        """

        self._status = status

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
        if issubclass(ProvisioningConnection, dict):
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
        if not isinstance(other, ProvisioningConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
