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

class EmailPreviewLinks(object):
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
    swagger_types['content_source'] = 'HrefObject'
    swagger_types['template'] = 'HrefObject'
    swagger_types['test'] = 'HrefObject'

    attribute_map = {
        '_self': 'self',
        'content_source': 'contentSource',
        'template': 'template',
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

    def set_attributes(self, _self=None, content_source=None, template=None, test=None, **kwargs):  # noqa: E501
        """EmailPreviewLinks - a model defined in Swagger"""  # noqa: E501
        self.__self = None
        self._content_source = None
        self._template = None
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
        if content_source is not None:
            if hasattr(models, self.swagger_types['content_source']):
                nested_class = getattr(models, self.swagger_types['content_source'])
                if isinstance(content_source, nested_class):
                    self.content_source = content_source
                elif isinstance(content_source, dict):
                    self.content_source = nested_class.from_kwargs(**content_source)
                else:
                    self.content_source = content_source
            else:
                self.content_source = content_source
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
        """Gets the _self of this EmailPreviewLinks.  # noqa: E501


        :return: The _self of this EmailPreviewLinks.  # noqa: E501
        :rtype: HrefObject
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this EmailPreviewLinks.


        :param _self: The _self of this EmailPreviewLinks.  # noqa: E501
        :type: HrefObject
        """

        self.__self = _self

    @property
    def content_source(self):
        """Gets the content_source of this EmailPreviewLinks.  # noqa: E501


        :return: The content_source of this EmailPreviewLinks.  # noqa: E501
        :rtype: HrefObject
        """
        return self._content_source

    @content_source.setter
    def content_source(self, content_source):
        """Sets the content_source of this EmailPreviewLinks.


        :param content_source: The content_source of this EmailPreviewLinks.  # noqa: E501
        :type: HrefObject
        """

        self._content_source = content_source

    @property
    def template(self):
        """Gets the template of this EmailPreviewLinks.  # noqa: E501


        :return: The template of this EmailPreviewLinks.  # noqa: E501
        :rtype: HrefObject
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this EmailPreviewLinks.


        :param template: The template of this EmailPreviewLinks.  # noqa: E501
        :type: HrefObject
        """

        self._template = template

    @property
    def test(self):
        """Gets the test of this EmailPreviewLinks.  # noqa: E501


        :return: The test of this EmailPreviewLinks.  # noqa: E501
        :rtype: HrefObject
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this EmailPreviewLinks.


        :param test: The test of this EmailPreviewLinks.  # noqa: E501
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
        if issubclass(EmailPreviewLinks, dict):
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
        if not isinstance(other, EmailPreviewLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
