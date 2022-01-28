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

class LogIpAddress(object):
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
    swagger_types['geographical_context'] = 'LogGeographicalContext'
    swagger_types['ip'] = 'str'
    swagger_types['source'] = 'str'
    swagger_types['version'] = 'str'

    attribute_map = {
        'geographical_context': 'geographicalContext',
        'ip': 'ip',
        'source': 'source',
        'version': 'version'
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

    def set_attributes(self, geographical_context=None, ip=None, source=None, version=None, **kwargs):  # noqa: E501
        """LogIpAddress - a model defined in Swagger"""  # noqa: E501
        self._geographical_context = None
        self._ip = None
        self._source = None
        self._version = None
        self.discriminator = None
        if geographical_context is not None:
            if hasattr(models, self.swagger_types['geographical_context']):
                nested_class = getattr(models, self.swagger_types['geographical_context'])
                if isinstance(geographical_context, nested_class):
                    self.geographical_context = geographical_context
                elif isinstance(geographical_context, dict):
                    self.geographical_context = nested_class.from_kwargs(**geographical_context)
                else:
                    self.geographical_context = geographical_context
            else:
                self.geographical_context = geographical_context
        if ip is not None:
            if hasattr(models, self.swagger_types['ip']):
                nested_class = getattr(models, self.swagger_types['ip'])
                if isinstance(ip, nested_class):
                    self.ip = ip
                elif isinstance(ip, dict):
                    self.ip = nested_class.from_kwargs(**ip)
                else:
                    self.ip = ip
            else:
                self.ip = ip
        if source is not None:
            if hasattr(models, self.swagger_types['source']):
                nested_class = getattr(models, self.swagger_types['source'])
                if isinstance(source, nested_class):
                    self.source = source
                elif isinstance(source, dict):
                    self.source = nested_class.from_kwargs(**source)
                else:
                    self.source = source
            else:
                self.source = source
        if version is not None:
            if hasattr(models, self.swagger_types['version']):
                nested_class = getattr(models, self.swagger_types['version'])
                if isinstance(version, nested_class):
                    self.version = version
                elif isinstance(version, dict):
                    self.version = nested_class.from_kwargs(**version)
                else:
                    self.version = version
            else:
                self.version = version

    @property
    def geographical_context(self):
        """Gets the geographical_context of this LogIpAddress.  # noqa: E501


        :return: The geographical_context of this LogIpAddress.  # noqa: E501
        :rtype: LogGeographicalContext
        """
        return self._geographical_context

    @geographical_context.setter
    def geographical_context(self, geographical_context):
        """Sets the geographical_context of this LogIpAddress.


        :param geographical_context: The geographical_context of this LogIpAddress.  # noqa: E501
        :type: LogGeographicalContext
        """

        self._geographical_context = geographical_context

    @property
    def ip(self):
        """Gets the ip of this LogIpAddress.  # noqa: E501


        :return: The ip of this LogIpAddress.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this LogIpAddress.


        :param ip: The ip of this LogIpAddress.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def source(self):
        """Gets the source of this LogIpAddress.  # noqa: E501


        :return: The source of this LogIpAddress.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this LogIpAddress.


        :param source: The source of this LogIpAddress.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def version(self):
        """Gets the version of this LogIpAddress.  # noqa: E501


        :return: The version of this LogIpAddress.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this LogIpAddress.


        :param version: The version of this LogIpAddress.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(LogIpAddress, dict):
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
        if not isinstance(other, LogIpAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
