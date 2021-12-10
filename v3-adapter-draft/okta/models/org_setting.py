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

class OrgSetting(object):
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
        'links': 'dict(str, object)',
        'address1': 'str',
        'address2': 'str',
        'city': 'str',
        'company_name': 'str',
        'country': 'str',
        'created': 'datetime',
        'end_user_support_help_url': 'str',
        'expires_at': 'datetime',
        'id': 'str',
        'last_updated': 'datetime',
        'phone_number': 'str',
        'postal_code': 'str',
        'state': 'str',
        'status': 'str',
        'subdomain': 'str',
        'support_phone_number': 'str',
        'website': 'str'
    }

    attribute_map = {
        'links': '_links',
        'address1': 'address1',
        'address2': 'address2',
        'city': 'city',
        'company_name': 'companyName',
        'country': 'country',
        'created': 'created',
        'end_user_support_help_url': 'endUserSupportHelpURL',
        'expires_at': 'expiresAt',
        'id': 'id',
        'last_updated': 'lastUpdated',
        'phone_number': 'phoneNumber',
        'postal_code': 'postalCode',
        'state': 'state',
        'status': 'status',
        'subdomain': 'subdomain',
        'support_phone_number': 'supportPhoneNumber',
        'website': 'website'
    }

    def __init__(self, config=None):
        super().__init__(config)
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, links=None, address1=None, address2=None, city=None, company_name=None, country=None, created=None, end_user_support_help_url=None, expires_at=None, id=None, last_updated=None, phone_number=None, postal_code=None, state=None, status=None, subdomain=None, support_phone_number=None, website=None):  # noqa: E501
        """OrgSetting - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._address1 = None
        self._address2 = None
        self._city = None
        self._company_name = None
        self._country = None
        self._created = None
        self._end_user_support_help_url = None
        self._expires_at = None
        self._id = None
        self._last_updated = None
        self._phone_number = None
        self._postal_code = None
        self._state = None
        self._status = None
        self._subdomain = None
        self._support_phone_number = None
        self._website = None
        self.discriminator = None
        if links is not None:
            self.links = links
        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if city is not None:
            self.city = city
        if company_name is not None:
            self.company_name = company_name
        if country is not None:
            self.country = country
        if created is not None:
            self.created = created
        if end_user_support_help_url is not None:
            self.end_user_support_help_url = end_user_support_help_url
        if expires_at is not None:
            self.expires_at = expires_at
        if id is not None:
            self.id = id
        if last_updated is not None:
            self.last_updated = last_updated
        if phone_number is not None:
            self.phone_number = phone_number
        if postal_code is not None:
            self.postal_code = postal_code
        if state is not None:
            self.state = state
        if status is not None:
            self.status = status
        if subdomain is not None:
            self.subdomain = subdomain
        if support_phone_number is not None:
            self.support_phone_number = support_phone_number
        if website is not None:
            self.website = website

    @property
    def links(self):
        """Gets the links of this OrgSetting.  # noqa: E501


        :return: The links of this OrgSetting.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this OrgSetting.


        :param links: The links of this OrgSetting.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def address1(self):
        """Gets the address1 of this OrgSetting.  # noqa: E501


        :return: The address1 of this OrgSetting.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this OrgSetting.


        :param address1: The address1 of this OrgSetting.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this OrgSetting.  # noqa: E501


        :return: The address2 of this OrgSetting.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this OrgSetting.


        :param address2: The address2 of this OrgSetting.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this OrgSetting.  # noqa: E501


        :return: The city of this OrgSetting.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this OrgSetting.


        :param city: The city of this OrgSetting.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def company_name(self):
        """Gets the company_name of this OrgSetting.  # noqa: E501


        :return: The company_name of this OrgSetting.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this OrgSetting.


        :param company_name: The company_name of this OrgSetting.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def country(self):
        """Gets the country of this OrgSetting.  # noqa: E501


        :return: The country of this OrgSetting.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this OrgSetting.


        :param country: The country of this OrgSetting.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def created(self):
        """Gets the created of this OrgSetting.  # noqa: E501


        :return: The created of this OrgSetting.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this OrgSetting.


        :param created: The created of this OrgSetting.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def end_user_support_help_url(self):
        """Gets the end_user_support_help_url of this OrgSetting.  # noqa: E501


        :return: The end_user_support_help_url of this OrgSetting.  # noqa: E501
        :rtype: str
        """
        return self._end_user_support_help_url

    @end_user_support_help_url.setter
    def end_user_support_help_url(self, end_user_support_help_url):
        """Sets the end_user_support_help_url of this OrgSetting.


        :param end_user_support_help_url: The end_user_support_help_url of this OrgSetting.  # noqa: E501
        :type: str
        """

        self._end_user_support_help_url = end_user_support_help_url

    @property
    def expires_at(self):
        """Gets the expires_at of this OrgSetting.  # noqa: E501


        :return: The expires_at of this OrgSetting.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this OrgSetting.


        :param expires_at: The expires_at of this OrgSetting.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def id(self):
        """Gets the id of this OrgSetting.  # noqa: E501


        :return: The id of this OrgSetting.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrgSetting.


        :param id: The id of this OrgSetting.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_updated(self):
        """Gets the last_updated of this OrgSetting.  # noqa: E501


        :return: The last_updated of this OrgSetting.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this OrgSetting.


        :param last_updated: The last_updated of this OrgSetting.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def phone_number(self):
        """Gets the phone_number of this OrgSetting.  # noqa: E501


        :return: The phone_number of this OrgSetting.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this OrgSetting.


        :param phone_number: The phone_number of this OrgSetting.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def postal_code(self):
        """Gets the postal_code of this OrgSetting.  # noqa: E501


        :return: The postal_code of this OrgSetting.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this OrgSetting.


        :param postal_code: The postal_code of this OrgSetting.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def state(self):
        """Gets the state of this OrgSetting.  # noqa: E501


        :return: The state of this OrgSetting.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this OrgSetting.


        :param state: The state of this OrgSetting.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def status(self):
        """Gets the status of this OrgSetting.  # noqa: E501


        :return: The status of this OrgSetting.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrgSetting.


        :param status: The status of this OrgSetting.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def subdomain(self):
        """Gets the subdomain of this OrgSetting.  # noqa: E501


        :return: The subdomain of this OrgSetting.  # noqa: E501
        :rtype: str
        """
        return self._subdomain

    @subdomain.setter
    def subdomain(self, subdomain):
        """Sets the subdomain of this OrgSetting.


        :param subdomain: The subdomain of this OrgSetting.  # noqa: E501
        :type: str
        """

        self._subdomain = subdomain

    @property
    def support_phone_number(self):
        """Gets the support_phone_number of this OrgSetting.  # noqa: E501


        :return: The support_phone_number of this OrgSetting.  # noqa: E501
        :rtype: str
        """
        return self._support_phone_number

    @support_phone_number.setter
    def support_phone_number(self, support_phone_number):
        """Sets the support_phone_number of this OrgSetting.


        :param support_phone_number: The support_phone_number of this OrgSetting.  # noqa: E501
        :type: str
        """

        self._support_phone_number = support_phone_number

    @property
    def website(self):
        """Gets the website of this OrgSetting.  # noqa: E501


        :return: The website of this OrgSetting.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this OrgSetting.


        :param website: The website of this OrgSetting.  # noqa: E501
        :type: str
        """

        self._website = website

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
        if issubclass(OrgSetting, dict):
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
        if not isinstance(other, OrgSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
