# lorawan_client.DownlinkQueueApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](DownlinkQueueApi.md#delete) | **DELETE** /api/nodes/{devEUI}/queue/{id} | Delete deletes an item from the queue.
[**enqueue**](DownlinkQueueApi.md#enqueue) | **POST** /api/nodes/{devEUI}/queue | Enqueue adds the given item to the queue. When the node operates in Class-C mode, the data will be pushed directly to the network-server.
[**list**](DownlinkQueueApi.md#list) | **GET** /api/nodes/{devEUI}/queue | List lists the items in the queue for the given node.


# **delete**
> ApiDeleteDownlinkQueueItemResponse delete(dev_eui, id)

Delete deletes an item from the queue.

### Example
```python
from __future__ import print_function
import time
import lorawan_client
from lorawan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lorawan_client.DownlinkQueueApi()
dev_eui = 'dev_eui_example' # str | 
id = 'id_example' # str | 

try:
    # Delete deletes an item from the queue.
    api_response = api_instance.delete(dev_eui, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownlinkQueueApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dev_eui** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**ApiDeleteDownlinkQueueItemResponse**](ApiDeleteDownlinkQueueItemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enqueue**
> ApiEnqueueDownlinkQueueItemResponse enqueue(dev_eui, body)

Enqueue adds the given item to the queue. When the node operates in Class-C mode, the data will be pushed directly to the network-server.

### Example
```python
from __future__ import print_function
import time
import lorawan_client
from lorawan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lorawan_client.DownlinkQueueApi()
dev_eui = 'dev_eui_example' # str | 
body = lorawan_client.ApiEnqueueDownlinkQueueItemRequest() # ApiEnqueueDownlinkQueueItemRequest | 

try:
    # Enqueue adds the given item to the queue. When the node operates in Class-C mode, the data will be pushed directly to the network-server.
    api_response = api_instance.enqueue(dev_eui, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownlinkQueueApi->enqueue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dev_eui** | **str**|  | 
 **body** | [**ApiEnqueueDownlinkQueueItemRequest**](ApiEnqueueDownlinkQueueItemRequest.md)|  | 

### Return type

[**ApiEnqueueDownlinkQueueItemResponse**](ApiEnqueueDownlinkQueueItemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ApiListDownlinkQueueItemsResponse list(dev_eui)

List lists the items in the queue for the given node.

### Example
```python
from __future__ import print_function
import time
import lorawan_client
from lorawan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lorawan_client.DownlinkQueueApi()
dev_eui = 'dev_eui_example' # str | 

try:
    # List lists the items in the queue for the given node.
    api_response = api_instance.list(dev_eui)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownlinkQueueApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dev_eui** | **str**|  | 

### Return type

[**ApiListDownlinkQueueItemsResponse**](ApiListDownlinkQueueItemsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

