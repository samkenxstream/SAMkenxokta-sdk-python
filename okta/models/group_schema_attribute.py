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

class GroupSchemaAttribute(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    swagger_types['description'] = 'str'
    swagger_types['enum'] = 'list[str]'
    swagger_types['external_name'] = 'str'
    swagger_types['external_namespace'] = 'str'
    swagger_types['items'] = 'UserSchemaAttributeItems'
    swagger_types['master'] = 'UserSchemaAttributeMaster'
    swagger_types['max_length'] = 'int'
    swagger_types['min_length'] = 'int'
    swagger_types['mutability'] = 'str'
    swagger_types['one_of'] = 'list[UserSchemaAttributeEnum]'
    swagger_types['permissions'] = 'list[UserSchemaAttributePermission]'
    swagger_types['required'] = 'bool'
    swagger_types['scope'] = 'UserSchemaAttributeScope'
    swagger_types['title'] = 'str'
    swagger_types['type'] = 'UserSchemaAttributeType'
    swagger_types['union'] = 'UserSchemaAttributeUnion'
    swagger_types['unique'] = 'str'

    attribute_map = {
        'description': 'description',
        'enum': 'enum',
        'external_name': 'externalName',
        'external_namespace': 'externalNamespace',
        'items': 'items',
        'master': 'master',
        'max_length': 'maxLength',
        'min_length': 'minLength',
        'mutability': 'mutability',
        'one_of': 'oneOf',
        'permissions': 'permissions',
        'required': 'required',
        'scope': 'scope',
        'title': 'title',
        'type': 'type',
        'union': 'union',
        'unique': 'unique'
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

    def set_attributes(self, description=None, enum=None, external_name=None, external_namespace=None, items=None, master=None, max_length=None, min_length=None, mutability=None, one_of=None, permissions=None, required=None, scope=None, title=None, type=None, union=None, unique=None, **kwargs):  # noqa: E501
        """GroupSchemaAttribute - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._enum = None
        self._external_name = None
        self._external_namespace = None
        self._items = None
        self._master = None
        self._max_length = None
        self._min_length = None
        self._mutability = None
        self._one_of = None
        self._permissions = None
        self._required = None
        self._scope = None
        self._title = None
        self._type = None
        self._union = None
        self._unique = None
        self.discriminator = None
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
        if enum is not None:
            if hasattr(models, self.swagger_types['enum']):
                nested_class = getattr(models, self.swagger_types['enum'])
                if isinstance(enum, nested_class):
                    self.enum = enum
                elif isinstance(enum, dict):
                    self.enum = nested_class.from_kwargs(**enum)
                else:
                    self.enum = enum
            else:
                self.enum = enum
        if external_name is not None:
            if hasattr(models, self.swagger_types['external_name']):
                nested_class = getattr(models, self.swagger_types['external_name'])
                if isinstance(external_name, nested_class):
                    self.external_name = external_name
                elif isinstance(external_name, dict):
                    self.external_name = nested_class.from_kwargs(**external_name)
                else:
                    self.external_name = external_name
            else:
                self.external_name = external_name
        if external_namespace is not None:
            if hasattr(models, self.swagger_types['external_namespace']):
                nested_class = getattr(models, self.swagger_types['external_namespace'])
                if isinstance(external_namespace, nested_class):
                    self.external_namespace = external_namespace
                elif isinstance(external_namespace, dict):
                    self.external_namespace = nested_class.from_kwargs(**external_namespace)
                else:
                    self.external_namespace = external_namespace
            else:
                self.external_namespace = external_namespace
        if items is not None:
            if hasattr(models, self.swagger_types['items']):
                nested_class = getattr(models, self.swagger_types['items'])
                if isinstance(items, nested_class):
                    self.items = items
                elif isinstance(items, dict):
                    self.items = nested_class.from_kwargs(**items)
                else:
                    self.items = items
            else:
                self.items = items
        if master is not None:
            if hasattr(models, self.swagger_types['master']):
                nested_class = getattr(models, self.swagger_types['master'])
                if isinstance(master, nested_class):
                    self.master = master
                elif isinstance(master, dict):
                    self.master = nested_class.from_kwargs(**master)
                else:
                    self.master = master
            else:
                self.master = master
        if max_length is not None:
            if hasattr(models, self.swagger_types['max_length']):
                nested_class = getattr(models, self.swagger_types['max_length'])
                if isinstance(max_length, nested_class):
                    self.max_length = max_length
                elif isinstance(max_length, dict):
                    self.max_length = nested_class.from_kwargs(**max_length)
                else:
                    self.max_length = max_length
            else:
                self.max_length = max_length
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
        if mutability is not None:
            if hasattr(models, self.swagger_types['mutability']):
                nested_class = getattr(models, self.swagger_types['mutability'])
                if isinstance(mutability, nested_class):
                    self.mutability = mutability
                elif isinstance(mutability, dict):
                    self.mutability = nested_class.from_kwargs(**mutability)
                else:
                    self.mutability = mutability
            else:
                self.mutability = mutability
        if one_of is not None:
            if hasattr(models, self.swagger_types['one_of']):
                nested_class = getattr(models, self.swagger_types['one_of'])
                if isinstance(one_of, nested_class):
                    self.one_of = one_of
                elif isinstance(one_of, dict):
                    self.one_of = nested_class.from_kwargs(**one_of)
                else:
                    self.one_of = one_of
            else:
                self.one_of = one_of
        if permissions is not None:
            if hasattr(models, self.swagger_types['permissions']):
                nested_class = getattr(models, self.swagger_types['permissions'])
                if isinstance(permissions, nested_class):
                    self.permissions = permissions
                elif isinstance(permissions, dict):
                    self.permissions = nested_class.from_kwargs(**permissions)
                else:
                    self.permissions = permissions
            else:
                self.permissions = permissions
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
        if scope is not None:
            if hasattr(models, self.swagger_types['scope']):
                nested_class = getattr(models, self.swagger_types['scope'])
                if isinstance(scope, nested_class):
                    self.scope = scope
                elif isinstance(scope, dict):
                    self.scope = nested_class.from_kwargs(**scope)
                else:
                    self.scope = scope
            else:
                self.scope = scope
        if title is not None:
            if hasattr(models, self.swagger_types['title']):
                nested_class = getattr(models, self.swagger_types['title'])
                if isinstance(title, nested_class):
                    self.title = title
                elif isinstance(title, dict):
                    self.title = nested_class.from_kwargs(**title)
                else:
                    self.title = title
            else:
                self.title = title
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
        if union is not None:
            if hasattr(models, self.swagger_types['union']):
                nested_class = getattr(models, self.swagger_types['union'])
                if isinstance(union, nested_class):
                    self.union = union
                elif isinstance(union, dict):
                    self.union = nested_class.from_kwargs(**union)
                else:
                    self.union = union
            else:
                self.union = union
        if unique is not None:
            if hasattr(models, self.swagger_types['unique']):
                nested_class = getattr(models, self.swagger_types['unique'])
                if isinstance(unique, nested_class):
                    self.unique = unique
                elif isinstance(unique, dict):
                    self.unique = nested_class.from_kwargs(**unique)
                else:
                    self.unique = unique
            else:
                self.unique = unique

    @property
    def description(self):
        """Gets the description of this GroupSchemaAttribute.  # noqa: E501


        :return: The description of this GroupSchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GroupSchemaAttribute.


        :param description: The description of this GroupSchemaAttribute.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enum(self):
        """Gets the enum of this GroupSchemaAttribute.  # noqa: E501


        :return: The enum of this GroupSchemaAttribute.  # noqa: E501
        :rtype: list[str]
        """
        return self._enum

    @enum.setter
    def enum(self, enum):
        """Sets the enum of this GroupSchemaAttribute.


        :param enum: The enum of this GroupSchemaAttribute.  # noqa: E501
        :type: list[str]
        """

        self._enum = enum

    @property
    def external_name(self):
        """Gets the external_name of this GroupSchemaAttribute.  # noqa: E501


        :return: The external_name of this GroupSchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._external_name

    @external_name.setter
    def external_name(self, external_name):
        """Sets the external_name of this GroupSchemaAttribute.


        :param external_name: The external_name of this GroupSchemaAttribute.  # noqa: E501
        :type: str
        """

        self._external_name = external_name

    @property
    def external_namespace(self):
        """Gets the external_namespace of this GroupSchemaAttribute.  # noqa: E501


        :return: The external_namespace of this GroupSchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._external_namespace

    @external_namespace.setter
    def external_namespace(self, external_namespace):
        """Sets the external_namespace of this GroupSchemaAttribute.


        :param external_namespace: The external_namespace of this GroupSchemaAttribute.  # noqa: E501
        :type: str
        """

        self._external_namespace = external_namespace

    @property
    def items(self):
        """Gets the items of this GroupSchemaAttribute.  # noqa: E501


        :return: The items of this GroupSchemaAttribute.  # noqa: E501
        :rtype: UserSchemaAttributeItems
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this GroupSchemaAttribute.


        :param items: The items of this GroupSchemaAttribute.  # noqa: E501
        :type: UserSchemaAttributeItems
        """

        self._items = items

    @property
    def master(self):
        """Gets the master of this GroupSchemaAttribute.  # noqa: E501


        :return: The master of this GroupSchemaAttribute.  # noqa: E501
        :rtype: UserSchemaAttributeMaster
        """
        return self._master

    @master.setter
    def master(self, master):
        """Sets the master of this GroupSchemaAttribute.


        :param master: The master of this GroupSchemaAttribute.  # noqa: E501
        :type: UserSchemaAttributeMaster
        """

        self._master = master

    @property
    def max_length(self):
        """Gets the max_length of this GroupSchemaAttribute.  # noqa: E501


        :return: The max_length of this GroupSchemaAttribute.  # noqa: E501
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this GroupSchemaAttribute.


        :param max_length: The max_length of this GroupSchemaAttribute.  # noqa: E501
        :type: int
        """

        self._max_length = max_length

    @property
    def min_length(self):
        """Gets the min_length of this GroupSchemaAttribute.  # noqa: E501


        :return: The min_length of this GroupSchemaAttribute.  # noqa: E501
        :rtype: int
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """Sets the min_length of this GroupSchemaAttribute.


        :param min_length: The min_length of this GroupSchemaAttribute.  # noqa: E501
        :type: int
        """

        self._min_length = min_length

    @property
    def mutability(self):
        """Gets the mutability of this GroupSchemaAttribute.  # noqa: E501


        :return: The mutability of this GroupSchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._mutability

    @mutability.setter
    def mutability(self, mutability):
        """Sets the mutability of this GroupSchemaAttribute.


        :param mutability: The mutability of this GroupSchemaAttribute.  # noqa: E501
        :type: str
        """

        self._mutability = mutability

    @property
    def one_of(self):
        """Gets the one_of of this GroupSchemaAttribute.  # noqa: E501


        :return: The one_of of this GroupSchemaAttribute.  # noqa: E501
        :rtype: list[UserSchemaAttributeEnum]
        """
        return self._one_of

    @one_of.setter
    def one_of(self, one_of):
        """Sets the one_of of this GroupSchemaAttribute.


        :param one_of: The one_of of this GroupSchemaAttribute.  # noqa: E501
        :type: list[UserSchemaAttributeEnum]
        """

        self._one_of = one_of

    @property
    def permissions(self):
        """Gets the permissions of this GroupSchemaAttribute.  # noqa: E501


        :return: The permissions of this GroupSchemaAttribute.  # noqa: E501
        :rtype: list[UserSchemaAttributePermission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this GroupSchemaAttribute.


        :param permissions: The permissions of this GroupSchemaAttribute.  # noqa: E501
        :type: list[UserSchemaAttributePermission]
        """

        self._permissions = permissions

    @property
    def required(self):
        """Gets the required of this GroupSchemaAttribute.  # noqa: E501


        :return: The required of this GroupSchemaAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this GroupSchemaAttribute.


        :param required: The required of this GroupSchemaAttribute.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def scope(self):
        """Gets the scope of this GroupSchemaAttribute.  # noqa: E501


        :return: The scope of this GroupSchemaAttribute.  # noqa: E501
        :rtype: UserSchemaAttributeScope
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this GroupSchemaAttribute.


        :param scope: The scope of this GroupSchemaAttribute.  # noqa: E501
        :type: UserSchemaAttributeScope
        """

        self._scope = scope

    @property
    def title(self):
        """Gets the title of this GroupSchemaAttribute.  # noqa: E501


        :return: The title of this GroupSchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GroupSchemaAttribute.


        :param title: The title of this GroupSchemaAttribute.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this GroupSchemaAttribute.  # noqa: E501


        :return: The type of this GroupSchemaAttribute.  # noqa: E501
        :rtype: UserSchemaAttributeType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GroupSchemaAttribute.


        :param type: The type of this GroupSchemaAttribute.  # noqa: E501
        :type: UserSchemaAttributeType
        """

        self._type = type

    @property
    def union(self):
        """Gets the union of this GroupSchemaAttribute.  # noqa: E501


        :return: The union of this GroupSchemaAttribute.  # noqa: E501
        :rtype: UserSchemaAttributeUnion
        """
        return self._union

    @union.setter
    def union(self, union):
        """Sets the union of this GroupSchemaAttribute.


        :param union: The union of this GroupSchemaAttribute.  # noqa: E501
        :type: UserSchemaAttributeUnion
        """

        self._union = union

    @property
    def unique(self):
        """Gets the unique of this GroupSchemaAttribute.  # noqa: E501


        :return: The unique of this GroupSchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._unique

    @unique.setter
    def unique(self, unique):
        """Sets the unique of this GroupSchemaAttribute.


        :param unique: The unique of this GroupSchemaAttribute.  # noqa: E501
        :type: str
        """

        self._unique = unique

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
        if issubclass(GroupSchemaAttribute, dict):
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
        if not isinstance(other, GroupSchemaAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
