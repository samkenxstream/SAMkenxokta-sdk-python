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

class SmsTemplate(object):
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
    swagger_types['created'] = 'datetime'
    swagger_types['id'] = 'str'
    swagger_types['last_updated'] = 'datetime'
    swagger_types['name'] = 'str'
    swagger_types['template'] = 'str'
    swagger_types['translations'] = 'SmsTemplateTranslations'
    swagger_types['type'] = 'SmsTemplateType'

    attribute_map = {
        'created': 'created',
        'id': 'id',
        'last_updated': 'lastUpdated',
        'name': 'name',
        'template': 'template',
        'translations': 'translations',
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

    def set_attributes(self, created=None, id=None, last_updated=None, name=None, template=None, translations=None, type=None, **kwargs):  # noqa: E501
        """SmsTemplate - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._id = None
        self._last_updated = None
        self._name = None
        self._template = None
        self._translations = None
        self._type = None
        self.discriminator = None
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
        if template is not None:
            if hasattr(models, self.swagger_types['template']):
                nested_class = getattr(models, self.swagger_types['template'])
                if isinstance(template, nested_class):
                    self.template = template
                elif isinstance(template, dict):
                    self.template = nested_class.from_kwargs(**template)
                else:
                    self.template = template
            else:
                self.template = template
        if translations is not None:
            if hasattr(models, self.swagger_types['translations']):
                nested_class = getattr(models, self.swagger_types['translations'])
                if isinstance(translations, nested_class):
                    self.translations = translations
                elif isinstance(translations, dict):
                    self.translations = nested_class.from_kwargs(**translations)
                else:
                    self.translations = translations
            else:
                self.translations = translations
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
    def created(self):
        """Gets the created of this SmsTemplate.  # noqa: E501


        :return: The created of this SmsTemplate.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SmsTemplate.


        :param created: The created of this SmsTemplate.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def id(self):
        """Gets the id of this SmsTemplate.  # noqa: E501


        :return: The id of this SmsTemplate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SmsTemplate.


        :param id: The id of this SmsTemplate.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_updated(self):
        """Gets the last_updated of this SmsTemplate.  # noqa: E501


        :return: The last_updated of this SmsTemplate.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this SmsTemplate.


        :param last_updated: The last_updated of this SmsTemplate.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def name(self):
        """Gets the name of this SmsTemplate.  # noqa: E501


        :return: The name of this SmsTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SmsTemplate.


        :param name: The name of this SmsTemplate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def template(self):
        """Gets the template of this SmsTemplate.  # noqa: E501


        :return: The template of this SmsTemplate.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this SmsTemplate.


        :param template: The template of this SmsTemplate.  # noqa: E501
        :type: str
        """

        self._template = template

    @property
    def translations(self):
        """Gets the translations of this SmsTemplate.  # noqa: E501


        :return: The translations of this SmsTemplate.  # noqa: E501
        :rtype: SmsTemplateTranslations
        """
        return self._translations

    @translations.setter
    def translations(self, translations):
        """Sets the translations of this SmsTemplate.


        :param translations: The translations of this SmsTemplate.  # noqa: E501
        :type: SmsTemplateTranslations
        """

        self._translations = translations

    @property
    def type(self):
        """Gets the type of this SmsTemplate.  # noqa: E501


        :return: The type of this SmsTemplate.  # noqa: E501
        :rtype: SmsTemplateType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SmsTemplate.


        :param type: The type of this SmsTemplate.  # noqa: E501
        :type: SmsTemplateType
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
        if issubclass(SmsTemplate, dict):
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
        if not isinstance(other, SmsTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
