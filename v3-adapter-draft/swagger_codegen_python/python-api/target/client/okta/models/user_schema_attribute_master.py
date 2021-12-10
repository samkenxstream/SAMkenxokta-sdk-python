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

class UserSchemaAttributeMaster(object):
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
        'type': 'UserSchemaAttributeMasterType',
        'priority': 'list[UserSchemaAttributeMasterPriority]'
    }

    attribute_map = {
        'type': 'type',
        'priority': 'priority'
    }

    def __init__(self, config=None):
        super().__init__(config)
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, type=None, priority=None):  # noqa: E501
        """UserSchemaAttributeMaster - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._priority = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if priority is not None:
            self.priority = priority

    @property
    def type(self):
        """Gets the type of this UserSchemaAttributeMaster.  # noqa: E501


        :return: The type of this UserSchemaAttributeMaster.  # noqa: E501
        :rtype: UserSchemaAttributeMasterType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UserSchemaAttributeMaster.


        :param type: The type of this UserSchemaAttributeMaster.  # noqa: E501
        :type: UserSchemaAttributeMasterType
        """

        self._type = type

    @property
    def priority(self):
        """Gets the priority of this UserSchemaAttributeMaster.  # noqa: E501


        :return: The priority of this UserSchemaAttributeMaster.  # noqa: E501
        :rtype: list[UserSchemaAttributeMasterPriority]
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this UserSchemaAttributeMaster.


        :param priority: The priority of this UserSchemaAttributeMaster.  # noqa: E501
        :type: list[UserSchemaAttributeMasterPriority]
        """

        self._priority = priority

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
        if issubclass(UserSchemaAttributeMaster, dict):
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
        if not isinstance(other, UserSchemaAttributeMaster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
