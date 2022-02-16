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

class AccessPolicyConstraint(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    swagger_types['methods'] = 'list[str]'
    swagger_types['reauthenticate_in'] = 'str'
    swagger_types['types'] = 'list[str]'

    attribute_map = {
        'methods': 'methods',
        'reauthenticate_in': 'reauthenticateIn',
        'types': 'types'
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

    def set_attributes(self, methods=None, reauthenticate_in=None, types=None, **kwargs):  # noqa: E501
        """AccessPolicyConstraint - a model defined in Swagger"""  # noqa: E501
        self._methods = None
        self._reauthenticate_in = None
        self._types = None
        self.discriminator = None
        if methods is not None:
            if hasattr(models, self.swagger_types['methods']):
                nested_class = getattr(models, self.swagger_types['methods'])
                if isinstance(methods, nested_class):
                    self.methods = methods
                elif isinstance(methods, dict):
                    self.methods = nested_class.from_kwargs(**methods)
                else:
                    self.methods = methods
            else:
                self.methods = methods
        if reauthenticate_in is not None:
            if hasattr(models, self.swagger_types['reauthenticate_in']):
                nested_class = getattr(models, self.swagger_types['reauthenticate_in'])
                if isinstance(reauthenticate_in, nested_class):
                    self.reauthenticate_in = reauthenticate_in
                elif isinstance(reauthenticate_in, dict):
                    self.reauthenticate_in = nested_class.from_kwargs(**reauthenticate_in)
                else:
                    self.reauthenticate_in = reauthenticate_in
            else:
                self.reauthenticate_in = reauthenticate_in
        if types is not None:
            if hasattr(models, self.swagger_types['types']):
                nested_class = getattr(models, self.swagger_types['types'])
                if isinstance(types, nested_class):
                    self.types = types
                elif isinstance(types, dict):
                    self.types = nested_class.from_kwargs(**types)
                else:
                    self.types = types
            else:
                self.types = types

    @property
    def methods(self):
        """Gets the methods of this AccessPolicyConstraint.  # noqa: E501


        :return: The methods of this AccessPolicyConstraint.  # noqa: E501
        :rtype: list[str]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        """Sets the methods of this AccessPolicyConstraint.


        :param methods: The methods of this AccessPolicyConstraint.  # noqa: E501
        :type: list[str]
        """

        self._methods = methods

    @property
    def reauthenticate_in(self):
        """Gets the reauthenticate_in of this AccessPolicyConstraint.  # noqa: E501


        :return: The reauthenticate_in of this AccessPolicyConstraint.  # noqa: E501
        :rtype: str
        """
        return self._reauthenticate_in

    @reauthenticate_in.setter
    def reauthenticate_in(self, reauthenticate_in):
        """Sets the reauthenticate_in of this AccessPolicyConstraint.


        :param reauthenticate_in: The reauthenticate_in of this AccessPolicyConstraint.  # noqa: E501
        :type: str
        """

        self._reauthenticate_in = reauthenticate_in

    @property
    def types(self):
        """Gets the types of this AccessPolicyConstraint.  # noqa: E501


        :return: The types of this AccessPolicyConstraint.  # noqa: E501
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this AccessPolicyConstraint.


        :param types: The types of this AccessPolicyConstraint.  # noqa: E501
        :type: list[str]
        """

        self._types = types

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
        if issubclass(AccessPolicyConstraint, dict):
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
        if not isinstance(other, AccessPolicyConstraint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
