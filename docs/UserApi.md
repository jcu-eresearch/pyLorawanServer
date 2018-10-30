# lorawan_client.UserApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](UserApi.md#create) | **POST** /api/users | Create a new user.
[**delete**](UserApi.md#delete) | **DELETE** /api/users/{id} | Delete a user.
[**get**](UserApi.md#get) | **GET** /api/users/{id} | Get data for a particular user.
[**list**](UserApi.md#list) | **GET** /api/users | Get user list.
[**update**](UserApi.md#update) | **PUT** /api/users/{id} | Update an existing user.
[**update_password**](UserApi.md#update_password) | **PUT** /api/users/{id}/password | UpdatePassword updates a password.


# **create**
> ApiAddUserResponse create(body)

Create a new user.

### Example
```python
from __future__ import print_function
import time
import lorawan_client
from lorawan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lorawan_client.UserApi()
body = lorawan_client.ApiAddUserRequest() # ApiAddUserRequest | 

try:
    # Create a new user.
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiAddUserRequest**](ApiAddUserRequest.md)|  | 

### Return type

[**ApiAddUserResponse**](ApiAddUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> ApiUserEmptyResponse delete(id)

Delete a user.

### Example
```python
from __future__ import print_function
import time
import lorawan_client
from lorawan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lorawan_client.UserApi()
id = 'id_example' # str | 

try:
    # Delete a user.
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApiUserEmptyResponse**](ApiUserEmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ApiGetUserResponse get(id)

Get data for a particular user.

### Example
```python
from __future__ import print_function
import time
import lorawan_client
from lorawan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lorawan_client.UserApi()
id = 'id_example' # str | 

try:
    # Get data for a particular user.
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApiGetUserResponse**](ApiGetUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ApiListUserResponse list(limit=limit, offset=offset, search=search)

Get user list.

### Example
```python
from __future__ import print_function
import time
import lorawan_client
from lorawan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lorawan_client.UserApi()
limit = 56 # int | Max number of user to return in the result-set. (optional)
offset = 56 # int | Offset in the result-set (for pagination). (optional)
search = 'search_example' # str | When provided, the given string will be used to search on username. (optional)

try:
    # Get user list.
    api_response = api_instance.list(limit=limit, offset=offset, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max number of user to return in the result-set. | [optional] 
 **offset** | **int**| Offset in the result-set (for pagination). | [optional] 
 **search** | **str**| When provided, the given string will be used to search on username. | [optional] 

### Return type

[**ApiListUserResponse**](ApiListUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ApiUserEmptyResponse update(id, body)

Update an existing user.

### Example
```python
from __future__ import print_function
import time
import lorawan_client
from lorawan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lorawan_client.UserApi()
id = 'id_example' # str | 
body = lorawan_client.ApiUpdateUserRequest() # ApiUpdateUserRequest | 

try:
    # Update an existing user.
    api_response = api_instance.update(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**ApiUpdateUserRequest**](ApiUpdateUserRequest.md)|  | 

### Return type

[**ApiUserEmptyResponse**](ApiUserEmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_password**
> ApiUserEmptyResponse update_password(id, body)

UpdatePassword updates a password.

### Example
```python
from __future__ import print_function
import time
import lorawan_client
from lorawan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lorawan_client.UserApi()
id = 'id_example' # str | 
body = lorawan_client.ApiUpdateUserPasswordRequest() # ApiUpdateUserPasswordRequest | 

try:
    # UpdatePassword updates a password.
    api_response = api_instance.update_password(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**ApiUpdateUserPasswordRequest**](ApiUpdateUserPasswordRequest.md)|  | 

### Return type

[**ApiUserEmptyResponse**](ApiUserEmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

