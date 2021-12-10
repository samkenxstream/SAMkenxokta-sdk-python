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

class WebAuthnUserFactorProfile(object):
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
        'credential_id': 'str',
        'authenticator_name': 'str'
    }

    attribute_map = {
        'credential_id': 'credentialId',
        'authenticator_name': 'authenticatorName'
    }

    def __init__(self, config=None):
        super().__init__(config)
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, credential_id=None, authenticator_name=None):  # noqa: E501
        """WebAuthnUserFactorProfile - a model defined in Swagger"""  # noqa: E501
        self._credential_id = None
        self._authenticator_name = None
        self.discriminator = None
        if credential_id is not None:
            self.credential_id = credential_id
        if authenticator_name is not None:
            self.authenticator_name = authenticator_name

    @property
    def credential_id(self):
        """Gets the credential_id of this WebAuthnUserFactorProfile.  # noqa: E501


        :return: The credential_id of this WebAuthnUserFactorProfile.  # noqa: E501
        :rtype: str
        """
        return self._credential_id

    @credential_id.setter
    def credential_id(self, credential_id):
        """Sets the credential_id of this WebAuthnUserFactorProfile.


        :param credential_id: The credential_id of this WebAuthnUserFactorProfile.  # noqa: E501
        :type: str
        """

        self._credential_id = credential_id

    @property
    def authenticator_name(self):
        """Gets the authenticator_name of this WebAuthnUserFactorProfile.  # noqa: E501


        :return: The authenticator_name of this WebAuthnUserFactorProfile.  # noqa: E501
        :rtype: str
        """
        return self._authenticator_name

    @authenticator_name.setter
    def authenticator_name(self, authenticator_name):
        """Sets the authenticator_name of this WebAuthnUserFactorProfile.


        :param authenticator_name: The authenticator_name of this WebAuthnUserFactorProfile.  # noqa: E501
        :type: str
        """

        self._authenticator_name = authenticator_name

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
        if issubclass(WebAuthnUserFactorProfile, dict):
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
        if not isinstance(other, WebAuthnUserFactorProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
