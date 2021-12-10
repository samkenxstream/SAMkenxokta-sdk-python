# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from okta.swagger_api_client import ApiClient


class Authenticator(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def activate_authenticator(self, authenticator_id, **kwargs):  # noqa: E501
        """Activate Authenticator  # noqa: E501

        Activates an authenticator by `authenticatorId`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activate_authenticator(authenticator_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authenticator_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.activate_authenticator_with_http_info(authenticator_id, **kwargs)  # noqa: E501
        else:
            (data) = self.activate_authenticator_with_http_info(authenticator_id, **kwargs)  # noqa: E501
            return data

    def activate_authenticator_with_http_info(self, authenticator_id, **kwargs):  # noqa: E501
        """Activate Authenticator  # noqa: E501

        Activates an authenticator by `authenticatorId`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activate_authenticator_with_http_info(authenticator_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authenticator_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authenticator_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method activate_authenticator" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authenticator_id' is set
        if ('authenticator_id' not in params or
                params['authenticator_id'] is None):
            raise ValueError("Missing the required parameter `authenticator_id` when calling `activate_authenticator`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'authenticator_id' in params:
            path_params['authenticatorId'] = params['authenticator_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/authenticators/{authenticatorId}/lifecycle/activate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def deactivate_authenticator(self, authenticator_id, **kwargs):  # noqa: E501
        """Deactivate Authenticator  # noqa: E501

        Deactivates an authenticator by `authenticatorId`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deactivate_authenticator(authenticator_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authenticator_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deactivate_authenticator_with_http_info(authenticator_id, **kwargs)  # noqa: E501
        else:
            (data) = self.deactivate_authenticator_with_http_info(authenticator_id, **kwargs)  # noqa: E501
            return data

    def deactivate_authenticator_with_http_info(self, authenticator_id, **kwargs):  # noqa: E501
        """Deactivate Authenticator  # noqa: E501

        Deactivates an authenticator by `authenticatorId`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deactivate_authenticator_with_http_info(authenticator_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authenticator_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authenticator_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deactivate_authenticator" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authenticator_id' is set
        if ('authenticator_id' not in params or
                params['authenticator_id'] is None):
            raise ValueError("Missing the required parameter `authenticator_id` when calling `deactivate_authenticator`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'authenticator_id' in params:
            path_params['authenticatorId'] = params['authenticator_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/authenticators/{authenticatorId}/lifecycle/deactivate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_authenticator(self, authenticator_id, **kwargs):  # noqa: E501
        """Get Authenticator  # noqa: E501

        Fetches an authenticator from your Okta organization by `authenticatorId`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_authenticator(authenticator_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authenticator_id: (required)
        :return: Authenticator
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_authenticator_with_http_info(authenticator_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_authenticator_with_http_info(authenticator_id, **kwargs)  # noqa: E501
            return data

    def get_authenticator_with_http_info(self, authenticator_id, **kwargs):  # noqa: E501
        """Get Authenticator  # noqa: E501

        Fetches an authenticator from your Okta organization by `authenticatorId`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_authenticator_with_http_info(authenticator_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authenticator_id: (required)
        :return: Authenticator
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authenticator_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_authenticator" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authenticator_id' is set
        if ('authenticator_id' not in params or
                params['authenticator_id'] is None):
            raise ValueError("Missing the required parameter `authenticator_id` when calling `get_authenticator`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'authenticator_id' in params:
            path_params['authenticatorId'] = params['authenticator_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/authenticators/{authenticatorId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Authenticator',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_authenticators(self, **kwargs):  # noqa: E501
        """List Authenticators  # noqa: E501

        Enumerates authenticators in your organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_authenticators(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Authenticator]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_authenticators_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_authenticators_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_authenticators_with_http_info(self, **kwargs):  # noqa: E501
        """List Authenticators  # noqa: E501

        Enumerates authenticators in your organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_authenticators_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Authenticator]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_authenticators" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/authenticators', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Authenticator]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
