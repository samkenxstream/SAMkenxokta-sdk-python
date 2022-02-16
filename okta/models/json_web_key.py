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

class JsonWebKey(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    swagger_types['links'] = 'dict(str, object)'
    swagger_types['alg'] = 'str'
    swagger_types['created'] = 'datetime'
    swagger_types['e'] = 'str'
    swagger_types['expires_at'] = 'datetime'
    swagger_types['key_ops'] = 'list[str]'
    swagger_types['kid'] = 'str'
    swagger_types['kty'] = 'str'
    swagger_types['last_updated'] = 'datetime'
    swagger_types['n'] = 'str'
    swagger_types['status'] = 'str'
    swagger_types['use'] = 'str'
    swagger_types['x_5_c'] = 'list[str]'
    swagger_types['x_5_t'] = 'str'
    swagger_types['x_5_t_s_256'] = 'str'
    swagger_types['x_5_u'] = 'str'

    attribute_map = {
        'links': '_links',
        'alg': 'alg',
        'created': 'created',
        'e': 'e',
        'expires_at': 'expiresAt',
        'key_ops': 'key_ops',
        'kid': 'kid',
        'kty': 'kty',
        'last_updated': 'lastUpdated',
        'n': 'n',
        'status': 'status',
        'use': 'use',
        'x_5_c': 'x5c',
        'x_5_t': 'x5t',
        'x_5_t_s_256': 'x5t#S256',
        'x_5_u': 'x5u'
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

    def set_attributes(self, links=None, alg=None, created=None, e=None, expires_at=None, key_ops=None, kid=None, kty=None, last_updated=None, n=None, status=None, use=None, x_5_c=None, x_5_t=None, x_5_t_s_256=None, x_5_u=None, **kwargs):  # noqa: E501
        """JsonWebKey - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._alg = None
        self._created = None
        self._e = None
        self._expires_at = None
        self._key_ops = None
        self._kid = None
        self._kty = None
        self._last_updated = None
        self._n = None
        self._status = None
        self._use = None
        self._x_5_c = None
        self._x_5_t = None
        self._x_5_t_s_256 = None
        self._x_5_u = None
        self.discriminator = None
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
        if alg is not None:
            if hasattr(models, self.swagger_types['alg']):
                nested_class = getattr(models, self.swagger_types['alg'])
                if isinstance(alg, nested_class):
                    self.alg = alg
                elif isinstance(alg, dict):
                    self.alg = nested_class.from_kwargs(**alg)
                else:
                    self.alg = alg
            else:
                self.alg = alg
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
        if e is not None:
            if hasattr(models, self.swagger_types['e']):
                nested_class = getattr(models, self.swagger_types['e'])
                if isinstance(e, nested_class):
                    self.e = e
                elif isinstance(e, dict):
                    self.e = nested_class.from_kwargs(**e)
                else:
                    self.e = e
            else:
                self.e = e
        if expires_at is not None:
            if hasattr(models, self.swagger_types['expires_at']):
                nested_class = getattr(models, self.swagger_types['expires_at'])
                if isinstance(expires_at, nested_class):
                    self.expires_at = expires_at
                elif isinstance(expires_at, dict):
                    self.expires_at = nested_class.from_kwargs(**expires_at)
                else:
                    self.expires_at = expires_at
            else:
                self.expires_at = expires_at
        if key_ops is not None:
            if hasattr(models, self.swagger_types['key_ops']):
                nested_class = getattr(models, self.swagger_types['key_ops'])
                if isinstance(key_ops, nested_class):
                    self.key_ops = key_ops
                elif isinstance(key_ops, dict):
                    self.key_ops = nested_class.from_kwargs(**key_ops)
                else:
                    self.key_ops = key_ops
            else:
                self.key_ops = key_ops
        if kid is not None:
            if hasattr(models, self.swagger_types['kid']):
                nested_class = getattr(models, self.swagger_types['kid'])
                if isinstance(kid, nested_class):
                    self.kid = kid
                elif isinstance(kid, dict):
                    self.kid = nested_class.from_kwargs(**kid)
                else:
                    self.kid = kid
            else:
                self.kid = kid
        if kty is not None:
            if hasattr(models, self.swagger_types['kty']):
                nested_class = getattr(models, self.swagger_types['kty'])
                if isinstance(kty, nested_class):
                    self.kty = kty
                elif isinstance(kty, dict):
                    self.kty = nested_class.from_kwargs(**kty)
                else:
                    self.kty = kty
            else:
                self.kty = kty
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
        if n is not None:
            if hasattr(models, self.swagger_types['n']):
                nested_class = getattr(models, self.swagger_types['n'])
                if isinstance(n, nested_class):
                    self.n = n
                elif isinstance(n, dict):
                    self.n = nested_class.from_kwargs(**n)
                else:
                    self.n = n
            else:
                self.n = n
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
        if use is not None:
            if hasattr(models, self.swagger_types['use']):
                nested_class = getattr(models, self.swagger_types['use'])
                if isinstance(use, nested_class):
                    self.use = use
                elif isinstance(use, dict):
                    self.use = nested_class.from_kwargs(**use)
                else:
                    self.use = use
            else:
                self.use = use
        if x_5_c is not None:
            if hasattr(models, self.swagger_types['x_5_c']):
                nested_class = getattr(models, self.swagger_types['x_5_c'])
                if isinstance(x_5_c, nested_class):
                    self.x_5_c = x_5_c
                elif isinstance(x_5_c, dict):
                    self.x_5_c = nested_class.from_kwargs(**x_5_c)
                else:
                    self.x_5_c = x_5_c
            else:
                self.x_5_c = x_5_c
        if x_5_t is not None:
            if hasattr(models, self.swagger_types['x_5_t']):
                nested_class = getattr(models, self.swagger_types['x_5_t'])
                if isinstance(x_5_t, nested_class):
                    self.x_5_t = x_5_t
                elif isinstance(x_5_t, dict):
                    self.x_5_t = nested_class.from_kwargs(**x_5_t)
                else:
                    self.x_5_t = x_5_t
            else:
                self.x_5_t = x_5_t
        if x_5_t_s_256 is not None:
            if hasattr(models, self.swagger_types['x_5_t_s_256']):
                nested_class = getattr(models, self.swagger_types['x_5_t_s_256'])
                if isinstance(x_5_t_s_256, nested_class):
                    self.x_5_t_s_256 = x_5_t_s_256
                elif isinstance(x_5_t_s_256, dict):
                    self.x_5_t_s_256 = nested_class.from_kwargs(**x_5_t_s_256)
                else:
                    self.x_5_t_s_256 = x_5_t_s_256
            else:
                self.x_5_t_s_256 = x_5_t_s_256
        if x_5_u is not None:
            if hasattr(models, self.swagger_types['x_5_u']):
                nested_class = getattr(models, self.swagger_types['x_5_u'])
                if isinstance(x_5_u, nested_class):
                    self.x_5_u = x_5_u
                elif isinstance(x_5_u, dict):
                    self.x_5_u = nested_class.from_kwargs(**x_5_u)
                else:
                    self.x_5_u = x_5_u
            else:
                self.x_5_u = x_5_u

    @property
    def links(self):
        """Gets the links of this JsonWebKey.  # noqa: E501


        :return: The links of this JsonWebKey.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this JsonWebKey.


        :param links: The links of this JsonWebKey.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def alg(self):
        """Gets the alg of this JsonWebKey.  # noqa: E501


        :return: The alg of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._alg

    @alg.setter
    def alg(self, alg):
        """Sets the alg of this JsonWebKey.


        :param alg: The alg of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._alg = alg

    @property
    def created(self):
        """Gets the created of this JsonWebKey.  # noqa: E501


        :return: The created of this JsonWebKey.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this JsonWebKey.


        :param created: The created of this JsonWebKey.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def e(self):
        """Gets the e of this JsonWebKey.  # noqa: E501


        :return: The e of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._e

    @e.setter
    def e(self, e):
        """Sets the e of this JsonWebKey.


        :param e: The e of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._e = e

    @property
    def expires_at(self):
        """Gets the expires_at of this JsonWebKey.  # noqa: E501


        :return: The expires_at of this JsonWebKey.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this JsonWebKey.


        :param expires_at: The expires_at of this JsonWebKey.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def key_ops(self):
        """Gets the key_ops of this JsonWebKey.  # noqa: E501


        :return: The key_ops of this JsonWebKey.  # noqa: E501
        :rtype: list[str]
        """
        return self._key_ops

    @key_ops.setter
    def key_ops(self, key_ops):
        """Sets the key_ops of this JsonWebKey.


        :param key_ops: The key_ops of this JsonWebKey.  # noqa: E501
        :type: list[str]
        """

        self._key_ops = key_ops

    @property
    def kid(self):
        """Gets the kid of this JsonWebKey.  # noqa: E501


        :return: The kid of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._kid

    @kid.setter
    def kid(self, kid):
        """Sets the kid of this JsonWebKey.


        :param kid: The kid of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._kid = kid

    @property
    def kty(self):
        """Gets the kty of this JsonWebKey.  # noqa: E501


        :return: The kty of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._kty

    @kty.setter
    def kty(self, kty):
        """Sets the kty of this JsonWebKey.


        :param kty: The kty of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._kty = kty

    @property
    def last_updated(self):
        """Gets the last_updated of this JsonWebKey.  # noqa: E501


        :return: The last_updated of this JsonWebKey.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this JsonWebKey.


        :param last_updated: The last_updated of this JsonWebKey.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def n(self):
        """Gets the n of this JsonWebKey.  # noqa: E501


        :return: The n of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._n

    @n.setter
    def n(self, n):
        """Sets the n of this JsonWebKey.


        :param n: The n of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._n = n

    @property
    def status(self):
        """Gets the status of this JsonWebKey.  # noqa: E501


        :return: The status of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JsonWebKey.


        :param status: The status of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def use(self):
        """Gets the use of this JsonWebKey.  # noqa: E501


        :return: The use of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._use

    @use.setter
    def use(self, use):
        """Sets the use of this JsonWebKey.


        :param use: The use of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._use = use

    @property
    def x_5_c(self):
        """Gets the x_5_c of this JsonWebKey.  # noqa: E501


        :return: The x_5_c of this JsonWebKey.  # noqa: E501
        :rtype: list[str]
        """
        return self._x_5_c

    @x_5_c.setter
    def x_5_c(self, x_5_c):
        """Sets the x_5_c of this JsonWebKey.


        :param x_5_c: The x_5_c of this JsonWebKey.  # noqa: E501
        :type: list[str]
        """

        self._x_5_c = x_5_c

    @property
    def x_5_t(self):
        """Gets the x_5_t of this JsonWebKey.  # noqa: E501


        :return: The x_5_t of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._x_5_t

    @x_5_t.setter
    def x_5_t(self, x_5_t):
        """Sets the x_5_t of this JsonWebKey.


        :param x_5_t: The x_5_t of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._x_5_t = x_5_t

    @property
    def x_5_t_s_256(self):
        """Gets the x_5_t_s_256 of this JsonWebKey.  # noqa: E501


        :return: The x_5_t_s_256 of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._x_5_t_s_256

    @x_5_t_s_256.setter
    def x_5_t_s_256(self, x_5_t_s_256):
        """Sets the x_5_t_s_256 of this JsonWebKey.


        :param x_5_t_s_256: The x_5_t_s_256 of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._x_5_t_s_256 = x_5_t_s_256

    @property
    def x_5_u(self):
        """Gets the x_5_u of this JsonWebKey.  # noqa: E501


        :return: The x_5_u of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._x_5_u

    @x_5_u.setter
    def x_5_u(self, x_5_u):
        """Sets the x_5_u of this JsonWebKey.


        :param x_5_u: The x_5_u of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._x_5_u = x_5_u

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
        if issubclass(JsonWebKey, dict):
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
        if not isinstance(other, JsonWebKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
