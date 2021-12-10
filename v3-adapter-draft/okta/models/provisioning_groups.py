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

class ProvisioningGroups(object):
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
        'action': 'str',
        'assignments': 'list[str]',
        'filter': 'list[str]',
        'source_attribute_name': 'str'
    }

    attribute_map = {
        'action': 'action',
        'assignments': 'assignments',
        'filter': 'filter',
        'source_attribute_name': 'sourceAttributeName'
    }

    def __init__(self, config=None):
        super().__init__(config)
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, action=None, assignments=None, filter=None, source_attribute_name=None):  # noqa: E501
        """ProvisioningGroups - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._assignments = None
        self._filter = None
        self._source_attribute_name = None
        self.discriminator = None
        if action is not None:
            self.action = action
        if assignments is not None:
            self.assignments = assignments
        if filter is not None:
            self.filter = filter
        if source_attribute_name is not None:
            self.source_attribute_name = source_attribute_name

    @property
    def action(self):
        """Gets the action of this ProvisioningGroups.  # noqa: E501


        :return: The action of this ProvisioningGroups.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ProvisioningGroups.


        :param action: The action of this ProvisioningGroups.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "APPEND", "SYNC", "ASSIGN"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def assignments(self):
        """Gets the assignments of this ProvisioningGroups.  # noqa: E501


        :return: The assignments of this ProvisioningGroups.  # noqa: E501
        :rtype: list[str]
        """
        return self._assignments

    @assignments.setter
    def assignments(self, assignments):
        """Sets the assignments of this ProvisioningGroups.


        :param assignments: The assignments of this ProvisioningGroups.  # noqa: E501
        :type: list[str]
        """

        self._assignments = assignments

    @property
    def filter(self):
        """Gets the filter of this ProvisioningGroups.  # noqa: E501


        :return: The filter of this ProvisioningGroups.  # noqa: E501
        :rtype: list[str]
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ProvisioningGroups.


        :param filter: The filter of this ProvisioningGroups.  # noqa: E501
        :type: list[str]
        """

        self._filter = filter

    @property
    def source_attribute_name(self):
        """Gets the source_attribute_name of this ProvisioningGroups.  # noqa: E501


        :return: The source_attribute_name of this ProvisioningGroups.  # noqa: E501
        :rtype: str
        """
        return self._source_attribute_name

    @source_attribute_name.setter
    def source_attribute_name(self, source_attribute_name):
        """Sets the source_attribute_name of this ProvisioningGroups.


        :param source_attribute_name: The source_attribute_name of this ProvisioningGroups.  # noqa: E501
        :type: str
        """

        self._source_attribute_name = source_attribute_name

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
        if issubclass(ProvisioningGroups, dict):
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
        if not isinstance(other, ProvisioningGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
