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

class PasswordCredentialHash(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    swagger_types['algorithm'] = 'PasswordCredentialHashAlgorithm'
    swagger_types['salt'] = 'str'
    swagger_types['salt_order'] = 'str'
    swagger_types['value'] = 'str'
    swagger_types['work_factor'] = 'int'

    attribute_map = {
        'algorithm': 'algorithm',
        'salt': 'salt',
        'salt_order': 'saltOrder',
        'value': 'value',
        'work_factor': 'workFactor'
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

    def set_attributes(self, algorithm=None, salt=None, salt_order=None, value=None, work_factor=None, **kwargs):  # noqa: E501
        """PasswordCredentialHash - a model defined in Swagger"""  # noqa: E501
        self._algorithm = None
        self._salt = None
        self._salt_order = None
        self._value = None
        self._work_factor = None
        self.discriminator = None
        if algorithm is not None:
            if hasattr(models, self.swagger_types['algorithm']):
                nested_class = getattr(models, self.swagger_types['algorithm'])
                if isinstance(algorithm, nested_class):
                    self.algorithm = algorithm
                elif isinstance(algorithm, dict):
                    self.algorithm = nested_class.from_kwargs(**algorithm)
                else:
                    self.algorithm = algorithm
            else:
                self.algorithm = algorithm
        if salt is not None:
            if hasattr(models, self.swagger_types['salt']):
                nested_class = getattr(models, self.swagger_types['salt'])
                if isinstance(salt, nested_class):
                    self.salt = salt
                elif isinstance(salt, dict):
                    self.salt = nested_class.from_kwargs(**salt)
                else:
                    self.salt = salt
            else:
                self.salt = salt
        if salt_order is not None:
            if hasattr(models, self.swagger_types['salt_order']):
                nested_class = getattr(models, self.swagger_types['salt_order'])
                if isinstance(salt_order, nested_class):
                    self.salt_order = salt_order
                elif isinstance(salt_order, dict):
                    self.salt_order = nested_class.from_kwargs(**salt_order)
                else:
                    self.salt_order = salt_order
            else:
                self.salt_order = salt_order
        if value is not None:
            if hasattr(models, self.swagger_types['value']):
                nested_class = getattr(models, self.swagger_types['value'])
                if isinstance(value, nested_class):
                    self.value = value
                elif isinstance(value, dict):
                    self.value = nested_class.from_kwargs(**value)
                else:
                    self.value = value
            else:
                self.value = value
        if work_factor is not None:
            if hasattr(models, self.swagger_types['work_factor']):
                nested_class = getattr(models, self.swagger_types['work_factor'])
                if isinstance(work_factor, nested_class):
                    self.work_factor = work_factor
                elif isinstance(work_factor, dict):
                    self.work_factor = nested_class.from_kwargs(**work_factor)
                else:
                    self.work_factor = work_factor
            else:
                self.work_factor = work_factor

    @property
    def algorithm(self):
        """Gets the algorithm of this PasswordCredentialHash.  # noqa: E501


        :return: The algorithm of this PasswordCredentialHash.  # noqa: E501
        :rtype: PasswordCredentialHashAlgorithm
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this PasswordCredentialHash.


        :param algorithm: The algorithm of this PasswordCredentialHash.  # noqa: E501
        :type: PasswordCredentialHashAlgorithm
        """

        self._algorithm = algorithm

    @property
    def salt(self):
        """Gets the salt of this PasswordCredentialHash.  # noqa: E501


        :return: The salt of this PasswordCredentialHash.  # noqa: E501
        :rtype: str
        """
        return self._salt

    @salt.setter
    def salt(self, salt):
        """Sets the salt of this PasswordCredentialHash.


        :param salt: The salt of this PasswordCredentialHash.  # noqa: E501
        :type: str
        """

        self._salt = salt

    @property
    def salt_order(self):
        """Gets the salt_order of this PasswordCredentialHash.  # noqa: E501


        :return: The salt_order of this PasswordCredentialHash.  # noqa: E501
        :rtype: str
        """
        return self._salt_order

    @salt_order.setter
    def salt_order(self, salt_order):
        """Sets the salt_order of this PasswordCredentialHash.


        :param salt_order: The salt_order of this PasswordCredentialHash.  # noqa: E501
        :type: str
        """

        self._salt_order = salt_order

    @property
    def value(self):
        """Gets the value of this PasswordCredentialHash.  # noqa: E501


        :return: The value of this PasswordCredentialHash.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PasswordCredentialHash.


        :param value: The value of this PasswordCredentialHash.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def work_factor(self):
        """Gets the work_factor of this PasswordCredentialHash.  # noqa: E501


        :return: The work_factor of this PasswordCredentialHash.  # noqa: E501
        :rtype: int
        """
        return self._work_factor

    @work_factor.setter
    def work_factor(self, work_factor):
        """Sets the work_factor of this PasswordCredentialHash.


        :param work_factor: The work_factor of this PasswordCredentialHash.  # noqa: E501
        :type: int
        """

        self._work_factor = work_factor

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
        if issubclass(PasswordCredentialHash, dict):
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
        if not isinstance(other, PasswordCredentialHash):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
