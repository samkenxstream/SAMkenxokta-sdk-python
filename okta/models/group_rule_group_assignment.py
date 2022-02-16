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

class GroupRuleGroupAssignment(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    swagger_types['group_ids'] = 'list[str]'

    attribute_map = {
        'group_ids': 'groupIds'
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

    def set_attributes(self, group_ids=None, **kwargs):  # noqa: E501
        """GroupRuleGroupAssignment - a model defined in Swagger"""  # noqa: E501
        self._group_ids = None
        self.discriminator = None
        if group_ids is not None:
            if hasattr(models, self.swagger_types['group_ids']):
                nested_class = getattr(models, self.swagger_types['group_ids'])
                if isinstance(group_ids, nested_class):
                    self.group_ids = group_ids
                elif isinstance(group_ids, dict):
                    self.group_ids = nested_class.from_kwargs(**group_ids)
                else:
                    self.group_ids = group_ids
            else:
                self.group_ids = group_ids

    @property
    def group_ids(self):
        """Gets the group_ids of this GroupRuleGroupAssignment.  # noqa: E501


        :return: The group_ids of this GroupRuleGroupAssignment.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        """Sets the group_ids of this GroupRuleGroupAssignment.


        :param group_ids: The group_ids of this GroupRuleGroupAssignment.  # noqa: E501
        :type: list[str]
        """

        self._group_ids = group_ids

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
        if issubclass(GroupRuleGroupAssignment, dict):
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
        if not isinstance(other, GroupRuleGroupAssignment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
