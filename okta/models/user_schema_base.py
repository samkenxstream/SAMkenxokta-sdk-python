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

class UserSchemaBase(object):
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
    swagger_types['id'] = 'str'
    swagger_types['type'] = 'str'
    swagger_types['properties'] = 'UserSchemaBaseProperties'
    swagger_types['required'] = 'list[str]'

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'properties': 'properties',
        'required': 'required'
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

    def set_attributes(self, id=None, type=None, properties=None, required=None, **kwargs):  # noqa: E501
        """UserSchemaBase - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._properties = None
        self._required = None
        self.discriminator = None
        if id is not None:
            if hasattr(models, self.swagger_types['id']):
                nested_class = getattr(models, self.swagger_types['id'])
                if isinstance(id, nested_class):
                    self.id = id
                elif isinstance(id, dict):
                    self.id = nested_class.from_kwargs(**id)
                else:
                    self.id = id
            else:
                self.id = id
        if type is not None:
            if hasattr(models, self.swagger_types['type']):
                nested_class = getattr(models, self.swagger_types['type'])
                if isinstance(type, nested_class):
                    self.type = type
                elif isinstance(type, dict):
                    self.type = nested_class.from_kwargs(**type)
                else:
                    self.type = type
            else:
                self.type = type
        if properties is not None:
            if hasattr(models, self.swagger_types['properties']):
                nested_class = getattr(models, self.swagger_types['properties'])
                if isinstance(properties, nested_class):
                    self.properties = properties
                elif isinstance(properties, dict):
                    self.properties = nested_class.from_kwargs(**properties)
                else:
                    self.properties = properties
            else:
                self.properties = properties
        if required is not None:
            if hasattr(models, self.swagger_types['required']):
                nested_class = getattr(models, self.swagger_types['required'])
                if isinstance(required, nested_class):
                    self.required = required
                elif isinstance(required, dict):
                    self.required = nested_class.from_kwargs(**required)
                else:
                    self.required = required
            else:
                self.required = required

    @property
    def id(self):
        """Gets the id of this UserSchemaBase.  # noqa: E501


        :return: The id of this UserSchemaBase.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserSchemaBase.


        :param id: The id of this UserSchemaBase.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this UserSchemaBase.  # noqa: E501


        :return: The type of this UserSchemaBase.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UserSchemaBase.


        :param type: The type of this UserSchemaBase.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def properties(self):
        """Gets the properties of this UserSchemaBase.  # noqa: E501


        :return: The properties of this UserSchemaBase.  # noqa: E501
        :rtype: UserSchemaBaseProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this UserSchemaBase.


        :param properties: The properties of this UserSchemaBase.  # noqa: E501
        :type: UserSchemaBaseProperties
        """

        self._properties = properties

    @property
    def required(self):
        """Gets the required of this UserSchemaBase.  # noqa: E501


        :return: The required of this UserSchemaBase.  # noqa: E501
        :rtype: list[str]
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this UserSchemaBase.


        :param required: The required of this UserSchemaBase.  # noqa: E501
        :type: list[str]
        """

        self._required = required

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
        if issubclass(UserSchemaBase, dict):
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
        if not isinstance(other, UserSchemaBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
