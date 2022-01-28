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

class Group(object):
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
    swagger_types['embedded'] = 'dict(str, object)'
    swagger_types['links'] = 'dict(str, object)'
    swagger_types['created'] = 'datetime'
    swagger_types['id'] = 'str'
    swagger_types['last_membership_updated'] = 'datetime'
    swagger_types['last_updated'] = 'datetime'
    swagger_types['object_class'] = 'list[str]'
    swagger_types['profile'] = 'GroupProfile'
    swagger_types['type'] = 'GroupType'

    attribute_map = {
        'embedded': '_embedded',
        'links': '_links',
        'created': 'created',
        'id': 'id',
        'last_membership_updated': 'lastMembershipUpdated',
        'last_updated': 'lastUpdated',
        'object_class': 'objectClass',
        'profile': 'profile',
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

    def set_attributes(self, embedded=None, links=None, created=None, id=None, last_membership_updated=None, last_updated=None, object_class=None, profile=None, type=None, **kwargs):  # noqa: E501
        """Group - a model defined in Swagger"""  # noqa: E501
        self._embedded = None
        self._links = None
        self._created = None
        self._id = None
        self._last_membership_updated = None
        self._last_updated = None
        self._object_class = None
        self._profile = None
        self._type = None
        self.discriminator = None
        if embedded is not None:
            if hasattr(models, self.swagger_types['embedded']):
                nested_class = getattr(models, self.swagger_types['embedded'])
                if isinstance(embedded, nested_class):
                    self.embedded = embedded
                elif isinstance(embedded, dict):
                    self.embedded = nested_class.from_kwargs(**embedded)
                else:
                    self.embedded = embedded
            else:
                self.embedded = embedded
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
        if last_membership_updated is not None:
            if hasattr(models, self.swagger_types['last_membership_updated']):
                nested_class = getattr(models, self.swagger_types['last_membership_updated'])
                if isinstance(last_membership_updated, nested_class):
                    self.last_membership_updated = last_membership_updated
                elif isinstance(last_membership_updated, dict):
                    self.last_membership_updated = nested_class.from_kwargs(**last_membership_updated)
                else:
                    self.last_membership_updated = last_membership_updated
            else:
                self.last_membership_updated = last_membership_updated
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
        if object_class is not None:
            if hasattr(models, self.swagger_types['object_class']):
                nested_class = getattr(models, self.swagger_types['object_class'])
                if isinstance(object_class, nested_class):
                    self.object_class = object_class
                elif isinstance(object_class, dict):
                    self.object_class = nested_class.from_kwargs(**object_class)
                else:
                    self.object_class = object_class
            else:
                self.object_class = object_class
        if profile is not None:
            if hasattr(models, self.swagger_types['profile']):
                nested_class = getattr(models, self.swagger_types['profile'])
                if isinstance(profile, nested_class):
                    self.profile = profile
                elif isinstance(profile, dict):
                    self.profile = nested_class.from_kwargs(**profile)
                else:
                    self.profile = profile
            else:
                self.profile = profile
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
    def embedded(self):
        """Gets the embedded of this Group.  # noqa: E501


        :return: The embedded of this Group.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this Group.


        :param embedded: The embedded of this Group.  # noqa: E501
        :type: dict(str, object)
        """

        self._embedded = embedded

    @property
    def links(self):
        """Gets the links of this Group.  # noqa: E501


        :return: The links of this Group.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Group.


        :param links: The links of this Group.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def created(self):
        """Gets the created of this Group.  # noqa: E501


        :return: The created of this Group.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Group.


        :param created: The created of this Group.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def id(self):
        """Gets the id of this Group.  # noqa: E501


        :return: The id of this Group.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Group.


        :param id: The id of this Group.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_membership_updated(self):
        """Gets the last_membership_updated of this Group.  # noqa: E501


        :return: The last_membership_updated of this Group.  # noqa: E501
        :rtype: datetime
        """
        return self._last_membership_updated

    @last_membership_updated.setter
    def last_membership_updated(self, last_membership_updated):
        """Sets the last_membership_updated of this Group.


        :param last_membership_updated: The last_membership_updated of this Group.  # noqa: E501
        :type: datetime
        """

        self._last_membership_updated = last_membership_updated

    @property
    def last_updated(self):
        """Gets the last_updated of this Group.  # noqa: E501


        :return: The last_updated of this Group.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this Group.


        :param last_updated: The last_updated of this Group.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def object_class(self):
        """Gets the object_class of this Group.  # noqa: E501


        :return: The object_class of this Group.  # noqa: E501
        :rtype: list[str]
        """
        return self._object_class

    @object_class.setter
    def object_class(self, object_class):
        """Sets the object_class of this Group.


        :param object_class: The object_class of this Group.  # noqa: E501
        :type: list[str]
        """

        self._object_class = object_class

    @property
    def profile(self):
        """Gets the profile of this Group.  # noqa: E501


        :return: The profile of this Group.  # noqa: E501
        :rtype: GroupProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this Group.


        :param profile: The profile of this Group.  # noqa: E501
        :type: GroupProfile
        """

        self._profile = profile

    @property
    def type(self):
        """Gets the type of this Group.  # noqa: E501


        :return: The type of this Group.  # noqa: E501
        :rtype: GroupType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Group.


        :param type: The type of this Group.  # noqa: E501
        :type: GroupType
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
        if issubclass(Group, dict):
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
        if not isinstance(other, Group):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
