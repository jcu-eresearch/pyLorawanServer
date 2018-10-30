# coding: utf-8

"""
    LoRa App Server REST API

     For more information about the usage of the LoRa App Server (REST) API, see [https://docs.loraserver.io/lora-app-server/api/](https://docs.loraserver.io/lora-app-server/api/).   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lorawan_server.api_client import ApiClient


class DownlinkQueueApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete(self, dev_eui, id, **kwargs):  # noqa: E501
        """Delete deletes an item from the queue.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete(dev_eui, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dev_eui: (required)
        :param str id: (required)
        :return: ApiDeleteDownlinkQueueItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_with_http_info(dev_eui, id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_with_http_info(dev_eui, id, **kwargs)  # noqa: E501
            return data

    def delete_with_http_info(self, dev_eui, id, **kwargs):  # noqa: E501
        """Delete deletes an item from the queue.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_with_http_info(dev_eui, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dev_eui: (required)
        :param str id: (required)
        :return: ApiDeleteDownlinkQueueItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dev_eui', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dev_eui' is set
        if ('dev_eui' not in params or
                params['dev_eui'] is None):
            raise ValueError("Missing the required parameter `dev_eui` when calling `delete`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dev_eui' in params:
            path_params['devEUI'] = params['dev_eui']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/nodes/{devEUI}/queue/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiDeleteDownlinkQueueItemResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def enqueue(self, dev_eui, body, **kwargs):  # noqa: E501
        """Enqueue adds the given item to the queue. When the node operates in Class-C mode, the data will be pushed directly to the network-server.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enqueue(dev_eui, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dev_eui: (required)
        :param ApiEnqueueDownlinkQueueItemRequest body: (required)
        :return: ApiEnqueueDownlinkQueueItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.enqueue_with_http_info(dev_eui, body, **kwargs)  # noqa: E501
        else:
            (data) = self.enqueue_with_http_info(dev_eui, body, **kwargs)  # noqa: E501
            return data

    def enqueue_with_http_info(self, dev_eui, body, **kwargs):  # noqa: E501
        """Enqueue adds the given item to the queue. When the node operates in Class-C mode, the data will be pushed directly to the network-server.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enqueue_with_http_info(dev_eui, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dev_eui: (required)
        :param ApiEnqueueDownlinkQueueItemRequest body: (required)
        :return: ApiEnqueueDownlinkQueueItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dev_eui', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enqueue" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dev_eui' is set
        if ('dev_eui' not in params or
                params['dev_eui'] is None):
            raise ValueError("Missing the required parameter `dev_eui` when calling `enqueue`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `enqueue`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dev_eui' in params:
            path_params['devEUI'] = params['dev_eui']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/nodes/{devEUI}/queue', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiEnqueueDownlinkQueueItemResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list(self, dev_eui, **kwargs):  # noqa: E501
        """List lists the items in the queue for the given node.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list(dev_eui, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dev_eui: (required)
        :return: ApiListDownlinkQueueItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_with_http_info(dev_eui, **kwargs)  # noqa: E501
        else:
            (data) = self.list_with_http_info(dev_eui, **kwargs)  # noqa: E501
            return data

    def list_with_http_info(self, dev_eui, **kwargs):  # noqa: E501
        """List lists the items in the queue for the given node.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_with_http_info(dev_eui, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dev_eui: (required)
        :return: ApiListDownlinkQueueItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dev_eui']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dev_eui' is set
        if ('dev_eui' not in params or
                params['dev_eui'] is None):
            raise ValueError("Missing the required parameter `dev_eui` when calling `list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dev_eui' in params:
            path_params['devEUI'] = params['dev_eui']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/nodes/{devEUI}/queue', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiListDownlinkQueueItemsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)