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

class EmailTemplateLinks(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    swagger_types['_self'] = 'HrefObject'
    swagger_types['customizations'] = 'HrefObject'
    swagger_types['default_content'] = 'HrefObject'
    swagger_types['test'] = 'HrefObject'

    attribute_map = {
        '_self': 'self',
        'customizations': 'customizations',
        'default_content': 'defaultContent',
        'test': 'test'
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

    def set_attributes(self, _self=None, customizations=None, default_content=None, test=None, **kwargs):  # noqa: E501
        """EmailTemplateLinks - a model defined in Swagger"""  # noqa: E501
        self.__self = None
        self._customizations = None
        self._default_content = None
        self._test = None
        self.discriminator = None
        if _self is not None:
            if hasattr(models, self.swagger_types['_self']):
                nested_class = getattr(models, self.swagger_types['_self'])
                if isinstance(_self, nested_class):
                    self._self = _self
                elif isinstance(_self, dict):
                    self._self = nested_class.from_kwargs(**_self)
                else:
                    self._self = _self
            else:
                self._self = _self
        if customizations is not None:
            if hasattr(models, self.swagger_types['customizations']):
                nested_class = getattr(models, self.swagger_types['customizations'])
                if isinstance(customizations, nested_class):
                    self.customizations = customizations
                elif isinstance(customizations, dict):
                    self.customizations = nested_class.from_kwargs(**customizations)
                else:
                    self.customizations = customizations
            else:
                self.customizations = customizations
        if default_content is not None:
            if hasattr(models, self.swagger_types['default_content']):
                nested_class = getattr(models, self.swagger_types['default_content'])
                if isinstance(default_content, nested_class):
                    self.default_content = default_content
                elif isinstance(default_content, dict):
                    self.default_content = nested_class.from_kwargs(**default_content)
                else:
                    self.default_content = default_content
            else:
                self.default_content = default_content
        if test is not None:
            if hasattr(models, self.swagger_types['test']):
                nested_class = getattr(models, self.swagger_types['test'])
                if isinstance(test, nested_class):
                    self.test = test
                elif isinstance(test, dict):
                    self.test = nested_class.from_kwargs(**test)
                else:
                    self.test = test
            else:
                self.test = test

    @property
    def _self(self):
        """Gets the _self of this EmailTemplateLinks.  # noqa: E501


        :return: The _self of this EmailTemplateLinks.  # noqa: E501
        :rtype: HrefObject
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this EmailTemplateLinks.


        :param _self: The _self of this EmailTemplateLinks.  # noqa: E501
        :type: HrefObject
        """

        self.__self = _self

    @property
    def customizations(self):
        """Gets the customizations of this EmailTemplateLinks.  # noqa: E501


        :return: The customizations of this EmailTemplateLinks.  # noqa: E501
        :rtype: HrefObject
        """
        return self._customizations

    @customizations.setter
    def customizations(self, customizations):
        """Sets the customizations of this EmailTemplateLinks.


        :param customizations: The customizations of this EmailTemplateLinks.  # noqa: E501
        :type: HrefObject
        """

        self._customizations = customizations

    @property
    def default_content(self):
        """Gets the default_content of this EmailTemplateLinks.  # noqa: E501


        :return: The default_content of this EmailTemplateLinks.  # noqa: E501
        :rtype: HrefObject
        """
        return self._default_content

    @default_content.setter
    def default_content(self, default_content):
        """Sets the default_content of this EmailTemplateLinks.


        :param default_content: The default_content of this EmailTemplateLinks.  # noqa: E501
        :type: HrefObject
        """

        self._default_content = default_content

    @property
    def test(self):
        """Gets the test of this EmailTemplateLinks.  # noqa: E501


        :return: The test of this EmailTemplateLinks.  # noqa: E501
        :rtype: HrefObject
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this EmailTemplateLinks.


        :param test: The test of this EmailTemplateLinks.  # noqa: E501
        :type: HrefObject
        """

        self._test = test

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
        if issubclass(EmailTemplateLinks, dict):
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
        if not isinstance(other, EmailTemplateLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
