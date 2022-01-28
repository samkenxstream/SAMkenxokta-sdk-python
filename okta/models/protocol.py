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

class Protocol(object):
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
    swagger_types['algorithms'] = 'ProtocolAlgorithms'
    swagger_types['credentials'] = 'IdentityProviderCredentials'
    swagger_types['endpoints'] = 'ProtocolEndpoints'
    swagger_types['issuer'] = 'ProtocolEndpoint'
    swagger_types['relay_state'] = 'ProtocolRelayState'
    swagger_types['scopes'] = 'list[str]'
    swagger_types['settings'] = 'ProtocolSettings'
    swagger_types['type'] = 'ProtocolType'

    attribute_map = {
        'algorithms': 'algorithms',
        'credentials': 'credentials',
        'endpoints': 'endpoints',
        'issuer': 'issuer',
        'relay_state': 'relayState',
        'scopes': 'scopes',
        'settings': 'settings',
        'type': 'type'
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

    def set_attributes(self, algorithms=None, credentials=None, endpoints=None, issuer=None, relay_state=None, scopes=None, settings=None, type=None, **kwargs):  # noqa: E501
        """Protocol - a model defined in Swagger"""  # noqa: E501
        self._algorithms = None
        self._credentials = None
        self._endpoints = None
        self._issuer = None
        self._relay_state = None
        self._scopes = None
        self._settings = None
        self._type = None
        self.discriminator = None
        if algorithms is not None:
            if hasattr(models, self.swagger_types['algorithms']):
                nested_class = getattr(models, self.swagger_types['algorithms'])
                if isinstance(algorithms, nested_class):
                    self.algorithms = algorithms
                elif isinstance(algorithms, dict):
                    self.algorithms = nested_class.from_kwargs(**algorithms)
                else:
                    self.algorithms = algorithms
            else:
                self.algorithms = algorithms
        if credentials is not None:
            if hasattr(models, self.swagger_types['credentials']):
                nested_class = getattr(models, self.swagger_types['credentials'])
                if isinstance(credentials, nested_class):
                    self.credentials = credentials
                elif isinstance(credentials, dict):
                    self.credentials = nested_class.from_kwargs(**credentials)
                else:
                    self.credentials = credentials
            else:
                self.credentials = credentials
        if endpoints is not None:
            if hasattr(models, self.swagger_types['endpoints']):
                nested_class = getattr(models, self.swagger_types['endpoints'])
                if isinstance(endpoints, nested_class):
                    self.endpoints = endpoints
                elif isinstance(endpoints, dict):
                    self.endpoints = nested_class.from_kwargs(**endpoints)
                else:
                    self.endpoints = endpoints
            else:
                self.endpoints = endpoints
        if issuer is not None:
            if hasattr(models, self.swagger_types['issuer']):
                nested_class = getattr(models, self.swagger_types['issuer'])
                if isinstance(issuer, nested_class):
                    self.issuer = issuer
                elif isinstance(issuer, dict):
                    self.issuer = nested_class.from_kwargs(**issuer)
                else:
                    self.issuer = issuer
            else:
                self.issuer = issuer
        if relay_state is not None:
            if hasattr(models, self.swagger_types['relay_state']):
                nested_class = getattr(models, self.swagger_types['relay_state'])
                if isinstance(relay_state, nested_class):
                    self.relay_state = relay_state
                elif isinstance(relay_state, dict):
                    self.relay_state = nested_class.from_kwargs(**relay_state)
                else:
                    self.relay_state = relay_state
            else:
                self.relay_state = relay_state
        if scopes is not None:
            if hasattr(models, self.swagger_types['scopes']):
                nested_class = getattr(models, self.swagger_types['scopes'])
                if isinstance(scopes, nested_class):
                    self.scopes = scopes
                elif isinstance(scopes, dict):
                    self.scopes = nested_class.from_kwargs(**scopes)
                else:
                    self.scopes = scopes
            else:
                self.scopes = scopes
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

    @property
    def algorithms(self):
        """Gets the algorithms of this Protocol.  # noqa: E501


        :return: The algorithms of this Protocol.  # noqa: E501
        :rtype: ProtocolAlgorithms
        """
        return self._algorithms

    @algorithms.setter
    def algorithms(self, algorithms):
        """Sets the algorithms of this Protocol.


        :param algorithms: The algorithms of this Protocol.  # noqa: E501
        :type: ProtocolAlgorithms
        """

        self._algorithms = algorithms

    @property
    def credentials(self):
        """Gets the credentials of this Protocol.  # noqa: E501


        :return: The credentials of this Protocol.  # noqa: E501
        :rtype: IdentityProviderCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this Protocol.


        :param credentials: The credentials of this Protocol.  # noqa: E501
        :type: IdentityProviderCredentials
        """

        self._credentials = credentials

    @property
    def endpoints(self):
        """Gets the endpoints of this Protocol.  # noqa: E501


        :return: The endpoints of this Protocol.  # noqa: E501
        :rtype: ProtocolEndpoints
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this Protocol.


        :param endpoints: The endpoints of this Protocol.  # noqa: E501
        :type: ProtocolEndpoints
        """

        self._endpoints = endpoints

    @property
    def issuer(self):
        """Gets the issuer of this Protocol.  # noqa: E501


        :return: The issuer of this Protocol.  # noqa: E501
        :rtype: ProtocolEndpoint
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this Protocol.


        :param issuer: The issuer of this Protocol.  # noqa: E501
        :type: ProtocolEndpoint
        """

        self._issuer = issuer

    @property
    def relay_state(self):
        """Gets the relay_state of this Protocol.  # noqa: E501


        :return: The relay_state of this Protocol.  # noqa: E501
        :rtype: ProtocolRelayState
        """
        return self._relay_state

    @relay_state.setter
    def relay_state(self, relay_state):
        """Sets the relay_state of this Protocol.


        :param relay_state: The relay_state of this Protocol.  # noqa: E501
        :type: ProtocolRelayState
        """

        self._relay_state = relay_state

    @property
    def scopes(self):
        """Gets the scopes of this Protocol.  # noqa: E501


        :return: The scopes of this Protocol.  # noqa: E501
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this Protocol.


        :param scopes: The scopes of this Protocol.  # noqa: E501
        :type: list[str]
        """

        self._scopes = scopes

    @property
    def settings(self):
        """Gets the settings of this Protocol.  # noqa: E501


        :return: The settings of this Protocol.  # noqa: E501
        :rtype: ProtocolSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this Protocol.


        :param settings: The settings of this Protocol.  # noqa: E501
        :type: ProtocolSettings
        """

        self._settings = settings

    @property
    def type(self):
        """Gets the type of this Protocol.  # noqa: E501


        :return: The type of this Protocol.  # noqa: E501
        :rtype: ProtocolType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Protocol.


        :param type: The type of this Protocol.  # noqa: E501
        :type: ProtocolType
        """

        self._type = type

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
        if issubclass(Protocol, dict):
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
        if not isinstance(other, Protocol):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
