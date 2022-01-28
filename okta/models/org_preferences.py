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

class OrgPreferences(object):
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
    swagger_types['show_end_user_footer'] = 'bool'

    attribute_map = {
        'links': '_links',
        'show_end_user_footer': 'showEndUserFooter'
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

    def set_attributes(self, links=None, show_end_user_footer=None, **kwargs):  # noqa: E501
        """OrgPreferences - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._show_end_user_footer = None
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
        if show_end_user_footer is not None:
            if hasattr(models, self.swagger_types['show_end_user_footer']):
                nested_class = getattr(models, self.swagger_types['show_end_user_footer'])
                if isinstance(show_end_user_footer, nested_class):
                    self.show_end_user_footer = show_end_user_footer
                elif isinstance(show_end_user_footer, dict):
                    self.show_end_user_footer = nested_class.from_kwargs(**show_end_user_footer)
                else:
                    self.show_end_user_footer = show_end_user_footer
            else:
                self.show_end_user_footer = show_end_user_footer

    @property
    def links(self):
        """Gets the links of this OrgPreferences.  # noqa: E501


        :return: The links of this OrgPreferences.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this OrgPreferences.


        :param links: The links of this OrgPreferences.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def show_end_user_footer(self):
        """Gets the show_end_user_footer of this OrgPreferences.  # noqa: E501


        :return: The show_end_user_footer of this OrgPreferences.  # noqa: E501
        :rtype: bool
        """
        return self._show_end_user_footer

    @show_end_user_footer.setter
    def show_end_user_footer(self, show_end_user_footer):
        """Sets the show_end_user_footer of this OrgPreferences.


        :param show_end_user_footer: The show_end_user_footer of this OrgPreferences.  # noqa: E501
        :type: bool
        """

        self._show_end_user_footer = show_end_user_footer

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
        if issubclass(OrgPreferences, dict):
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
        if not isinstance(other, OrgPreferences):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
