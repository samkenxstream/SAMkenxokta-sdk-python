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

class IonField(object):
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
        'form': 'IonForm',
        'label': 'str',
        'mutable': 'bool',
        'name': 'str',
        'required': 'bool',
        'secret': 'bool',
        'type': 'str',
        'value': 'dict(str, object)',
        'visible': 'bool'
    }

    attribute_map = {
        'form': 'form',
        'label': 'label',
        'mutable': 'mutable',
        'name': 'name',
        'required': 'required',
        'secret': 'secret',
        'type': 'type',
        'value': 'value',
        'visible': 'visible'
    }

    def __init__(self, config=None):
        super().__init__(config)
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, form=None, label=None, mutable=None, name=None, required=None, secret=None, type=None, value=None, visible=None):  # noqa: E501
        """IonField - a model defined in Swagger"""  # noqa: E501
        self._form = None
        self._label = None
        self._mutable = None
        self._name = None
        self._required = None
        self._secret = None
        self._type = None
        self._value = None
        self._visible = None
        self.discriminator = None
        if form is not None:
            self.form = form
        if label is not None:
            self.label = label
        if mutable is not None:
            self.mutable = mutable
        if name is not None:
            self.name = name
        if required is not None:
            self.required = required
        if secret is not None:
            self.secret = secret
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if visible is not None:
            self.visible = visible

    @property
    def form(self):
        """Gets the form of this IonField.  # noqa: E501


        :return: The form of this IonField.  # noqa: E501
        :rtype: IonForm
        """
        return self._form

    @form.setter
    def form(self, form):
        """Sets the form of this IonField.


        :param form: The form of this IonField.  # noqa: E501
        :type: IonForm
        """

        self._form = form

    @property
    def label(self):
        """Gets the label of this IonField.  # noqa: E501


        :return: The label of this IonField.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this IonField.


        :param label: The label of this IonField.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def mutable(self):
        """Gets the mutable of this IonField.  # noqa: E501


        :return: The mutable of this IonField.  # noqa: E501
        :rtype: bool
        """
        return self._mutable

    @mutable.setter
    def mutable(self, mutable):
        """Sets the mutable of this IonField.


        :param mutable: The mutable of this IonField.  # noqa: E501
        :type: bool
        """

        self._mutable = mutable

    @property
    def name(self):
        """Gets the name of this IonField.  # noqa: E501


        :return: The name of this IonField.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IonField.


        :param name: The name of this IonField.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def required(self):
        """Gets the required of this IonField.  # noqa: E501


        :return: The required of this IonField.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this IonField.


        :param required: The required of this IonField.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def secret(self):
        """Gets the secret of this IonField.  # noqa: E501


        :return: The secret of this IonField.  # noqa: E501
        :rtype: bool
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this IonField.


        :param secret: The secret of this IonField.  # noqa: E501
        :type: bool
        """

        self._secret = secret

    @property
    def type(self):
        """Gets the type of this IonField.  # noqa: E501


        :return: The type of this IonField.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IonField.


        :param type: The type of this IonField.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this IonField.  # noqa: E501


        :return: The value of this IonField.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this IonField.


        :param value: The value of this IonField.  # noqa: E501
        :type: dict(str, object)
        """

        self._value = value

    @property
    def visible(self):
        """Gets the visible of this IonField.  # noqa: E501


        :return: The visible of this IonField.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this IonField.


        :param visible: The visible of this IonField.  # noqa: E501
        :type: bool
        """

        self._visible = visible

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
        if issubclass(IonField, dict):
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
        if not isinstance(other, IonField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
