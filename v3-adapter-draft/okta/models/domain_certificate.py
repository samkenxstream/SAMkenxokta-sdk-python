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

class DomainCertificate(object):
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
        'certificate': 'str',
        'certificate_chain': 'str',
        'private_key': 'str',
        'type': 'DomainCertificateType'
    }

    attribute_map = {
        'certificate': 'certificate',
        'certificate_chain': 'certificateChain',
        'private_key': 'privateKey',
        'type': 'type'
    }

    def __init__(self, config=None):
        super().__init__(config)
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, certificate=None, certificate_chain=None, private_key=None, type=None):  # noqa: E501
        """DomainCertificate - a model defined in Swagger"""  # noqa: E501
        self._certificate = None
        self._certificate_chain = None
        self._private_key = None
        self._type = None
        self.discriminator = None
        if certificate is not None:
            self.certificate = certificate
        if certificate_chain is not None:
            self.certificate_chain = certificate_chain
        if private_key is not None:
            self.private_key = private_key
        if type is not None:
            self.type = type

    @property
    def certificate(self):
        """Gets the certificate of this DomainCertificate.  # noqa: E501


        :return: The certificate of this DomainCertificate.  # noqa: E501
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this DomainCertificate.


        :param certificate: The certificate of this DomainCertificate.  # noqa: E501
        :type: str
        """

        self._certificate = certificate

    @property
    def certificate_chain(self):
        """Gets the certificate_chain of this DomainCertificate.  # noqa: E501


        :return: The certificate_chain of this DomainCertificate.  # noqa: E501
        :rtype: str
        """
        return self._certificate_chain

    @certificate_chain.setter
    def certificate_chain(self, certificate_chain):
        """Sets the certificate_chain of this DomainCertificate.


        :param certificate_chain: The certificate_chain of this DomainCertificate.  # noqa: E501
        :type: str
        """

        self._certificate_chain = certificate_chain

    @property
    def private_key(self):
        """Gets the private_key of this DomainCertificate.  # noqa: E501


        :return: The private_key of this DomainCertificate.  # noqa: E501
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this DomainCertificate.


        :param private_key: The private_key of this DomainCertificate.  # noqa: E501
        :type: str
        """

        self._private_key = private_key

    @property
    def type(self):
        """Gets the type of this DomainCertificate.  # noqa: E501


        :return: The type of this DomainCertificate.  # noqa: E501
        :rtype: DomainCertificateType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DomainCertificate.


        :param type: The type of this DomainCertificate.  # noqa: E501
        :type: DomainCertificateType
        """

        self._type = type

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
        if issubclass(DomainCertificate, dict):
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
        if not isinstance(other, DomainCertificate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
