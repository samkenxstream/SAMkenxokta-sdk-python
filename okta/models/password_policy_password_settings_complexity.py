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

class PasswordPolicyPasswordSettingsComplexity(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    swagger_types['dictionary'] = 'PasswordDictionary'
    swagger_types['exclude_attributes'] = 'list[str]'
    swagger_types['exclude_username'] = 'bool'
    swagger_types['min_length'] = 'int'
    swagger_types['min_lower_case'] = 'int'
    swagger_types['min_number'] = 'int'
    swagger_types['min_symbol'] = 'int'
    swagger_types['min_upper_case'] = 'int'

    attribute_map = {
        'dictionary': 'dictionary',
        'exclude_attributes': 'excludeAttributes',
        'exclude_username': 'excludeUsername',
        'min_length': 'minLength',
        'min_lower_case': 'minLowerCase',
        'min_number': 'minNumber',
        'min_symbol': 'minSymbol',
        'min_upper_case': 'minUpperCase'
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

    def set_attributes(self, dictionary=None, exclude_attributes=None, exclude_username=True, min_length=None, min_lower_case=None, min_number=None, min_symbol=None, min_upper_case=None, **kwargs):  # noqa: E501
        """PasswordPolicyPasswordSettingsComplexity - a model defined in Swagger"""  # noqa: E501
        self._dictionary = None
        self._exclude_attributes = None
        self._exclude_username = None
        self._min_length = None
        self._min_lower_case = None
        self._min_number = None
        self._min_symbol = None
        self._min_upper_case = None
        self.discriminator = None
        if dictionary is not None:
            if hasattr(models, self.swagger_types['dictionary']):
                nested_class = getattr(models, self.swagger_types['dictionary'])
                if isinstance(dictionary, nested_class):
                    self.dictionary = dictionary
                elif isinstance(dictionary, dict):
                    self.dictionary = nested_class.from_kwargs(**dictionary)
                else:
                    self.dictionary = dictionary
            else:
                self.dictionary = dictionary
        if exclude_attributes is not None:
            if hasattr(models, self.swagger_types['exclude_attributes']):
                nested_class = getattr(models, self.swagger_types['exclude_attributes'])
                if isinstance(exclude_attributes, nested_class):
                    self.exclude_attributes = exclude_attributes
                elif isinstance(exclude_attributes, dict):
                    self.exclude_attributes = nested_class.from_kwargs(**exclude_attributes)
                else:
                    self.exclude_attributes = exclude_attributes
            else:
                self.exclude_attributes = exclude_attributes
        if exclude_username is not None:
            if hasattr(models, self.swagger_types['exclude_username']):
                nested_class = getattr(models, self.swagger_types['exclude_username'])
                if isinstance(exclude_username, nested_class):
                    self.exclude_username = exclude_username
                elif isinstance(exclude_username, dict):
                    self.exclude_username = nested_class.from_kwargs(**exclude_username)
                else:
                    self.exclude_username = exclude_username
            else:
                self.exclude_username = exclude_username
        if min_length is not None:
            if hasattr(models, self.swagger_types['min_length']):
                nested_class = getattr(models, self.swagger_types['min_length'])
                if isinstance(min_length, nested_class):
                    self.min_length = min_length
                elif isinstance(min_length, dict):
                    self.min_length = nested_class.from_kwargs(**min_length)
                else:
                    self.min_length = min_length
            else:
                self.min_length = min_length
        if min_lower_case is not None:
            if hasattr(models, self.swagger_types['min_lower_case']):
                nested_class = getattr(models, self.swagger_types['min_lower_case'])
                if isinstance(min_lower_case, nested_class):
                    self.min_lower_case = min_lower_case
                elif isinstance(min_lower_case, dict):
                    self.min_lower_case = nested_class.from_kwargs(**min_lower_case)
                else:
                    self.min_lower_case = min_lower_case
            else:
                self.min_lower_case = min_lower_case
        if min_number is not None:
            if hasattr(models, self.swagger_types['min_number']):
                nested_class = getattr(models, self.swagger_types['min_number'])
                if isinstance(min_number, nested_class):
                    self.min_number = min_number
                elif isinstance(min_number, dict):
                    self.min_number = nested_class.from_kwargs(**min_number)
                else:
                    self.min_number = min_number
            else:
                self.min_number = min_number
        if min_symbol is not None:
            if hasattr(models, self.swagger_types['min_symbol']):
                nested_class = getattr(models, self.swagger_types['min_symbol'])
                if isinstance(min_symbol, nested_class):
                    self.min_symbol = min_symbol
                elif isinstance(min_symbol, dict):
                    self.min_symbol = nested_class.from_kwargs(**min_symbol)
                else:
                    self.min_symbol = min_symbol
            else:
                self.min_symbol = min_symbol
        if min_upper_case is not None:
            if hasattr(models, self.swagger_types['min_upper_case']):
                nested_class = getattr(models, self.swagger_types['min_upper_case'])
                if isinstance(min_upper_case, nested_class):
                    self.min_upper_case = min_upper_case
                elif isinstance(min_upper_case, dict):
                    self.min_upper_case = nested_class.from_kwargs(**min_upper_case)
                else:
                    self.min_upper_case = min_upper_case
            else:
                self.min_upper_case = min_upper_case

    @property
    def dictionary(self):
        """Gets the dictionary of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501


        :return: The dictionary of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501
        :rtype: PasswordDictionary
        """
        return self._dictionary

    @dictionary.setter
    def dictionary(self, dictionary):
        """Sets the dictionary of this PasswordPolicyPasswordSettingsComplexity.


        :param dictionary: The dictionary of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501
        :type: PasswordDictionary
        """

        self._dictionary = dictionary

    @property
    def exclude_attributes(self):
        """Gets the exclude_attributes of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501


        :return: The exclude_attributes of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501
        :rtype: list[str]
        """
        return self._exclude_attributes

    @exclude_attributes.setter
    def exclude_attributes(self, exclude_attributes):
        """Sets the exclude_attributes of this PasswordPolicyPasswordSettingsComplexity.


        :param exclude_attributes: The exclude_attributes of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501
        :type: list[str]
        """

        self._exclude_attributes = exclude_attributes

    @property
    def exclude_username(self):
        """Gets the exclude_username of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501


        :return: The exclude_username of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_username

    @exclude_username.setter
    def exclude_username(self, exclude_username):
        """Sets the exclude_username of this PasswordPolicyPasswordSettingsComplexity.


        :param exclude_username: The exclude_username of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501
        :type: bool
        """

        self._exclude_username = exclude_username

    @property
    def min_length(self):
        """Gets the min_length of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501


        :return: The min_length of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501
        :rtype: int
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """Sets the min_length of this PasswordPolicyPasswordSettingsComplexity.


        :param min_length: The min_length of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501
        :type: int
        """

        self._min_length = min_length

    @property
    def min_lower_case(self):
        """Gets the min_lower_case of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501


        :return: The min_lower_case of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501
        :rtype: int
        """
        return self._min_lower_case

    @min_lower_case.setter
    def min_lower_case(self, min_lower_case):
        """Sets the min_lower_case of this PasswordPolicyPasswordSettingsComplexity.


        :param min_lower_case: The min_lower_case of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501
        :type: int
        """

        self._min_lower_case = min_lower_case

    @property
    def min_number(self):
        """Gets the min_number of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501


        :return: The min_number of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501
        :rtype: int
        """
        return self._min_number

    @min_number.setter
    def min_number(self, min_number):
        """Sets the min_number of this PasswordPolicyPasswordSettingsComplexity.


        :param min_number: The min_number of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501
        :type: int
        """

        self._min_number = min_number

    @property
    def min_symbol(self):
        """Gets the min_symbol of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501


        :return: The min_symbol of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501
        :rtype: int
        """
        return self._min_symbol

    @min_symbol.setter
    def min_symbol(self, min_symbol):
        """Sets the min_symbol of this PasswordPolicyPasswordSettingsComplexity.


        :param min_symbol: The min_symbol of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501
        :type: int
        """

        self._min_symbol = min_symbol

    @property
    def min_upper_case(self):
        """Gets the min_upper_case of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501


        :return: The min_upper_case of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501
        :rtype: int
        """
        return self._min_upper_case

    @min_upper_case.setter
    def min_upper_case(self, min_upper_case):
        """Sets the min_upper_case of this PasswordPolicyPasswordSettingsComplexity.


        :param min_upper_case: The min_upper_case of this PasswordPolicyPasswordSettingsComplexity.  # noqa: E501
        :type: int
        """

        self._min_upper_case = min_upper_case

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
        if issubclass(PasswordPolicyPasswordSettingsComplexity, dict):
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
        if not isinstance(other, PasswordPolicyPasswordSettingsComplexity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
