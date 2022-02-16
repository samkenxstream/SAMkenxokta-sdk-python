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

class ForgotPasswordResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    swagger_types['reset_password_url'] = 'str'

    attribute_map = {
        'reset_password_url': 'resetPasswordUrl'
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

    def set_attributes(self, reset_password_url=None, **kwargs):  # noqa: E501
        """ForgotPasswordResponse - a model defined in Swagger"""  # noqa: E501
        self._reset_password_url = None
        self.discriminator = None
        if reset_password_url is not None:
            if hasattr(models, self.swagger_types['reset_password_url']):
                nested_class = getattr(models, self.swagger_types['reset_password_url'])
                if isinstance(reset_password_url, nested_class):
                    self.reset_password_url = reset_password_url
                elif isinstance(reset_password_url, dict):
                    self.reset_password_url = nested_class.from_kwargs(**reset_password_url)
                else:
                    self.reset_password_url = reset_password_url
            else:
                self.reset_password_url = reset_password_url

    @property
    def reset_password_url(self):
        """Gets the reset_password_url of this ForgotPasswordResponse.  # noqa: E501


        :return: The reset_password_url of this ForgotPasswordResponse.  # noqa: E501
        :rtype: str
        """
        return self._reset_password_url

    @reset_password_url.setter
    def reset_password_url(self, reset_password_url):
        """Sets the reset_password_url of this ForgotPasswordResponse.


        :param reset_password_url: The reset_password_url of this ForgotPasswordResponse.  # noqa: E501
        :type: str
        """

        self._reset_password_url = reset_password_url

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
        if issubclass(ForgotPasswordResponse, dict):
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
        if not isinstance(other, ForgotPasswordResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
