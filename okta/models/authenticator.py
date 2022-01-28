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

class Authenticator(object):
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
    swagger_types['links'] = 'dict(str, object)'
    swagger_types['created'] = 'datetime'
    swagger_types['id'] = 'str'
    swagger_types['key'] = 'str'
    swagger_types['status'] = 'AuthenticatorStatus'
    swagger_types['last_updated'] = 'datetime'
    swagger_types['name'] = 'str'
    swagger_types['provider'] = 'AuthenticatorProvider'
    swagger_types['type'] = 'AuthenticatorType'
    swagger_types['settings'] = 'AuthenticatorSettings'

    attribute_map = {
        'links': '_links',
        'created': 'created',
        'id': 'id',
        'key': 'key',
        'status': 'status',
        'last_updated': 'lastUpdated',
        'name': 'name',
        'provider': 'provider',
        'type': 'type',
        'settings': 'settings'
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

    def set_attributes(self, links=None, created=None, id=None, key=None, status=None, last_updated=None, name=None, provider=None, type=None, settings=None, **kwargs):  # noqa: E501
        """Authenticator - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._created = None
        self._id = None
        self._key = None
        self._status = None
        self._last_updated = None
        self._name = None
        self._provider = None
        self._type = None
        self._settings = None
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
        if created is not None:
            if hasattr(models, self.swagger_types['created']):
                nested_class = getattr(models, self.swagger_types['created'])
                if isinstance(created, nested_class):
                    self.created = created
                elif isinstance(created, dict):
                    self.created = nested_class.from_kwargs(**created)
                else:
                    self.created = created
            else:
                self.created = created
        if id is not None:
            if hasattr(models, self.swagger_types['id']):
                nested_class = getattr(models, self.swagger_types['id'])
                if isinstance(id, nested_class):
                    self.id = id
                elif isinstance(id, dict):
                    self.id = nested_class.from_kwargs(**id)
                else:
                    self.id = id
            else:
                self.id = id
        if key is not None:
            if hasattr(models, self.swagger_types['key']):
                nested_class = getattr(models, self.swagger_types['key'])
                if isinstance(key, nested_class):
                    self.key = key
                elif isinstance(key, dict):
                    self.key = nested_class.from_kwargs(**key)
                else:
                    self.key = key
            else:
                self.key = key
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
        if last_updated is not None:
            if hasattr(models, self.swagger_types['last_updated']):
                nested_class = getattr(models, self.swagger_types['last_updated'])
                if isinstance(last_updated, nested_class):
                    self.last_updated = last_updated
                elif isinstance(last_updated, dict):
                    self.last_updated = nested_class.from_kwargs(**last_updated)
                else:
                    self.last_updated = last_updated
            else:
                self.last_updated = last_updated
        if name is not None:
            if hasattr(models, self.swagger_types['name']):
                nested_class = getattr(models, self.swagger_types['name'])
                if isinstance(name, nested_class):
                    self.name = name
                elif isinstance(name, dict):
                    self.name = nested_class.from_kwargs(**name)
                else:
                    self.name = name
            else:
                self.name = name
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
        if type is not None:
            if hasattr(models, self.swagger_types['type']):
                nested_class = getattr(models, self.swagger_types['type'])
                if isinstance(type, nested_class):
                    self.type = type
                elif isinstance(type, dict):
                    self.type = nested_class.from_kwargs(**type)
                else:
                    self.type = type
            else:
                self.type = type
        if settings is not None:
            if hasattr(models, self.swagger_types['settings']):
                nested_class = getattr(models, self.swagger_types['settings'])
                if isinstance(settings, nested_class):
                    self.settings = settings
                elif isinstance(settings, dict):
                    self.settings = nested_class.from_kwargs(**settings)
                else:
                    self.settings = settings
            else:
                self.settings = settings

    @property
    def links(self):
        """Gets the links of this Authenticator.  # noqa: E501


        :return: The links of this Authenticator.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Authenticator.


        :param links: The links of this Authenticator.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def created(self):
        """Gets the created of this Authenticator.  # noqa: E501


        :return: The created of this Authenticator.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Authenticator.


        :param created: The created of this Authenticator.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def id(self):
        """Gets the id of this Authenticator.  # noqa: E501


        :return: The id of this Authenticator.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Authenticator.


        :param id: The id of this Authenticator.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def key(self):
        """Gets the key of this Authenticator.  # noqa: E501


        :return: The key of this Authenticator.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Authenticator.


        :param key: The key of this Authenticator.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def status(self):
        """Gets the status of this Authenticator.  # noqa: E501


        :return: The status of this Authenticator.  # noqa: E501
        :rtype: AuthenticatorStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Authenticator.


        :param status: The status of this Authenticator.  # noqa: E501
        :type: AuthenticatorStatus
        """

        self._status = status

    @property
    def last_updated(self):
        """Gets the last_updated of this Authenticator.  # noqa: E501


        :return: The last_updated of this Authenticator.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this Authenticator.


        :param last_updated: The last_updated of this Authenticator.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def name(self):
        """Gets the name of this Authenticator.  # noqa: E501


        :return: The name of this Authenticator.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Authenticator.


        :param name: The name of this Authenticator.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def provider(self):
        """Gets the provider of this Authenticator.  # noqa: E501


        :return: The provider of this Authenticator.  # noqa: E501
        :rtype: AuthenticatorProvider
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this Authenticator.


        :param provider: The provider of this Authenticator.  # noqa: E501
        :type: AuthenticatorProvider
        """

        self._provider = provider

    @property
    def type(self):
        """Gets the type of this Authenticator.  # noqa: E501


        :return: The type of this Authenticator.  # noqa: E501
        :rtype: AuthenticatorType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Authenticator.


        :param type: The type of this Authenticator.  # noqa: E501
        :type: AuthenticatorType
        """

        self._type = type

    @property
    def settings(self):
        """Gets the settings of this Authenticator.  # noqa: E501


        :return: The settings of this Authenticator.  # noqa: E501
        :rtype: AuthenticatorSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this Authenticator.


        :param settings: The settings of this Authenticator.  # noqa: E501
        :type: AuthenticatorSettings
        """

        self._settings = settings

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
        if issubclass(Authenticator, dict):
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
        if not isinstance(other, Authenticator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
