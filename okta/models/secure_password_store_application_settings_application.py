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
from okta.models.application_settings_application import ApplicationSettingsApplication  # noqa: F401,E501

import okta.models as models  # noqa
from okta.helpers import to_snake_case

class SecurePasswordStoreApplicationSettingsApplication(ApplicationSettingsApplication):
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
    if hasattr(ApplicationSettingsApplication, "swagger_types"):
        swagger_types.update(ApplicationSettingsApplication.swagger_types)
    swagger_types['optional_field_1'] = 'str'
    swagger_types['optional_field_1_value'] = 'str'
    swagger_types['optional_field_2'] = 'str'
    swagger_types['optional_field_2_value'] = 'str'
    swagger_types['optional_field_3'] = 'str'
    swagger_types['optional_field_3_value'] = 'str'
    swagger_types['password_field'] = 'str'
    swagger_types['url'] = 'str'
    swagger_types['username_field'] = 'str'

    attribute_map = {
        'optional_field_1': 'optionalField1',
        'optional_field_1_value': 'optionalField1Value',
        'optional_field_2': 'optionalField2',
        'optional_field_2_value': 'optionalField2Value',
        'optional_field_3': 'optionalField3',
        'optional_field_3_value': 'optionalField3Value',
        'password_field': 'passwordField',
        'url': 'url',
        'username_field': 'usernameField'
    }
    if hasattr(ApplicationSettingsApplication, "attribute_map"):
        attribute_map.update(ApplicationSettingsApplication.attribute_map)

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
        else:
            config = {}
        self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, optional_field_1=None, optional_field_1_value=None, optional_field_2=None, optional_field_2_value=None, optional_field_3=None, optional_field_3_value=None, password_field=None, url=None, username_field=None, **kwargs):  # noqa: E501
        """SecurePasswordStoreApplicationSettingsApplication - a model defined in Swagger"""  # noqa: E501
        config = {}
        if kwargs is not None:
            config = {to_snake_case(key): value for key, value in kwargs.items()}
        super().set_attributes(**config)
        self._optional_field_1 = None
        self._optional_field_1_value = None
        self._optional_field_2 = None
        self._optional_field_2_value = None
        self._optional_field_3 = None
        self._optional_field_3_value = None
        self._password_field = None
        self._url = None
        self._username_field = None
        self.discriminator = None
        if optional_field_1 is not None:
            if hasattr(models, self.swagger_types['optional_field_1']):
                nested_class = getattr(models, self.swagger_types['optional_field_1'])
                if isinstance(optional_field_1, nested_class):
                    self.optional_field_1 = optional_field_1
                elif isinstance(optional_field_1, dict):
                    self.optional_field_1 = nested_class.from_kwargs(**optional_field_1)
                else:
                    self.optional_field_1 = optional_field_1
            else:
                self.optional_field_1 = optional_field_1
        if optional_field_1_value is not None:
            if hasattr(models, self.swagger_types['optional_field_1_value']):
                nested_class = getattr(models, self.swagger_types['optional_field_1_value'])
                if isinstance(optional_field_1_value, nested_class):
                    self.optional_field_1_value = optional_field_1_value
                elif isinstance(optional_field_1_value, dict):
                    self.optional_field_1_value = nested_class.from_kwargs(**optional_field_1_value)
                else:
                    self.optional_field_1_value = optional_field_1_value
            else:
                self.optional_field_1_value = optional_field_1_value
        if optional_field_2 is not None:
            if hasattr(models, self.swagger_types['optional_field_2']):
                nested_class = getattr(models, self.swagger_types['optional_field_2'])
                if isinstance(optional_field_2, nested_class):
                    self.optional_field_2 = optional_field_2
                elif isinstance(optional_field_2, dict):
                    self.optional_field_2 = nested_class.from_kwargs(**optional_field_2)
                else:
                    self.optional_field_2 = optional_field_2
            else:
                self.optional_field_2 = optional_field_2
        if optional_field_2_value is not None:
            if hasattr(models, self.swagger_types['optional_field_2_value']):
                nested_class = getattr(models, self.swagger_types['optional_field_2_value'])
                if isinstance(optional_field_2_value, nested_class):
                    self.optional_field_2_value = optional_field_2_value
                elif isinstance(optional_field_2_value, dict):
                    self.optional_field_2_value = nested_class.from_kwargs(**optional_field_2_value)
                else:
                    self.optional_field_2_value = optional_field_2_value
            else:
                self.optional_field_2_value = optional_field_2_value
        if optional_field_3 is not None:
            if hasattr(models, self.swagger_types['optional_field_3']):
                nested_class = getattr(models, self.swagger_types['optional_field_3'])
                if isinstance(optional_field_3, nested_class):
                    self.optional_field_3 = optional_field_3
                elif isinstance(optional_field_3, dict):
                    self.optional_field_3 = nested_class.from_kwargs(**optional_field_3)
                else:
                    self.optional_field_3 = optional_field_3
            else:
                self.optional_field_3 = optional_field_3
        if optional_field_3_value is not None:
            if hasattr(models, self.swagger_types['optional_field_3_value']):
                nested_class = getattr(models, self.swagger_types['optional_field_3_value'])
                if isinstance(optional_field_3_value, nested_class):
                    self.optional_field_3_value = optional_field_3_value
                elif isinstance(optional_field_3_value, dict):
                    self.optional_field_3_value = nested_class.from_kwargs(**optional_field_3_value)
                else:
                    self.optional_field_3_value = optional_field_3_value
            else:
                self.optional_field_3_value = optional_field_3_value
        if password_field is not None:
            if hasattr(models, self.swagger_types['password_field']):
                nested_class = getattr(models, self.swagger_types['password_field'])
                if isinstance(password_field, nested_class):
                    self.password_field = password_field
                elif isinstance(password_field, dict):
                    self.password_field = nested_class.from_kwargs(**password_field)
                else:
                    self.password_field = password_field
            else:
                self.password_field = password_field
        if url is not None:
            if hasattr(models, self.swagger_types['url']):
                nested_class = getattr(models, self.swagger_types['url'])
                if isinstance(url, nested_class):
                    self.url = url
                elif isinstance(url, dict):
                    self.url = nested_class.from_kwargs(**url)
                else:
                    self.url = url
            else:
                self.url = url
        if username_field is not None:
            if hasattr(models, self.swagger_types['username_field']):
                nested_class = getattr(models, self.swagger_types['username_field'])
                if isinstance(username_field, nested_class):
                    self.username_field = username_field
                elif isinstance(username_field, dict):
                    self.username_field = nested_class.from_kwargs(**username_field)
                else:
                    self.username_field = username_field
            else:
                self.username_field = username_field

    @property
    def optional_field_1(self):
        """Gets the optional_field_1 of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501


        :return: The optional_field_1 of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._optional_field_1

    @optional_field_1.setter
    def optional_field_1(self, optional_field_1):
        """Sets the optional_field_1 of this SecurePasswordStoreApplicationSettingsApplication.


        :param optional_field_1: The optional_field_1 of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._optional_field_1 = optional_field_1

    @property
    def optional_field_1_value(self):
        """Gets the optional_field_1_value of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501


        :return: The optional_field_1_value of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._optional_field_1_value

    @optional_field_1_value.setter
    def optional_field_1_value(self, optional_field_1_value):
        """Sets the optional_field_1_value of this SecurePasswordStoreApplicationSettingsApplication.


        :param optional_field_1_value: The optional_field_1_value of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._optional_field_1_value = optional_field_1_value

    @property
    def optional_field_2(self):
        """Gets the optional_field_2 of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501


        :return: The optional_field_2 of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._optional_field_2

    @optional_field_2.setter
    def optional_field_2(self, optional_field_2):
        """Sets the optional_field_2 of this SecurePasswordStoreApplicationSettingsApplication.


        :param optional_field_2: The optional_field_2 of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._optional_field_2 = optional_field_2

    @property
    def optional_field_2_value(self):
        """Gets the optional_field_2_value of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501


        :return: The optional_field_2_value of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._optional_field_2_value

    @optional_field_2_value.setter
    def optional_field_2_value(self, optional_field_2_value):
        """Sets the optional_field_2_value of this SecurePasswordStoreApplicationSettingsApplication.


        :param optional_field_2_value: The optional_field_2_value of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._optional_field_2_value = optional_field_2_value

    @property
    def optional_field_3(self):
        """Gets the optional_field_3 of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501


        :return: The optional_field_3 of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._optional_field_3

    @optional_field_3.setter
    def optional_field_3(self, optional_field_3):
        """Sets the optional_field_3 of this SecurePasswordStoreApplicationSettingsApplication.


        :param optional_field_3: The optional_field_3 of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._optional_field_3 = optional_field_3

    @property
    def optional_field_3_value(self):
        """Gets the optional_field_3_value of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501


        :return: The optional_field_3_value of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._optional_field_3_value

    @optional_field_3_value.setter
    def optional_field_3_value(self, optional_field_3_value):
        """Sets the optional_field_3_value of this SecurePasswordStoreApplicationSettingsApplication.


        :param optional_field_3_value: The optional_field_3_value of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._optional_field_3_value = optional_field_3_value

    @property
    def password_field(self):
        """Gets the password_field of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501


        :return: The password_field of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._password_field

    @password_field.setter
    def password_field(self, password_field):
        """Sets the password_field of this SecurePasswordStoreApplicationSettingsApplication.


        :param password_field: The password_field of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._password_field = password_field

    @property
    def url(self):
        """Gets the url of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501


        :return: The url of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SecurePasswordStoreApplicationSettingsApplication.


        :param url: The url of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def username_field(self):
        """Gets the username_field of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501


        :return: The username_field of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._username_field

    @username_field.setter
    def username_field(self, username_field):
        """Sets the username_field of this SecurePasswordStoreApplicationSettingsApplication.


        :param username_field: The username_field of this SecurePasswordStoreApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._username_field = username_field

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
        if issubclass(SecurePasswordStoreApplicationSettingsApplication, dict):
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
        if not isinstance(other, SecurePasswordStoreApplicationSettingsApplication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
