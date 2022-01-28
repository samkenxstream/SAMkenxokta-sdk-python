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

class Provisioning(object):
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
    swagger_types['action'] = 'ProvisioningAction'
    swagger_types['conditions'] = 'ProvisioningConditions'
    swagger_types['groups'] = 'ProvisioningGroups'
    swagger_types['profile_master'] = 'bool'

    attribute_map = {
        'action': 'action',
        'conditions': 'conditions',
        'groups': 'groups',
        'profile_master': 'profileMaster'
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

    def set_attributes(self, action=None, conditions=None, groups=None, profile_master=None, **kwargs):  # noqa: E501
        """Provisioning - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._conditions = None
        self._groups = None
        self._profile_master = None
        self.discriminator = None
        if action is not None:
            if hasattr(models, self.swagger_types['action']):
                nested_class = getattr(models, self.swagger_types['action'])
                if isinstance(action, nested_class):
                    self.action = action
                elif isinstance(action, dict):
                    self.action = nested_class.from_kwargs(**action)
                else:
                    self.action = action
            else:
                self.action = action
        if conditions is not None:
            if hasattr(models, self.swagger_types['conditions']):
                nested_class = getattr(models, self.swagger_types['conditions'])
                if isinstance(conditions, nested_class):
                    self.conditions = conditions
                elif isinstance(conditions, dict):
                    self.conditions = nested_class.from_kwargs(**conditions)
                else:
                    self.conditions = conditions
            else:
                self.conditions = conditions
        if groups is not None:
            if hasattr(models, self.swagger_types['groups']):
                nested_class = getattr(models, self.swagger_types['groups'])
                if isinstance(groups, nested_class):
                    self.groups = groups
                elif isinstance(groups, dict):
                    self.groups = nested_class.from_kwargs(**groups)
                else:
                    self.groups = groups
            else:
                self.groups = groups
        if profile_master is not None:
            if hasattr(models, self.swagger_types['profile_master']):
                nested_class = getattr(models, self.swagger_types['profile_master'])
                if isinstance(profile_master, nested_class):
                    self.profile_master = profile_master
                elif isinstance(profile_master, dict):
                    self.profile_master = nested_class.from_kwargs(**profile_master)
                else:
                    self.profile_master = profile_master
            else:
                self.profile_master = profile_master

    @property
    def action(self):
        """Gets the action of this Provisioning.  # noqa: E501


        :return: The action of this Provisioning.  # noqa: E501
        :rtype: ProvisioningAction
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this Provisioning.


        :param action: The action of this Provisioning.  # noqa: E501
        :type: ProvisioningAction
        """

        self._action = action

    @property
    def conditions(self):
        """Gets the conditions of this Provisioning.  # noqa: E501


        :return: The conditions of this Provisioning.  # noqa: E501
        :rtype: ProvisioningConditions
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this Provisioning.


        :param conditions: The conditions of this Provisioning.  # noqa: E501
        :type: ProvisioningConditions
        """

        self._conditions = conditions

    @property
    def groups(self):
        """Gets the groups of this Provisioning.  # noqa: E501


        :return: The groups of this Provisioning.  # noqa: E501
        :rtype: ProvisioningGroups
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this Provisioning.


        :param groups: The groups of this Provisioning.  # noqa: E501
        :type: ProvisioningGroups
        """

        self._groups = groups

    @property
    def profile_master(self):
        """Gets the profile_master of this Provisioning.  # noqa: E501


        :return: The profile_master of this Provisioning.  # noqa: E501
        :rtype: bool
        """
        return self._profile_master

    @profile_master.setter
    def profile_master(self, profile_master):
        """Sets the profile_master of this Provisioning.


        :param profile_master: The profile_master of this Provisioning.  # noqa: E501
        :type: bool
        """

        self._profile_master = profile_master

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
        if issubclass(Provisioning, dict):
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
        if not isinstance(other, Provisioning):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
