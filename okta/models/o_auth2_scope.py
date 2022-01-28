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

class OAuth2Scope(object):
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
    swagger_types['consent'] = 'OAuth2ScopeConsentType'
    swagger_types['default'] = 'bool'
    swagger_types['description'] = 'str'
    swagger_types['display_name'] = 'str'
    swagger_types['id'] = 'str'
    swagger_types['metadata_publish'] = 'OAuth2ScopeMetadataPublish'
    swagger_types['name'] = 'str'
    swagger_types['system'] = 'bool'

    attribute_map = {
        'consent': 'consent',
        'default': 'default',
        'description': 'description',
        'display_name': 'displayName',
        'id': 'id',
        'metadata_publish': 'metadataPublish',
        'name': 'name',
        'system': 'system'
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

    def set_attributes(self, consent=None, default=None, description=None, display_name=None, id=None, metadata_publish=None, name=None, system=None, **kwargs):  # noqa: E501
        """OAuth2Scope - a model defined in Swagger"""  # noqa: E501
        self._consent = None
        self._default = None
        self._description = None
        self._display_name = None
        self._id = None
        self._metadata_publish = None
        self._name = None
        self._system = None
        self.discriminator = None
        if consent is not None:
            if hasattr(models, self.swagger_types['consent']):
                nested_class = getattr(models, self.swagger_types['consent'])
                if isinstance(consent, nested_class):
                    self.consent = consent
                elif isinstance(consent, dict):
                    self.consent = nested_class.from_kwargs(**consent)
                else:
                    self.consent = consent
            else:
                self.consent = consent
        if default is not None:
            if hasattr(models, self.swagger_types['default']):
                nested_class = getattr(models, self.swagger_types['default'])
                if isinstance(default, nested_class):
                    self.default = default
                elif isinstance(default, dict):
                    self.default = nested_class.from_kwargs(**default)
                else:
                    self.default = default
            else:
                self.default = default
        if description is not None:
            if hasattr(models, self.swagger_types['description']):
                nested_class = getattr(models, self.swagger_types['description'])
                if isinstance(description, nested_class):
                    self.description = description
                elif isinstance(description, dict):
                    self.description = nested_class.from_kwargs(**description)
                else:
                    self.description = description
            else:
                self.description = description
        if display_name is not None:
            if hasattr(models, self.swagger_types['display_name']):
                nested_class = getattr(models, self.swagger_types['display_name'])
                if isinstance(display_name, nested_class):
                    self.display_name = display_name
                elif isinstance(display_name, dict):
                    self.display_name = nested_class.from_kwargs(**display_name)
                else:
                    self.display_name = display_name
            else:
                self.display_name = display_name
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
        if metadata_publish is not None:
            if hasattr(models, self.swagger_types['metadata_publish']):
                nested_class = getattr(models, self.swagger_types['metadata_publish'])
                if isinstance(metadata_publish, nested_class):
                    self.metadata_publish = metadata_publish
                elif isinstance(metadata_publish, dict):
                    self.metadata_publish = nested_class.from_kwargs(**metadata_publish)
                else:
                    self.metadata_publish = metadata_publish
            else:
                self.metadata_publish = metadata_publish
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
        if system is not None:
            if hasattr(models, self.swagger_types['system']):
                nested_class = getattr(models, self.swagger_types['system'])
                if isinstance(system, nested_class):
                    self.system = system
                elif isinstance(system, dict):
                    self.system = nested_class.from_kwargs(**system)
                else:
                    self.system = system
            else:
                self.system = system

    @property
    def consent(self):
        """Gets the consent of this OAuth2Scope.  # noqa: E501


        :return: The consent of this OAuth2Scope.  # noqa: E501
        :rtype: OAuth2ScopeConsentType
        """
        return self._consent

    @consent.setter
    def consent(self, consent):
        """Sets the consent of this OAuth2Scope.


        :param consent: The consent of this OAuth2Scope.  # noqa: E501
        :type: OAuth2ScopeConsentType
        """

        self._consent = consent

    @property
    def default(self):
        """Gets the default of this OAuth2Scope.  # noqa: E501


        :return: The default of this OAuth2Scope.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this OAuth2Scope.


        :param default: The default of this OAuth2Scope.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def description(self):
        """Gets the description of this OAuth2Scope.  # noqa: E501


        :return: The description of this OAuth2Scope.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OAuth2Scope.


        :param description: The description of this OAuth2Scope.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this OAuth2Scope.  # noqa: E501


        :return: The display_name of this OAuth2Scope.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this OAuth2Scope.


        :param display_name: The display_name of this OAuth2Scope.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this OAuth2Scope.  # noqa: E501


        :return: The id of this OAuth2Scope.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OAuth2Scope.


        :param id: The id of this OAuth2Scope.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def metadata_publish(self):
        """Gets the metadata_publish of this OAuth2Scope.  # noqa: E501


        :return: The metadata_publish of this OAuth2Scope.  # noqa: E501
        :rtype: OAuth2ScopeMetadataPublish
        """
        return self._metadata_publish

    @metadata_publish.setter
    def metadata_publish(self, metadata_publish):
        """Sets the metadata_publish of this OAuth2Scope.


        :param metadata_publish: The metadata_publish of this OAuth2Scope.  # noqa: E501
        :type: OAuth2ScopeMetadataPublish
        """

        self._metadata_publish = metadata_publish

    @property
    def name(self):
        """Gets the name of this OAuth2Scope.  # noqa: E501


        :return: The name of this OAuth2Scope.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OAuth2Scope.


        :param name: The name of this OAuth2Scope.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def system(self):
        """Gets the system of this OAuth2Scope.  # noqa: E501


        :return: The system of this OAuth2Scope.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this OAuth2Scope.


        :param system: The system of this OAuth2Scope.  # noqa: E501
        :type: bool
        """

        self._system = system

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
        if issubclass(OAuth2Scope, dict):
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
        if not isinstance(other, OAuth2Scope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
