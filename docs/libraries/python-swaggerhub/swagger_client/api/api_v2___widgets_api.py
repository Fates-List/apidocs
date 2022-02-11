# coding: utf-8

"""
    Fates List

                 Current API: v2 beta 3             Default API: v2             API URL: https://api.fateslist.xyz             API Docs: https://apidocs.fateslist.xyz             Enum Reference: https://apidocs.fateslist.xyz/structures/enums.autogen           # noqa: E501

    OpenAPI spec version: 0.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class APIV2WidgetsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_widget(self, target_id, target_type, format, **kwargs):  # noqa: E501
        """Get Widget  # noqa: E501

            Returns a widget      **For colors (bgcolor, textcolor), use H for html hex instead of #. Example: H123456**      - cd - A custom description you wish to set for the widget      - desc_length - Set this to anything less than 0 to try and use full length (may 500), otherwise this sets the length of description to use.      **Using 0 for desc_length will disable description**      no_cache - If this is set to true, cache will not be used but will still be updated. If using cd, set this option to true and cache the image yourself     Note that no_cache is slow and may lead to ratelimits and/or your got being banned if used excessively       # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_widget(target_id, target_type, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int target_id: (required)
        :param ReviewType target_type: (required)
        :param WidgetFormat format: (required)
        :param str bgcolor:
        :param str textcolor:
        :param bool no_cache:
        :param str cd:
        :param int desc_length:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_widget_with_http_info(target_id, target_type, format, **kwargs)  # noqa: E501
        else:
            (data) = self.get_widget_with_http_info(target_id, target_type, format, **kwargs)  # noqa: E501
            return data

    def get_widget_with_http_info(self, target_id, target_type, format, **kwargs):  # noqa: E501
        """Get Widget  # noqa: E501

            Returns a widget      **For colors (bgcolor, textcolor), use H for html hex instead of #. Example: H123456**      - cd - A custom description you wish to set for the widget      - desc_length - Set this to anything less than 0 to try and use full length (may 500), otherwise this sets the length of description to use.      **Using 0 for desc_length will disable description**      no_cache - If this is set to true, cache will not be used but will still be updated. If using cd, set this option to true and cache the image yourself     Note that no_cache is slow and may lead to ratelimits and/or your got being banned if used excessively       # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_widget_with_http_info(target_id, target_type, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int target_id: (required)
        :param ReviewType target_type: (required)
        :param WidgetFormat format: (required)
        :param str bgcolor:
        :param str textcolor:
        :param bool no_cache:
        :param str cd:
        :param int desc_length:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['target_id', 'target_type', 'format', 'bgcolor', 'textcolor', 'no_cache', 'cd', 'desc_length']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_widget" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'target_id' is set
        if ('target_id' not in params or
                params['target_id'] is None):
            raise ValueError("Missing the required parameter `target_id` when calling `get_widget`")  # noqa: E501
        # verify the required parameter 'target_type' is set
        if ('target_type' not in params or
                params['target_type'] is None):
            raise ValueError("Missing the required parameter `target_type` when calling `get_widget`")  # noqa: E501
        # verify the required parameter 'format' is set
        if ('format' not in params or
                params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `get_widget`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'target_id' in params:
            path_params['target_id'] = params['target_id']  # noqa: E501

        query_params = []
        if 'target_type' in params:
            query_params.append(('target_type', params['target_type']))  # noqa: E501
        if 'format' in params:
            query_params.append(('format', params['format']))  # noqa: E501
        if 'bgcolor' in params:
            query_params.append(('bgcolor', params['bgcolor']))  # noqa: E501
        if 'textcolor' in params:
            query_params.append(('textcolor', params['textcolor']))  # noqa: E501
        if 'no_cache' in params:
            query_params.append(('no_cache', params['no_cache']))  # noqa: E501
        if 'cd' in params:
            query_params.append(('cd', params['cd']))  # noqa: E501
        if 'desc_length' in params:
            query_params.append(('desc_length', params['desc_length']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/widgets/{target_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
