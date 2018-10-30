# lorawan_client.OrganizationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user**](OrganizationApi.md#add_user) | **POST** /api/organizations/{id}/users | Add a new user to an organization.
[**create**](OrganizationApi.md#create) | **POST** /api/organizations | Create a new organization.
[**delete**](OrganizationApi.md#delete) | **DELETE** /api/organizations/{id} | Delete an organization.
[**delete_user**](OrganizationApi.md#delete_user) | **DELETE** /api/organizations/{id}/users/{userID} | Delete a user from an organization.
[**get**](OrganizationApi.md#get) | **GET** /api/organizations/{id} | Get data for a particular organization.
[**get_user**](OrganizationApi.md#get_user) | **GET** /api/organizations/{id}/users/{userID} | Get data for a particular organization user.
[**list**](OrganizationApi.md#list) | **GET** /api/organizations | Get organization list.
[**list_users**](OrganizationApi.md#list_users) | **GET** /api/organizations/{id}/users | Get organization&#39;s user list.
[**update**](OrganizationApi.md#update) | **PUT** /api/organizations/{id} | Update an existing organization.
[**update_user**](OrganizationApi.md#update_user) | **PUT** /api/organizations/{id}/users/{userID} | Update a user in an organization.


# **add_user**
> ApiOrganizationEmptyResponse add_user(id, body)

Add a new user to an organization.

### Example
```python
from __future__ import print_function
import time
import lorawan_client
from lorawan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lorawan_client.OrganizationApi()
id = 'id_example' # str | 
body = lorawan_client.ApiOrganizationUserRequest() # ApiOrganizationUserRequest | 

try:
    # Add a new user to an organization.
    api_response = api_instance.add_user(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->add_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**ApiOrganizationUserRequest**](ApiOrganizationUserRequest.md)|  | 

### Return type

[**ApiOrganizationEmptyResponse**](ApiOrganizationEmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> ApiCreateOrganizationResponse create(body)

Create a new organization.

### Example
```python
from __future__ import print_function
import time
import lorawan_client
from lorawan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lorawan_client.OrganizationApi()
body = lorawan_client.ApiCreateOrganizationRequest() # ApiCreateOrganizationRequest | 

try:
    # Create a new organization.
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiCreateOrganizationRequest**](ApiCreateOrganizationRequest.md)|  | 

### Return type

[**ApiCreateOrganizationResponse**](ApiCreateOrganizationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> ApiOrganizationEmptyResponse delete(id)

Delete an organization.

### Example
```python
from __future__ import print_function
import time
import lorawan_client
from lorawan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lorawan_client.OrganizationApi()
id = 'id_example' # str | 

try:
    # Delete an organization.
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApiOrganizationEmptyResponse**](ApiOrganizationEmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> ApiOrganizationEmptyResponse delete_user(id, user_id)

Delete a user from an organization.

### Example
```python
from __future__ import print_function
import time
import lorawan_client
from lorawan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lorawan_client.OrganizationApi()
id = 'id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # Delete a user from an organization.
    api_response = api_instance.delete_user(id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**ApiOrganizationEmptyResponse**](ApiOrganizationEmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ApiGetOrganizationResponse get(id)

Get data for a particular organization.

### Example
```python
from __future__ import print_function
import time
import lorawan_client
from lorawan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lorawan_client.OrganizationApi()
id = 'id_example' # str | 

try:
    # Get data for a particular organization.
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApiGetOrganizationResponse**](ApiGetOrganizationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> ApiGetOrganizationUserResponse get_user(id, user_id)

Get data for a particular organization user.

### Example
```python
from __future__ import print_function
import time
import lorawan_client
from lorawan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lorawan_client.OrganizationApi()
id = 'id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # Get data for a particular organization user.
    api_response = api_instance.get_user(id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**ApiGetOrganizationUserResponse**](ApiGetOrganizationUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ApiListOrganizationResponse list(limit=limit, offset=offset, search=search)

Get organization list.

### Example
```python
from __future__ import print_function
import time
import lorawan_client
from lorawan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lorawan_client.OrganizationApi()
limit = 56 # int | Max number of organizations to return in the result-set. (optional)
offset = 56 # int | Offset in the result-set (for pagination). (optional)
search = 'search_example' # str | When provided, the given string will be used to search on displayName. (optional)

try:
    # Get organization list.
    api_response = api_instance.list(limit=limit, offset=offset, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max number of organizations to return in the result-set. | [optional] 
 **offset** | **int**| Offset in the result-set (for pagination). | [optional] 
 **search** | **str**| When provided, the given string will be used to search on displayName. | [optional] 

### Return type

[**ApiListOrganizationResponse**](ApiListOrganizationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> ApiListOrganizationUsersResponse list_users(id, limit=limit, offset=offset)

Get organization's user list.

### Example
```python
from __future__ import print_function
import time
import lorawan_client
from lorawan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lorawan_client.OrganizationApi()
id = 'id_example' # str | 
limit = 56 # int | Max number of users to return in the result-set. (optional)
offset = 56 # int | Offset in the result-set (for pagination). (optional)

try:
    # Get organization's user list.
    api_response = api_instance.list_users(id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**| Max number of users to return in the result-set. | [optional] 
 **offset** | **int**| Offset in the result-set (for pagination). | [optional] 

### Return type

[**ApiListOrganizationUsersResponse**](ApiListOrganizationUsersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ApiOrganizationEmptyResponse update(id, body)

Update an existing organization.

### Example
```python
from __future__ import print_function
import time
import lorawan_client
from lorawan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lorawan_client.OrganizationApi()
id = 'id_example' # str | 
body = lorawan_client.ApiUpdateOrganizationRequest() # ApiUpdateOrganizationRequest | 

try:
    # Update an existing organization.
    api_response = api_instance.update(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**ApiUpdateOrganizationRequest**](ApiUpdateOrganizationRequest.md)|  | 

### Return type

[**ApiOrganizationEmptyResponse**](ApiOrganizationEmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> ApiOrganizationEmptyResponse update_user(id, user_id, body)

Update a user in an organization.

### Example
```python
from __future__ import print_function
import time
import lorawan_client
from lorawan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lorawan_client.OrganizationApi()
id = 'id_example' # str | 
user_id = 'user_id_example' # str | 
body = lorawan_client.ApiOrganizationUserRequest() # ApiOrganizationUserRequest | 

try:
    # Update a user in an organization.
    api_response = api_instance.update_user(id, user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **user_id** | **str**|  | 
 **body** | [**ApiOrganizationUserRequest**](ApiOrganizationUserRequest.md)|  | 

### Return type

[**ApiOrganizationEmptyResponse**](ApiOrganizationEmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

