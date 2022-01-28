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

class ProtocolAlgorithmTypeSignature(object):
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
    swagger_types['algorithm'] = 'str'
    swagger_types['scope'] = 'ProtocolAlgorithmTypeSignatureScope'

    attribute_map = {
        'algorithm': 'algorithm',
        'scope': 'scope'
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

    def set_attributes(self, algorithm=None, scope=None, **kwargs):  # noqa: E501
        """ProtocolAlgorithmTypeSignature - a model defined in Swagger"""  # noqa: E501
        self._algorithm = None
        self._scope = None
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

    @property
    def algorithm(self):
        """Gets the algorithm of this ProtocolAlgorithmTypeSignature.  # noqa: E501


        :return: The algorithm of this ProtocolAlgorithmTypeSignature.  # noqa: E501
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this ProtocolAlgorithmTypeSignature.


        :param algorithm: The algorithm of this ProtocolAlgorithmTypeSignature.  # noqa: E501
        :type: str
        """

        self._algorithm = algorithm

    @property
    def scope(self):
        """Gets the scope of this ProtocolAlgorithmTypeSignature.  # noqa: E501


        :return: The scope of this ProtocolAlgorithmTypeSignature.  # noqa: E501
        :rtype: ProtocolAlgorithmTypeSignatureScope
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ProtocolAlgorithmTypeSignature.


        :param scope: The scope of this ProtocolAlgorithmTypeSignature.  # noqa: E501
        :type: ProtocolAlgorithmTypeSignatureScope
        """

        self._scope = scope

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
        if issubclass(ProtocolAlgorithmTypeSignature, dict):
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
        if not isinstance(other, ProtocolAlgorithmTypeSignature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
