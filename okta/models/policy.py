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

class Policy(object):
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
    swagger_types['embedded'] = 'dict(str, object)'
    swagger_types['links'] = 'dict(str, object)'
    swagger_types['conditions'] = 'PolicyRuleConditions'
    swagger_types['created'] = 'datetime'
    swagger_types['description'] = 'str'
    swagger_types['id'] = 'str'
    swagger_types['last_updated'] = 'datetime'
    swagger_types['name'] = 'str'
    swagger_types['priority'] = 'int'
    swagger_types['status'] = 'LifecycleStatus'
    swagger_types['system'] = 'bool'
    swagger_types['type'] = 'PolicyType'

    attribute_map = {
        'embedded': '_embedded',
        'links': '_links',
        'conditions': 'conditions',
        'created': 'created',
        'description': 'description',
        'id': 'id',
        'last_updated': 'lastUpdated',
        'name': 'name',
        'priority': 'priority',
        'status': 'status',
        'system': 'system',
        'type': 'type'
    }

    discriminator_value_class_map = {
            'ACCESS_POLICY'.lower(): 'AccessPolicy',
            'IDP_DISCOVERY'.lower(): 'IdentityProviderPolicy',
            'OAUTH_AUTHORIZATION_POLICY'.lower(): 'AuthorizationServerPolicy',
            'OKTA_SIGN_ON'.lower(): 'OktaSignOnPolicy',
            'PASSWORD'.lower(): 'PasswordPolicy',
            'PROFILE_ENROLLMENT'.lower(): 'ProfileEnrollmentPolicy',
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

    def set_attributes(self, embedded=None, links=None, conditions=None, created=None, description=None, id=None, last_updated=None, name=None, priority=None, status=None, system=None, type=None, **kwargs):  # noqa: E501
        """Policy - a model defined in Swagger"""  # noqa: E501
        self._embedded = None
        self._links = None
        self._conditions = None
        self._created = None
        self._description = None
        self._id = None
        self._last_updated = None
        self._name = None
        self._priority = None
        self._status = None
        self._system = None
        self._type = None
        self.discriminator = 'type'
        if embedded is not None:
            if hasattr(models, self.swagger_types['embedded']):
                nested_class = getattr(models, self.swagger_types['embedded'])
                if isinstance(embedded, nested_class):
                    self.embedded = embedded
                elif isinstance(embedded, dict):
                    self.embedded = nested_class.from_kwargs(**embedded)
                else:
                    self.embedded = embedded
            else:
                self.embedded = embedded
        if links is not None:
            if hasattr(models, self.swagger_types['links']):
                nested_class = getattr(models, self.swagger_types['links'])
                if isinstance(links, nested_class):
                    self.links = links
                elif isinstance(links, dict):
                    self.links = nested_class.from_kwargs(**links)
                else:
                    self.links = links
            else:
                self.links = links
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
        if created is not None:
            if hasattr(models, self.swagger_types['created']):
                nested_class = getattr(models, self.swagger_types['created'])
                if isinstance(created, nested_class):
                    self.created = created
                elif isinstance(created, dict):
                    self.created = nested_class.from_kwargs(**created)
                else:
                    self.created = created
            else:
                self.created = created
        if description is not None:
            if hasattr(models, self.swagger_types['description']):
                nested_class = getattr(models, self.swagger_types['description'])
                if isinstance(description, nested_class):
                    self.description = description
                elif isinstance(description, dict):
                    self.description = nested_class.from_kwargs(**description)
                else:
                    self.description = description
            else:
                self.description = description
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
        if last_updated is not None:
            if hasattr(models, self.swagger_types['last_updated']):
                nested_class = getattr(models, self.swagger_types['last_updated'])
                if isinstance(last_updated, nested_class):
                    self.last_updated = last_updated
                elif isinstance(last_updated, dict):
                    self.last_updated = nested_class.from_kwargs(**last_updated)
                else:
                    self.last_updated = last_updated
            else:
                self.last_updated = last_updated
        if name is not None:
            if hasattr(models, self.swagger_types['name']):
                nested_class = getattr(models, self.swagger_types['name'])
                if isinstance(name, nested_class):
                    self.name = name
                elif isinstance(name, dict):
                    self.name = nested_class.from_kwargs(**name)
                else:
                    self.name = name
            else:
                self.name = name
        if priority is not None:
            if hasattr(models, self.swagger_types['priority']):
                nested_class = getattr(models, self.swagger_types['priority'])
                if isinstance(priority, nested_class):
                    self.priority = priority
                elif isinstance(priority, dict):
                    self.priority = nested_class.from_kwargs(**priority)
                else:
                    self.priority = priority
            else:
                self.priority = priority
        if status is not None:
            if hasattr(models, self.swagger_types['status']):
                nested_class = getattr(models, self.swagger_types['status'])
                if isinstance(status, nested_class):
                    self.status = status
                elif isinstance(status, dict):
                    self.status = nested_class.from_kwargs(**status)
                else:
                    self.status = status
            else:
                self.status = status
        if system is not None:
            if hasattr(models, self.swagger_types['system']):
                nested_class = getattr(models, self.swagger_types['system'])
                if isinstance(system, nested_class):
                    self.system = system
                elif isinstance(system, dict):
                    self.system = nested_class.from_kwargs(**system)
                else:
                    self.system = system
            else:
                self.system = system
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

    @property
    def embedded(self):
        """Gets the embedded of this Policy.  # noqa: E501


        :return: The embedded of this Policy.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this Policy.


        :param embedded: The embedded of this Policy.  # noqa: E501
        :type: dict(str, object)
        """

        self._embedded = embedded

    @property
    def links(self):
        """Gets the links of this Policy.  # noqa: E501


        :return: The links of this Policy.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Policy.


        :param links: The links of this Policy.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def conditions(self):
        """Gets the conditions of this Policy.  # noqa: E501


        :return: The conditions of this Policy.  # noqa: E501
        :rtype: PolicyRuleConditions
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this Policy.


        :param conditions: The conditions of this Policy.  # noqa: E501
        :type: PolicyRuleConditions
        """

        self._conditions = conditions

    @property
    def created(self):
        """Gets the created of this Policy.  # noqa: E501


        :return: The created of this Policy.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Policy.


        :param created: The created of this Policy.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def description(self):
        """Gets the description of this Policy.  # noqa: E501


        :return: The description of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Policy.


        :param description: The description of this Policy.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Policy.  # noqa: E501


        :return: The id of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Policy.


        :param id: The id of this Policy.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_updated(self):
        """Gets the last_updated of this Policy.  # noqa: E501


        :return: The last_updated of this Policy.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this Policy.


        :param last_updated: The last_updated of this Policy.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def name(self):
        """Gets the name of this Policy.  # noqa: E501


        :return: The name of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Policy.


        :param name: The name of this Policy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def priority(self):
        """Gets the priority of this Policy.  # noqa: E501


        :return: The priority of this Policy.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this Policy.


        :param priority: The priority of this Policy.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def status(self):
        """Gets the status of this Policy.  # noqa: E501


        :return: The status of this Policy.  # noqa: E501
        :rtype: LifecycleStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Policy.


        :param status: The status of this Policy.  # noqa: E501
        :type: LifecycleStatus
        """

        self._status = status

    @property
    def system(self):
        """Gets the system of this Policy.  # noqa: E501


        :return: The system of this Policy.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this Policy.


        :param system: The system of this Policy.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def type(self):
        """Gets the type of this Policy.  # noqa: E501


        :return: The type of this Policy.  # noqa: E501
        :rtype: PolicyType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Policy.


        :param type: The type of this Policy.  # noqa: E501
        :type: PolicyType
        """

        self._type = type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(Policy, dict):
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
        if not isinstance(other, Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
