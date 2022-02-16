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
from okta.models.email_content import EmailContent  # noqa: F401,E501

import okta.models as models  # noqa
from okta.helpers import to_snake_case

class EmailCustomization(EmailContent):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    if hasattr(EmailContent, "swagger_types"):
        swagger_types.update(EmailContent.swagger_types)
    swagger_types['id'] = 'str'
    swagger_types['created'] = 'datetime'
    swagger_types['last_updated'] = 'datetime'
    swagger_types['language'] = 'str'
    swagger_types['is_default'] = 'bool'
    swagger_types['links'] = 'EmailCustomizationLinks'

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'last_updated': 'lastUpdated',
        'language': 'language',
        'is_default': 'isDefault',
        'links': '_links'
    }
    if hasattr(EmailContent, "attribute_map"):
        attribute_map.update(EmailContent.attribute_map)

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
        else:
            config = {}
        self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, id=None, created=None, last_updated=None, language=None, is_default=None, links=None, **kwargs):  # noqa: E501
        """EmailCustomization - a model defined in Swagger"""  # noqa: E501
        config = {}
        if kwargs is not None:
            config = {to_snake_case(key): value for key, value in kwargs.items()}
        super().set_attributes(**config)
        self._id = None
        self._created = None
        self._last_updated = None
        self._language = None
        self._is_default = None
        self._links = None
        self.discriminator = None
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
        self.language = language
        if is_default is not None:
            if hasattr(models, self.swagger_types['is_default']):
                nested_class = getattr(models, self.swagger_types['is_default'])
                if isinstance(is_default, nested_class):
                    self.is_default = is_default
                elif isinstance(is_default, dict):
                    self.is_default = nested_class.from_kwargs(**is_default)
                else:
                    self.is_default = is_default
            else:
                self.is_default = is_default
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

    @property
    def id(self):
        """Gets the id of this EmailCustomization.  # noqa: E501


        :return: The id of this EmailCustomization.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EmailCustomization.


        :param id: The id of this EmailCustomization.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created(self):
        """Gets the created of this EmailCustomization.  # noqa: E501


        :return: The created of this EmailCustomization.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this EmailCustomization.


        :param created: The created of this EmailCustomization.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def last_updated(self):
        """Gets the last_updated of this EmailCustomization.  # noqa: E501


        :return: The last_updated of this EmailCustomization.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this EmailCustomization.


        :param last_updated: The last_updated of this EmailCustomization.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def language(self):
        """Gets the language of this EmailCustomization.  # noqa: E501

        unique under each email templage  # noqa: E501

        :return: The language of this EmailCustomization.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this EmailCustomization.

        unique under each email templage  # noqa: E501

        :param language: The language of this EmailCustomization.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def is_default(self):
        """Gets the is_default of this EmailCustomization.  # noqa: E501


        :return: The is_default of this EmailCustomization.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this EmailCustomization.


        :param is_default: The is_default of this EmailCustomization.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def links(self):
        """Gets the links of this EmailCustomization.  # noqa: E501


        :return: The links of this EmailCustomization.  # noqa: E501
        :rtype: EmailCustomizationLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this EmailCustomization.


        :param links: The links of this EmailCustomization.  # noqa: E501
        :type: EmailCustomizationLinks
        """

        self._links = links

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
        if issubclass(EmailCustomization, dict):
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
        if not isinstance(other, EmailCustomization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
