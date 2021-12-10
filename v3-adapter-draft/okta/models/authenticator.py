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
    swagger_types = {
        'links': 'dict(str, object)',
        'created': 'datetime',
        'id': 'str',
        'key': 'str',
        'status': 'AuthenticatorStatus',
        'last_updated': 'datetime',
        'name': 'str',
        'type': 'AuthenticatorType',
        'settings': 'AuthenticatorSettings'
    }

    attribute_map = {
        'links': '_links',
        'created': 'created',
        'id': 'id',
        'key': 'key',
        'status': 'status',
        'last_updated': 'lastUpdated',
        'name': 'name',
        'type': 'type',
        'settings': 'settings'
    }

    def __init__(self, config=None):
        super().__init__(config)
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, links=None, created=None, id=None, key=None, status=None, last_updated=None, name=None, type=None, settings=None):  # noqa: E501
        """Authenticator - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._created = None
        self._id = None
        self._key = None
        self._status = None
        self._last_updated = None
        self._name = None
        self._type = None
        self._settings = None
        self.discriminator = None
        if links is not None:
            self.links = links
        if created is not None:
            self.created = created
        if id is not None:
            self.id = id
        if key is not None:
            self.key = key
        if status is not None:
            self.status = status
        if last_updated is not None:
            self.last_updated = last_updated
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if settings is not None:
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
