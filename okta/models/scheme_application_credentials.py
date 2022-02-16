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
from okta.models.application_credentials import ApplicationCredentials  # noqa: F401,E501

import okta.models as models  # noqa
from okta.helpers import to_snake_case

class SchemeApplicationCredentials(ApplicationCredentials):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    if hasattr(ApplicationCredentials, "swagger_types"):
        swagger_types.update(ApplicationCredentials.swagger_types)
    swagger_types['password'] = 'PasswordCredential'
    swagger_types['reveal_password'] = 'bool'
    swagger_types['scheme'] = 'ApplicationCredentialsScheme'
    swagger_types['signing'] = 'ApplicationCredentialsSigning'
    swagger_types['user_name'] = 'str'

    attribute_map = {
        'password': 'password',
        'reveal_password': 'revealPassword',
        'scheme': 'scheme',
        'signing': 'signing',
        'user_name': 'userName'
    }
    if hasattr(ApplicationCredentials, "attribute_map"):
        attribute_map.update(ApplicationCredentials.attribute_map)

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
        else:
            config = {}
        self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, password=None, reveal_password=None, scheme=None, signing=None, user_name=None, **kwargs):  # noqa: E501
        """SchemeApplicationCredentials - a model defined in Swagger"""  # noqa: E501
        config = {}
        if kwargs is not None:
            config = {to_snake_case(key): value for key, value in kwargs.items()}
        super().set_attributes(**config)
        self._password = None
        self._reveal_password = None
        self._scheme = None
        self._signing = None
        self._user_name = None
        self.discriminator = None
        if password is not None:
            if hasattr(models, self.swagger_types['password']):
                nested_class = getattr(models, self.swagger_types['password'])
                if isinstance(password, nested_class):
                    self.password = password
                elif isinstance(password, dict):
                    self.password = nested_class.from_kwargs(**password)
                else:
                    self.password = password
            else:
                self.password = password
        if reveal_password is not None:
            if hasattr(models, self.swagger_types['reveal_password']):
                nested_class = getattr(models, self.swagger_types['reveal_password'])
                if isinstance(reveal_password, nested_class):
                    self.reveal_password = reveal_password
                elif isinstance(reveal_password, dict):
                    self.reveal_password = nested_class.from_kwargs(**reveal_password)
                else:
                    self.reveal_password = reveal_password
            else:
                self.reveal_password = reveal_password
        if scheme is not None:
            if hasattr(models, self.swagger_types['scheme']):
                nested_class = getattr(models, self.swagger_types['scheme'])
                if isinstance(scheme, nested_class):
                    self.scheme = scheme
                elif isinstance(scheme, dict):
                    self.scheme = nested_class.from_kwargs(**scheme)
                else:
                    self.scheme = scheme
            else:
                self.scheme = scheme
        if signing is not None:
            if hasattr(models, self.swagger_types['signing']):
                nested_class = getattr(models, self.swagger_types['signing'])
                if isinstance(signing, nested_class):
                    self.signing = signing
                elif isinstance(signing, dict):
                    self.signing = nested_class.from_kwargs(**signing)
                else:
                    self.signing = signing
            else:
                self.signing = signing
        if user_name is not None:
            if hasattr(models, self.swagger_types['user_name']):
                nested_class = getattr(models, self.swagger_types['user_name'])
                if isinstance(user_name, nested_class):
                    self.user_name = user_name
                elif isinstance(user_name, dict):
                    self.user_name = nested_class.from_kwargs(**user_name)
                else:
                    self.user_name = user_name
            else:
                self.user_name = user_name

    @property
    def password(self):
        """Gets the password of this SchemeApplicationCredentials.  # noqa: E501


        :return: The password of this SchemeApplicationCredentials.  # noqa: E501
        :rtype: PasswordCredential
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SchemeApplicationCredentials.


        :param password: The password of this SchemeApplicationCredentials.  # noqa: E501
        :type: PasswordCredential
        """

        self._password = password

    @property
    def reveal_password(self):
        """Gets the reveal_password of this SchemeApplicationCredentials.  # noqa: E501


        :return: The reveal_password of this SchemeApplicationCredentials.  # noqa: E501
        :rtype: bool
        """
        return self._reveal_password

    @reveal_password.setter
    def reveal_password(self, reveal_password):
        """Sets the reveal_password of this SchemeApplicationCredentials.


        :param reveal_password: The reveal_password of this SchemeApplicationCredentials.  # noqa: E501
        :type: bool
        """

        self._reveal_password = reveal_password

    @property
    def scheme(self):
        """Gets the scheme of this SchemeApplicationCredentials.  # noqa: E501


        :return: The scheme of this SchemeApplicationCredentials.  # noqa: E501
        :rtype: ApplicationCredentialsScheme
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this SchemeApplicationCredentials.


        :param scheme: The scheme of this SchemeApplicationCredentials.  # noqa: E501
        :type: ApplicationCredentialsScheme
        """

        self._scheme = scheme

    @property
    def signing(self):
        """Gets the signing of this SchemeApplicationCredentials.  # noqa: E501


        :return: The signing of this SchemeApplicationCredentials.  # noqa: E501
        :rtype: ApplicationCredentialsSigning
        """
        return self._signing

    @signing.setter
    def signing(self, signing):
        """Sets the signing of this SchemeApplicationCredentials.


        :param signing: The signing of this SchemeApplicationCredentials.  # noqa: E501
        :type: ApplicationCredentialsSigning
        """

        self._signing = signing

    @property
    def user_name(self):
        """Gets the user_name of this SchemeApplicationCredentials.  # noqa: E501


        :return: The user_name of this SchemeApplicationCredentials.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this SchemeApplicationCredentials.


        :param user_name: The user_name of this SchemeApplicationCredentials.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

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
        if issubclass(SchemeApplicationCredentials, dict):
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
        if not isinstance(other, SchemeApplicationCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
