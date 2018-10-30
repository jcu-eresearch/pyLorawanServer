# swagger_client.NodeApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate**](NodeApi.md#activate) | **POST** /api/nodes/{devEUI}/activation | Activate (re)activates the node (only when ABP is set to true).
[**create**](NodeApi.md#create) | **POST** /api/nodes | Create creates the given node.
[**delete**](NodeApi.md#delete) | **DELETE** /api/nodes/{devEUI} | Delete deletes the node matching the given DevEUI.
[**get**](NodeApi.md#get) | **GET** /api/nodes/{devEUI} | Get returns the node for the requested DevEUI.
[**get_activation**](NodeApi.md#get_activation) | **GET** /api/nodes/{devEUI}/activation | GetActivation returns the current activation details of the node (OTAA and ABP).
[**get_frame_logs**](NodeApi.md#get_frame_logs) | **GET** /api/nodes/{devEUI}/frames | GetFrameLogs returns the uplink / downlink frame log for the given DevEUI.
[**get_random_dev_addr**](NodeApi.md#get_random_dev_addr) | **POST** /api/nodes/getRandomDevAddr | GetRandomDevAddr returns a random DevAddr taking the NwkID prefix into account.
[**list_by_application_id**](NodeApi.md#list_by_application_id) | **GET** /api/applications/{applicationID}/nodes | ListByApplicationID lists the nodes by the given application ID, sorted by the name of the node.
[**update**](NodeApi.md#update) | **PUT** /api/nodes/{devEUI} | Update updates the node matching the given DevEUI.


# **activate**
> ApiActivateNodeResponse activate(dev_eui, body)

Activate (re)activates the node (only when ABP is set to true).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NodeApi()
dev_eui = 'dev_eui_example' # str | 
body = swagger_client.ApiActivateNodeRequest() # ApiActivateNodeRequest | 

try:
    # Activate (re)activates the node (only when ABP is set to true).
    api_response = api_instance.activate(dev_eui, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->activate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dev_eui** | **str**|  | 
 **body** | [**ApiActivateNodeRequest**](ApiActivateNodeRequest.md)|  | 

### Return type

[**ApiActivateNodeResponse**](ApiActivateNodeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> ApiCreateNodeResponse create(body)

Create creates the given node.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NodeApi()
body = swagger_client.ApiCreateNodeRequest() # ApiCreateNodeRequest | 

try:
    # Create creates the given node.
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiCreateNodeRequest**](ApiCreateNodeRequest.md)|  | 

### Return type

[**ApiCreateNodeResponse**](ApiCreateNodeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> ApiDeleteNodeResponse delete(dev_eui)

Delete deletes the node matching the given DevEUI.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NodeApi()
dev_eui = 'dev_eui_example' # str | 

try:
    # Delete deletes the node matching the given DevEUI.
    api_response = api_instance.delete(dev_eui)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dev_eui** | **str**|  | 

### Return type

[**ApiDeleteNodeResponse**](ApiDeleteNodeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ApiGetNodeResponse get(dev_eui)

Get returns the node for the requested DevEUI.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NodeApi()
dev_eui = 'dev_eui_example' # str | 

try:
    # Get returns the node for the requested DevEUI.
    api_response = api_instance.get(dev_eui)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dev_eui** | **str**|  | 

### Return type

[**ApiGetNodeResponse**](ApiGetNodeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activation**
> ApiGetNodeActivationResponse get_activation(dev_eui)

GetActivation returns the current activation details of the node (OTAA and ABP).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NodeApi()
dev_eui = 'dev_eui_example' # str | 

try:
    # GetActivation returns the current activation details of the node (OTAA and ABP).
    api_response = api_instance.get_activation(dev_eui)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->get_activation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dev_eui** | **str**|  | 

### Return type

[**ApiGetNodeActivationResponse**](ApiGetNodeActivationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_frame_logs**
> ApiGetFrameLogsResponse get_frame_logs(dev_eui, limit=limit, offset=offset)

GetFrameLogs returns the uplink / downlink frame log for the given DevEUI.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NodeApi()
dev_eui = 'dev_eui_example' # str | 
limit = 'limit_example' # str | Max number of frames to return in the result-set. (optional)
offset = 'offset_example' # str | Offset of the result-set (for pagination). (optional)

try:
    # GetFrameLogs returns the uplink / downlink frame log for the given DevEUI.
    api_response = api_instance.get_frame_logs(dev_eui, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->get_frame_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dev_eui** | **str**|  | 
 **limit** | **str**| Max number of frames to return in the result-set. | [optional] 
 **offset** | **str**| Offset of the result-set (for pagination). | [optional] 

### Return type

[**ApiGetFrameLogsResponse**](ApiGetFrameLogsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_random_dev_addr**
> ApiGetRandomDevAddrResponse get_random_dev_addr()

GetRandomDevAddr returns a random DevAddr taking the NwkID prefix into account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NodeApi()

try:
    # GetRandomDevAddr returns a random DevAddr taking the NwkID prefix into account.
    api_response = api_instance.get_random_dev_addr()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->get_random_dev_addr: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiGetRandomDevAddrResponse**](ApiGetRandomDevAddrResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_by_application_id**
> ApiListNodeResponse list_by_application_id(application_id, limit=limit, offset=offset, search=search)

ListByApplicationID lists the nodes by the given application ID, sorted by the name of the node.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NodeApi()
application_id = 'application_id_example' # str | 
limit = 'limit_example' # str | Max number of nodes to return in the result-set. (optional)
offset = 'offset_example' # str | Offset of the result-set (for pagination). (optional)
search = 'search_example' # str | Search against name or DevEUI. (optional)

try:
    # ListByApplicationID lists the nodes by the given application ID, sorted by the name of the node.
    api_response = api_instance.list_by_application_id(application_id, limit=limit, offset=offset, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->list_by_application_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **limit** | **str**| Max number of nodes to return in the result-set. | [optional] 
 **offset** | **str**| Offset of the result-set (for pagination). | [optional] 
 **search** | **str**| Search against name or DevEUI. | [optional] 

### Return type

[**ApiListNodeResponse**](ApiListNodeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ApiUpdateNodeResponse update(dev_eui, body)

Update updates the node matching the given DevEUI.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NodeApi()
dev_eui = 'dev_eui_example' # str | 
body = swagger_client.ApiUpdateNodeRequest() # ApiUpdateNodeRequest | 

try:
    # Update updates the node matching the given DevEUI.
    api_response = api_instance.update(dev_eui, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dev_eui** | **str**|  | 
 **body** | [**ApiUpdateNodeRequest**](ApiUpdateNodeRequest.md)|  | 

### Return type

[**ApiUpdateNodeResponse**](ApiUpdateNodeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

