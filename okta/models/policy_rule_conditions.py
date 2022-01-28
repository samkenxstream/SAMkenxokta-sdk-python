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

class PolicyRuleConditions(object):
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
    swagger_types['app'] = 'AppAndInstancePolicyRuleCondition'
    swagger_types['apps'] = 'AppInstancePolicyRuleCondition'
    swagger_types['auth_context'] = 'PolicyRuleAuthContextCondition'
    swagger_types['auth_provider'] = 'PasswordPolicyAuthenticationProviderCondition'
    swagger_types['before_scheduled_action'] = 'BeforeScheduledActionPolicyRuleCondition'
    swagger_types['clients'] = 'ClientPolicyCondition'
    swagger_types['context'] = 'ContextPolicyRuleCondition'
    swagger_types['device'] = 'DevicePolicyRuleCondition'
    swagger_types['grant_types'] = 'GrantTypePolicyRuleCondition'
    swagger_types['groups'] = 'GroupPolicyRuleCondition'
    swagger_types['identity_provider'] = 'IdentityProviderPolicyRuleCondition'
    swagger_types['mdm_enrollment'] = 'MDMEnrollmentPolicyRuleCondition'
    swagger_types['network'] = 'PolicyNetworkCondition'
    swagger_types['people'] = 'PolicyPeopleCondition'
    swagger_types['platform'] = 'PlatformPolicyRuleCondition'
    swagger_types['risk'] = 'RiskPolicyRuleCondition'
    swagger_types['risk_score'] = 'RiskScorePolicyRuleCondition'
    swagger_types['scopes'] = 'OAuth2ScopesMediationPolicyRuleCondition'
    swagger_types['user_identifier'] = 'UserIdentifierPolicyRuleCondition'
    swagger_types['user_status'] = 'UserStatusPolicyRuleCondition'
    swagger_types['users'] = 'UserPolicyRuleCondition'

    attribute_map = {
        'app': 'app',
        'apps': 'apps',
        'auth_context': 'authContext',
        'auth_provider': 'authProvider',
        'before_scheduled_action': 'beforeScheduledAction',
        'clients': 'clients',
        'context': 'context',
        'device': 'device',
        'grant_types': 'grantTypes',
        'groups': 'groups',
        'identity_provider': 'identityProvider',
        'mdm_enrollment': 'mdmEnrollment',
        'network': 'network',
        'people': 'people',
        'platform': 'platform',
        'risk': 'risk',
        'risk_score': 'riskScore',
        'scopes': 'scopes',
        'user_identifier': 'userIdentifier',
        'user_status': 'userStatus',
        'users': 'users'
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

    def set_attributes(self, app=None, apps=None, auth_context=None, auth_provider=None, before_scheduled_action=None, clients=None, context=None, device=None, grant_types=None, groups=None, identity_provider=None, mdm_enrollment=None, network=None, people=None, platform=None, risk=None, risk_score=None, scopes=None, user_identifier=None, user_status=None, users=None, **kwargs):  # noqa: E501
        """PolicyRuleConditions - a model defined in Swagger"""  # noqa: E501
        self._app = None
        self._apps = None
        self._auth_context = None
        self._auth_provider = None
        self._before_scheduled_action = None
        self._clients = None
        self._context = None
        self._device = None
        self._grant_types = None
        self._groups = None
        self._identity_provider = None
        self._mdm_enrollment = None
        self._network = None
        self._people = None
        self._platform = None
        self._risk = None
        self._risk_score = None
        self._scopes = None
        self._user_identifier = None
        self._user_status = None
        self._users = None
        self.discriminator = None
        if app is not None:
            if hasattr(models, self.swagger_types['app']):
                nested_class = getattr(models, self.swagger_types['app'])
                if isinstance(app, nested_class):
                    self.app = app
                elif isinstance(app, dict):
                    self.app = nested_class.from_kwargs(**app)
                else:
                    self.app = app
            else:
                self.app = app
        if apps is not None:
            if hasattr(models, self.swagger_types['apps']):
                nested_class = getattr(models, self.swagger_types['apps'])
                if isinstance(apps, nested_class):
                    self.apps = apps
                elif isinstance(apps, dict):
                    self.apps = nested_class.from_kwargs(**apps)
                else:
                    self.apps = apps
            else:
                self.apps = apps
        if auth_context is not None:
            if hasattr(models, self.swagger_types['auth_context']):
                nested_class = getattr(models, self.swagger_types['auth_context'])
                if isinstance(auth_context, nested_class):
                    self.auth_context = auth_context
                elif isinstance(auth_context, dict):
                    self.auth_context = nested_class.from_kwargs(**auth_context)
                else:
                    self.auth_context = auth_context
            else:
                self.auth_context = auth_context
        if auth_provider is not None:
            if hasattr(models, self.swagger_types['auth_provider']):
                nested_class = getattr(models, self.swagger_types['auth_provider'])
                if isinstance(auth_provider, nested_class):
                    self.auth_provider = auth_provider
                elif isinstance(auth_provider, dict):
                    self.auth_provider = nested_class.from_kwargs(**auth_provider)
                else:
                    self.auth_provider = auth_provider
            else:
                self.auth_provider = auth_provider
        if before_scheduled_action is not None:
            if hasattr(models, self.swagger_types['before_scheduled_action']):
                nested_class = getattr(models, self.swagger_types['before_scheduled_action'])
                if isinstance(before_scheduled_action, nested_class):
                    self.before_scheduled_action = before_scheduled_action
                elif isinstance(before_scheduled_action, dict):
                    self.before_scheduled_action = nested_class.from_kwargs(**before_scheduled_action)
                else:
                    self.before_scheduled_action = before_scheduled_action
            else:
                self.before_scheduled_action = before_scheduled_action
        if clients is not None:
            if hasattr(models, self.swagger_types['clients']):
                nested_class = getattr(models, self.swagger_types['clients'])
                if isinstance(clients, nested_class):
                    self.clients = clients
                elif isinstance(clients, dict):
                    self.clients = nested_class.from_kwargs(**clients)
                else:
                    self.clients = clients
            else:
                self.clients = clients
        if context is not None:
            if hasattr(models, self.swagger_types['context']):
                nested_class = getattr(models, self.swagger_types['context'])
                if isinstance(context, nested_class):
                    self.context = context
                elif isinstance(context, dict):
                    self.context = nested_class.from_kwargs(**context)
                else:
                    self.context = context
            else:
                self.context = context
        if device is not None:
            if hasattr(models, self.swagger_types['device']):
                nested_class = getattr(models, self.swagger_types['device'])
                if isinstance(device, nested_class):
                    self.device = device
                elif isinstance(device, dict):
                    self.device = nested_class.from_kwargs(**device)
                else:
                    self.device = device
            else:
                self.device = device
        if grant_types is not None:
            if hasattr(models, self.swagger_types['grant_types']):
                nested_class = getattr(models, self.swagger_types['grant_types'])
                if isinstance(grant_types, nested_class):
                    self.grant_types = grant_types
                elif isinstance(grant_types, dict):
                    self.grant_types = nested_class.from_kwargs(**grant_types)
                else:
                    self.grant_types = grant_types
            else:
                self.grant_types = grant_types
        if groups is not None:
            if hasattr(models, self.swagger_types['groups']):
                nested_class = getattr(models, self.swagger_types['groups'])
                if isinstance(groups, nested_class):
                    self.groups = groups
                elif isinstance(groups, dict):
                    self.groups = nested_class.from_kwargs(**groups)
                else:
                    self.groups = groups
            else:
                self.groups = groups
        if identity_provider is not None:
            if hasattr(models, self.swagger_types['identity_provider']):
                nested_class = getattr(models, self.swagger_types['identity_provider'])
                if isinstance(identity_provider, nested_class):
                    self.identity_provider = identity_provider
                elif isinstance(identity_provider, dict):
                    self.identity_provider = nested_class.from_kwargs(**identity_provider)
                else:
                    self.identity_provider = identity_provider
            else:
                self.identity_provider = identity_provider
        if mdm_enrollment is not None:
            if hasattr(models, self.swagger_types['mdm_enrollment']):
                nested_class = getattr(models, self.swagger_types['mdm_enrollment'])
                if isinstance(mdm_enrollment, nested_class):
                    self.mdm_enrollment = mdm_enrollment
                elif isinstance(mdm_enrollment, dict):
                    self.mdm_enrollment = nested_class.from_kwargs(**mdm_enrollment)
                else:
                    self.mdm_enrollment = mdm_enrollment
            else:
                self.mdm_enrollment = mdm_enrollment
        if network is not None:
            if hasattr(models, self.swagger_types['network']):
                nested_class = getattr(models, self.swagger_types['network'])
                if isinstance(network, nested_class):
                    self.network = network
                elif isinstance(network, dict):
                    self.network = nested_class.from_kwargs(**network)
                else:
                    self.network = network
            else:
                self.network = network
        if people is not None:
            if hasattr(models, self.swagger_types['people']):
                nested_class = getattr(models, self.swagger_types['people'])
                if isinstance(people, nested_class):
                    self.people = people
                elif isinstance(people, dict):
                    self.people = nested_class.from_kwargs(**people)
                else:
                    self.people = people
            else:
                self.people = people
        if platform is not None:
            if hasattr(models, self.swagger_types['platform']):
                nested_class = getattr(models, self.swagger_types['platform'])
                if isinstance(platform, nested_class):
                    self.platform = platform
                elif isinstance(platform, dict):
                    self.platform = nested_class.from_kwargs(**platform)
                else:
                    self.platform = platform
            else:
                self.platform = platform
        if risk is not None:
            if hasattr(models, self.swagger_types['risk']):
                nested_class = getattr(models, self.swagger_types['risk'])
                if isinstance(risk, nested_class):
                    self.risk = risk
                elif isinstance(risk, dict):
                    self.risk = nested_class.from_kwargs(**risk)
                else:
                    self.risk = risk
            else:
                self.risk = risk
        if risk_score is not None:
            if hasattr(models, self.swagger_types['risk_score']):
                nested_class = getattr(models, self.swagger_types['risk_score'])
                if isinstance(risk_score, nested_class):
                    self.risk_score = risk_score
                elif isinstance(risk_score, dict):
                    self.risk_score = nested_class.from_kwargs(**risk_score)
                else:
                    self.risk_score = risk_score
            else:
                self.risk_score = risk_score
        if scopes is not None:
            if hasattr(models, self.swagger_types['scopes']):
                nested_class = getattr(models, self.swagger_types['scopes'])
                if isinstance(scopes, nested_class):
                    self.scopes = scopes
                elif isinstance(scopes, dict):
                    self.scopes = nested_class.from_kwargs(**scopes)
                else:
                    self.scopes = scopes
            else:
                self.scopes = scopes
        if user_identifier is not None:
            if hasattr(models, self.swagger_types['user_identifier']):
                nested_class = getattr(models, self.swagger_types['user_identifier'])
                if isinstance(user_identifier, nested_class):
                    self.user_identifier = user_identifier
                elif isinstance(user_identifier, dict):
                    self.user_identifier = nested_class.from_kwargs(**user_identifier)
                else:
                    self.user_identifier = user_identifier
            else:
                self.user_identifier = user_identifier
        if user_status is not None:
            if hasattr(models, self.swagger_types['user_status']):
                nested_class = getattr(models, self.swagger_types['user_status'])
                if isinstance(user_status, nested_class):
                    self.user_status = user_status
                elif isinstance(user_status, dict):
                    self.user_status = nested_class.from_kwargs(**user_status)
                else:
                    self.user_status = user_status
            else:
                self.user_status = user_status
        if users is not None:
            if hasattr(models, self.swagger_types['users']):
                nested_class = getattr(models, self.swagger_types['users'])
                if isinstance(users, nested_class):
                    self.users = users
                elif isinstance(users, dict):
                    self.users = nested_class.from_kwargs(**users)
                else:
                    self.users = users
            else:
                self.users = users

    @property
    def app(self):
        """Gets the app of this PolicyRuleConditions.  # noqa: E501


        :return: The app of this PolicyRuleConditions.  # noqa: E501
        :rtype: AppAndInstancePolicyRuleCondition
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this PolicyRuleConditions.


        :param app: The app of this PolicyRuleConditions.  # noqa: E501
        :type: AppAndInstancePolicyRuleCondition
        """

        self._app = app

    @property
    def apps(self):
        """Gets the apps of this PolicyRuleConditions.  # noqa: E501


        :return: The apps of this PolicyRuleConditions.  # noqa: E501
        :rtype: AppInstancePolicyRuleCondition
        """
        return self._apps

    @apps.setter
    def apps(self, apps):
        """Sets the apps of this PolicyRuleConditions.


        :param apps: The apps of this PolicyRuleConditions.  # noqa: E501
        :type: AppInstancePolicyRuleCondition
        """

        self._apps = apps

    @property
    def auth_context(self):
        """Gets the auth_context of this PolicyRuleConditions.  # noqa: E501


        :return: The auth_context of this PolicyRuleConditions.  # noqa: E501
        :rtype: PolicyRuleAuthContextCondition
        """
        return self._auth_context

    @auth_context.setter
    def auth_context(self, auth_context):
        """Sets the auth_context of this PolicyRuleConditions.


        :param auth_context: The auth_context of this PolicyRuleConditions.  # noqa: E501
        :type: PolicyRuleAuthContextCondition
        """

        self._auth_context = auth_context

    @property
    def auth_provider(self):
        """Gets the auth_provider of this PolicyRuleConditions.  # noqa: E501


        :return: The auth_provider of this PolicyRuleConditions.  # noqa: E501
        :rtype: PasswordPolicyAuthenticationProviderCondition
        """
        return self._auth_provider

    @auth_provider.setter
    def auth_provider(self, auth_provider):
        """Sets the auth_provider of this PolicyRuleConditions.


        :param auth_provider: The auth_provider of this PolicyRuleConditions.  # noqa: E501
        :type: PasswordPolicyAuthenticationProviderCondition
        """

        self._auth_provider = auth_provider

    @property
    def before_scheduled_action(self):
        """Gets the before_scheduled_action of this PolicyRuleConditions.  # noqa: E501


        :return: The before_scheduled_action of this PolicyRuleConditions.  # noqa: E501
        :rtype: BeforeScheduledActionPolicyRuleCondition
        """
        return self._before_scheduled_action

    @before_scheduled_action.setter
    def before_scheduled_action(self, before_scheduled_action):
        """Sets the before_scheduled_action of this PolicyRuleConditions.


        :param before_scheduled_action: The before_scheduled_action of this PolicyRuleConditions.  # noqa: E501
        :type: BeforeScheduledActionPolicyRuleCondition
        """

        self._before_scheduled_action = before_scheduled_action

    @property
    def clients(self):
        """Gets the clients of this PolicyRuleConditions.  # noqa: E501


        :return: The clients of this PolicyRuleConditions.  # noqa: E501
        :rtype: ClientPolicyCondition
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this PolicyRuleConditions.


        :param clients: The clients of this PolicyRuleConditions.  # noqa: E501
        :type: ClientPolicyCondition
        """

        self._clients = clients

    @property
    def context(self):
        """Gets the context of this PolicyRuleConditions.  # noqa: E501


        :return: The context of this PolicyRuleConditions.  # noqa: E501
        :rtype: ContextPolicyRuleCondition
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this PolicyRuleConditions.


        :param context: The context of this PolicyRuleConditions.  # noqa: E501
        :type: ContextPolicyRuleCondition
        """

        self._context = context

    @property
    def device(self):
        """Gets the device of this PolicyRuleConditions.  # noqa: E501


        :return: The device of this PolicyRuleConditions.  # noqa: E501
        :rtype: DevicePolicyRuleCondition
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this PolicyRuleConditions.


        :param device: The device of this PolicyRuleConditions.  # noqa: E501
        :type: DevicePolicyRuleCondition
        """

        self._device = device

    @property
    def grant_types(self):
        """Gets the grant_types of this PolicyRuleConditions.  # noqa: E501


        :return: The grant_types of this PolicyRuleConditions.  # noqa: E501
        :rtype: GrantTypePolicyRuleCondition
        """
        return self._grant_types

    @grant_types.setter
    def grant_types(self, grant_types):
        """Sets the grant_types of this PolicyRuleConditions.


        :param grant_types: The grant_types of this PolicyRuleConditions.  # noqa: E501
        :type: GrantTypePolicyRuleCondition
        """

        self._grant_types = grant_types

    @property
    def groups(self):
        """Gets the groups of this PolicyRuleConditions.  # noqa: E501


        :return: The groups of this PolicyRuleConditions.  # noqa: E501
        :rtype: GroupPolicyRuleCondition
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this PolicyRuleConditions.


        :param groups: The groups of this PolicyRuleConditions.  # noqa: E501
        :type: GroupPolicyRuleCondition
        """

        self._groups = groups

    @property
    def identity_provider(self):
        """Gets the identity_provider of this PolicyRuleConditions.  # noqa: E501


        :return: The identity_provider of this PolicyRuleConditions.  # noqa: E501
        :rtype: IdentityProviderPolicyRuleCondition
        """
        return self._identity_provider

    @identity_provider.setter
    def identity_provider(self, identity_provider):
        """Sets the identity_provider of this PolicyRuleConditions.


        :param identity_provider: The identity_provider of this PolicyRuleConditions.  # noqa: E501
        :type: IdentityProviderPolicyRuleCondition
        """

        self._identity_provider = identity_provider

    @property
    def mdm_enrollment(self):
        """Gets the mdm_enrollment of this PolicyRuleConditions.  # noqa: E501


        :return: The mdm_enrollment of this PolicyRuleConditions.  # noqa: E501
        :rtype: MDMEnrollmentPolicyRuleCondition
        """
        return self._mdm_enrollment

    @mdm_enrollment.setter
    def mdm_enrollment(self, mdm_enrollment):
        """Sets the mdm_enrollment of this PolicyRuleConditions.


        :param mdm_enrollment: The mdm_enrollment of this PolicyRuleConditions.  # noqa: E501
        :type: MDMEnrollmentPolicyRuleCondition
        """

        self._mdm_enrollment = mdm_enrollment

    @property
    def network(self):
        """Gets the network of this PolicyRuleConditions.  # noqa: E501


        :return: The network of this PolicyRuleConditions.  # noqa: E501
        :rtype: PolicyNetworkCondition
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this PolicyRuleConditions.


        :param network: The network of this PolicyRuleConditions.  # noqa: E501
        :type: PolicyNetworkCondition
        """

        self._network = network

    @property
    def people(self):
        """Gets the people of this PolicyRuleConditions.  # noqa: E501


        :return: The people of this PolicyRuleConditions.  # noqa: E501
        :rtype: PolicyPeopleCondition
        """
        return self._people

    @people.setter
    def people(self, people):
        """Sets the people of this PolicyRuleConditions.


        :param people: The people of this PolicyRuleConditions.  # noqa: E501
        :type: PolicyPeopleCondition
        """

        self._people = people

    @property
    def platform(self):
        """Gets the platform of this PolicyRuleConditions.  # noqa: E501


        :return: The platform of this PolicyRuleConditions.  # noqa: E501
        :rtype: PlatformPolicyRuleCondition
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this PolicyRuleConditions.


        :param platform: The platform of this PolicyRuleConditions.  # noqa: E501
        :type: PlatformPolicyRuleCondition
        """

        self._platform = platform

    @property
    def risk(self):
        """Gets the risk of this PolicyRuleConditions.  # noqa: E501


        :return: The risk of this PolicyRuleConditions.  # noqa: E501
        :rtype: RiskPolicyRuleCondition
        """
        return self._risk

    @risk.setter
    def risk(self, risk):
        """Sets the risk of this PolicyRuleConditions.


        :param risk: The risk of this PolicyRuleConditions.  # noqa: E501
        :type: RiskPolicyRuleCondition
        """

        self._risk = risk

    @property
    def risk_score(self):
        """Gets the risk_score of this PolicyRuleConditions.  # noqa: E501


        :return: The risk_score of this PolicyRuleConditions.  # noqa: E501
        :rtype: RiskScorePolicyRuleCondition
        """
        return self._risk_score

    @risk_score.setter
    def risk_score(self, risk_score):
        """Sets the risk_score of this PolicyRuleConditions.


        :param risk_score: The risk_score of this PolicyRuleConditions.  # noqa: E501
        :type: RiskScorePolicyRuleCondition
        """

        self._risk_score = risk_score

    @property
    def scopes(self):
        """Gets the scopes of this PolicyRuleConditions.  # noqa: E501


        :return: The scopes of this PolicyRuleConditions.  # noqa: E501
        :rtype: OAuth2ScopesMediationPolicyRuleCondition
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this PolicyRuleConditions.


        :param scopes: The scopes of this PolicyRuleConditions.  # noqa: E501
        :type: OAuth2ScopesMediationPolicyRuleCondition
        """

        self._scopes = scopes

    @property
    def user_identifier(self):
        """Gets the user_identifier of this PolicyRuleConditions.  # noqa: E501


        :return: The user_identifier of this PolicyRuleConditions.  # noqa: E501
        :rtype: UserIdentifierPolicyRuleCondition
        """
        return self._user_identifier

    @user_identifier.setter
    def user_identifier(self, user_identifier):
        """Sets the user_identifier of this PolicyRuleConditions.


        :param user_identifier: The user_identifier of this PolicyRuleConditions.  # noqa: E501
        :type: UserIdentifierPolicyRuleCondition
        """

        self._user_identifier = user_identifier

    @property
    def user_status(self):
        """Gets the user_status of this PolicyRuleConditions.  # noqa: E501


        :return: The user_status of this PolicyRuleConditions.  # noqa: E501
        :rtype: UserStatusPolicyRuleCondition
        """
        return self._user_status

    @user_status.setter
    def user_status(self, user_status):
        """Sets the user_status of this PolicyRuleConditions.


        :param user_status: The user_status of this PolicyRuleConditions.  # noqa: E501
        :type: UserStatusPolicyRuleCondition
        """

        self._user_status = user_status

    @property
    def users(self):
        """Gets the users of this PolicyRuleConditions.  # noqa: E501


        :return: The users of this PolicyRuleConditions.  # noqa: E501
        :rtype: UserPolicyRuleCondition
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this PolicyRuleConditions.


        :param users: The users of this PolicyRuleConditions.  # noqa: E501
        :type: UserPolicyRuleCondition
        """

        self._users = users

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
        if issubclass(PolicyRuleConditions, dict):
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
        if not isinstance(other, PolicyRuleConditions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
