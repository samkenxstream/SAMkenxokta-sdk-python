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

class AppUserCredentials(object):
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
        'password': 'AppUserPasswordCredential',
        'user_name': 'str'
    }

    attribute_map = {
        'password': 'password',
        'user_name': 'userName'
    }

    def __init__(self, config=None):
        super().__init__(config)
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, password=None, user_name=None):  # noqa: E501
        """AppUserCredentials - a model defined in Swagger"""  # noqa: E501
        self._password = None
        self._user_name = None
        self.discriminator = None
        if password is not None:
            self.password = password
        if user_name is not None:
            self.user_name = user_name

    @property
    def password(self):
        """Gets the password of this AppUserCredentials.  # noqa: E501


        :return: The password of this AppUserCredentials.  # noqa: E501
        :rtype: AppUserPasswordCredential
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AppUserCredentials.


        :param password: The password of this AppUserCredentials.  # noqa: E501
        :type: AppUserPasswordCredential
        """

        self._password = password

    @property
    def user_name(self):
        """Gets the user_name of this AppUserCredentials.  # noqa: E501


        :return: The user_name of this AppUserCredentials.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this AppUserCredentials.


        :param user_name: The user_name of this AppUserCredentials.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

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
        if issubclass(AppUserCredentials, dict):
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
        if not isinstance(other, AppUserCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
