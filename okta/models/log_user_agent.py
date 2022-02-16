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

class LogUserAgent(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    swagger_types['browser'] = 'str'
    swagger_types['os'] = 'str'
    swagger_types['raw_user_agent'] = 'str'

    attribute_map = {
        'browser': 'browser',
        'os': 'os',
        'raw_user_agent': 'rawUserAgent'
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

    def set_attributes(self, browser=None, os=None, raw_user_agent=None, **kwargs):  # noqa: E501
        """LogUserAgent - a model defined in Swagger"""  # noqa: E501
        self._browser = None
        self._os = None
        self._raw_user_agent = None
        self.discriminator = None
        if browser is not None:
            if hasattr(models, self.swagger_types['browser']):
                nested_class = getattr(models, self.swagger_types['browser'])
                if isinstance(browser, nested_class):
                    self.browser = browser
                elif isinstance(browser, dict):
                    self.browser = nested_class.from_kwargs(**browser)
                else:
                    self.browser = browser
            else:
                self.browser = browser
        if os is not None:
            if hasattr(models, self.swagger_types['os']):
                nested_class = getattr(models, self.swagger_types['os'])
                if isinstance(os, nested_class):
                    self.os = os
                elif isinstance(os, dict):
                    self.os = nested_class.from_kwargs(**os)
                else:
                    self.os = os
            else:
                self.os = os
        if raw_user_agent is not None:
            if hasattr(models, self.swagger_types['raw_user_agent']):
                nested_class = getattr(models, self.swagger_types['raw_user_agent'])
                if isinstance(raw_user_agent, nested_class):
                    self.raw_user_agent = raw_user_agent
                elif isinstance(raw_user_agent, dict):
                    self.raw_user_agent = nested_class.from_kwargs(**raw_user_agent)
                else:
                    self.raw_user_agent = raw_user_agent
            else:
                self.raw_user_agent = raw_user_agent

    @property
    def browser(self):
        """Gets the browser of this LogUserAgent.  # noqa: E501


        :return: The browser of this LogUserAgent.  # noqa: E501
        :rtype: str
        """
        return self._browser

    @browser.setter
    def browser(self, browser):
        """Sets the browser of this LogUserAgent.


        :param browser: The browser of this LogUserAgent.  # noqa: E501
        :type: str
        """

        self._browser = browser

    @property
    def os(self):
        """Gets the os of this LogUserAgent.  # noqa: E501


        :return: The os of this LogUserAgent.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this LogUserAgent.


        :param os: The os of this LogUserAgent.  # noqa: E501
        :type: str
        """

        self._os = os

    @property
    def raw_user_agent(self):
        """Gets the raw_user_agent of this LogUserAgent.  # noqa: E501


        :return: The raw_user_agent of this LogUserAgent.  # noqa: E501
        :rtype: str
        """
        return self._raw_user_agent

    @raw_user_agent.setter
    def raw_user_agent(self, raw_user_agent):
        """Sets the raw_user_agent of this LogUserAgent.


        :param raw_user_agent: The raw_user_agent of this LogUserAgent.  # noqa: E501
        :type: str
        """

        self._raw_user_agent = raw_user_agent

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
        if issubclass(LogUserAgent, dict):
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
        if not isinstance(other, LogUserAgent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
