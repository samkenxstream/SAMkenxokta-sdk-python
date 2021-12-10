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

class UserFactor(object):
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
        'embedded': 'dict(str, object)',
        'links': 'dict(str, object)',
        'created': 'datetime',
        'factor_type': 'FactorType',
        'id': 'str',
        'last_updated': 'datetime',
        'provider': 'FactorProvider',
        'status': 'FactorStatus',
        'verify': 'VerifyFactorRequest'
    }

    attribute_map = {
        'embedded': '_embedded',
        'links': '_links',
        'created': 'created',
        'factor_type': 'factorType',
        'id': 'id',
        'last_updated': 'lastUpdated',
        'provider': 'provider',
        'status': 'status',
        'verify': 'verify'
    }

    discriminator_value_class_map = {
            'call'.lower(): '#/components/schemas/CallUserFactor',
            'email'.lower(): '#/components/schemas/EmailUserFactor',
            'push'.lower(): '#/components/schemas/PushUserFactor',
            'question'.lower(): '#/components/schemas/SecurityQuestionUserFactor',
            'sms'.lower(): '#/components/schemas/SmsUserFactor',
            'token'.lower(): '#/components/schemas/TokenUserFactor',
            'token:hardware'.lower(): '#/components/schemas/HardwareUserFactor',
            'token:hotp'.lower(): '#/components/schemas/CustomHotpUserFactor',
            'token:software:totp'.lower(): '#/components/schemas/TotpUserFactor',
            'u2f'.lower(): '#/components/schemas/U2fUserFactor',
            'web'.lower(): '#/components/schemas/WebUserFactor',
            'webauthn'.lower(): '#/components/schemas/WebAuthnUserFactor',
            'hotp'.lower(): '#/components/schemas/CustomHotpUserFactor',
    }

    def __init__(self, config=None):
        super().__init__(config)
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, embedded=None, links=None, created=None, factor_type=None, id=None, last_updated=None, provider=None, status=None, verify=None):  # noqa: E501
        """UserFactor - a model defined in Swagger"""  # noqa: E501
        self._embedded = None
        self._links = None
        self._created = None
        self._factor_type = None
        self._id = None
        self._last_updated = None
        self._provider = None
        self._status = None
        self._verify = None
        self.discriminator = 'factorType'
        if embedded is not None:
            self.embedded = embedded
        if links is not None:
            self.links = links
        if created is not None:
            self.created = created
        if factor_type is not None:
            self.factor_type = factor_type
        if id is not None:
            self.id = id
        if last_updated is not None:
            self.last_updated = last_updated
        if provider is not None:
            self.provider = provider
        if status is not None:
            self.status = status
        if verify is not None:
            self.verify = verify

    @property
    def embedded(self):
        """Gets the embedded of this UserFactor.  # noqa: E501


        :return: The embedded of this UserFactor.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this UserFactor.


        :param embedded: The embedded of this UserFactor.  # noqa: E501
        :type: dict(str, object)
        """

        self._embedded = embedded

    @property
    def links(self):
        """Gets the links of this UserFactor.  # noqa: E501


        :return: The links of this UserFactor.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this UserFactor.


        :param links: The links of this UserFactor.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def created(self):
        """Gets the created of this UserFactor.  # noqa: E501


        :return: The created of this UserFactor.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this UserFactor.


        :param created: The created of this UserFactor.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def factor_type(self):
        """Gets the factor_type of this UserFactor.  # noqa: E501


        :return: The factor_type of this UserFactor.  # noqa: E501
        :rtype: FactorType
        """
        return self._factor_type

    @factor_type.setter
    def factor_type(self, factor_type):
        """Sets the factor_type of this UserFactor.


        :param factor_type: The factor_type of this UserFactor.  # noqa: E501
        :type: FactorType
        """

        self._factor_type = factor_type

    @property
    def id(self):
        """Gets the id of this UserFactor.  # noqa: E501


        :return: The id of this UserFactor.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserFactor.


        :param id: The id of this UserFactor.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_updated(self):
        """Gets the last_updated of this UserFactor.  # noqa: E501


        :return: The last_updated of this UserFactor.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this UserFactor.


        :param last_updated: The last_updated of this UserFactor.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def provider(self):
        """Gets the provider of this UserFactor.  # noqa: E501


        :return: The provider of this UserFactor.  # noqa: E501
        :rtype: FactorProvider
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this UserFactor.


        :param provider: The provider of this UserFactor.  # noqa: E501
        :type: FactorProvider
        """

        self._provider = provider

    @property
    def status(self):
        """Gets the status of this UserFactor.  # noqa: E501


        :return: The status of this UserFactor.  # noqa: E501
        :rtype: FactorStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserFactor.


        :param status: The status of this UserFactor.  # noqa: E501
        :type: FactorStatus
        """

        self._status = status

    @property
    def verify(self):
        """Gets the verify of this UserFactor.  # noqa: E501


        :return: The verify of this UserFactor.  # noqa: E501
        :rtype: VerifyFactorRequest
        """
        return self._verify

    @verify.setter
    def verify(self, verify):
        """Sets the verify of this UserFactor.


        :param verify: The verify of this UserFactor.  # noqa: E501
        :type: VerifyFactorRequest
        """

        self._verify = verify

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
        if issubclass(UserFactor, dict):
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
        if not isinstance(other, UserFactor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
