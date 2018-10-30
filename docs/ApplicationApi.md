# swagger_client.ApplicationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user**](ApplicationApi.md#add_user) | **POST** /api/applications/{id}/users | AddUser adds a user to an application.
[**create**](ApplicationApi.md#create) | **POST** /api/applications | Create creates the given application.
[**create_http_integration**](ApplicationApi.md#create_http_integration) | **POST** /api/applications/{id}/integrations/http | CreateHTTPIntegration creates an HTTP application-integration.
[**delete**](ApplicationApi.md#delete) | **DELETE** /api/applications/{id} | Delete deletes the given application.
[**delete_http_integration**](ApplicationApi.md#delete_http_integration) | **DELETE** /api/applications/{id}/integrations/http | DeleteIntegration deletes the application-integration of the given type.
[**delete_user**](ApplicationApi.md#delete_user) | **DELETE** /api/applications/{id}/users/{userID} | DeleteUser deletes the user&#39;s access to the associated application.
[**get**](ApplicationApi.md#get) | **GET** /api/applications/{id} | Get returns the requested application.
[**get_http_integration**](ApplicationApi.md#get_http_integration) | **GET** /api/applications/{id}/integrations/http | GetHTTPIntegration returns the HTTP application-itegration.
[**get_user**](ApplicationApi.md#get_user) | **GET** /api/applications/{id}/users/{userID} | GetUser gets the user that is associated with the application.
[**list**](ApplicationApi.md#list) | **GET** /api/applications | List lists the available applications.
[**list_integrations**](ApplicationApi.md#list_integrations) | **GET** /api/applications/{id}/integrations | ListIntegrations lists all configured integrations.
[**list_users**](ApplicationApi.md#list_users) | **GET** /api/applications/{id}/users | ListUsers lists the users for an application.
[**update**](ApplicationApi.md#update) | **PUT** /api/applications/{id} | Update updates the given application.
[**update_http_integration**](ApplicationApi.md#update_http_integration) | **PUT** /api/applications/{id}/integrations/http | UpdateHTTPIntegration updates the HTTP application-integration.
[**update_user**](ApplicationApi.md#update_user) | **PUT** /api/applications/{id}/users/{userID} | UpdateUser sets the user&#39;s access to the associated application.


# **add_user**
> ApiEmptyApplicationUserResponse add_user(id, body)

AddUser adds a user to an application.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
id = 'id_example' # str | 
body = swagger_client.ApiAddApplicationUserRequest() # ApiAddApplicationUserRequest | 

try:
    # AddUser adds a user to an application.
    api_response = api_instance.add_user(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->add_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**ApiAddApplicationUserRequest**](ApiAddApplicationUserRequest.md)|  | 

### Return type

[**ApiEmptyApplicationUserResponse**](ApiEmptyApplicationUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> ApiCreateApplicationResponse create(body)

Create creates the given application.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
body = swagger_client.ApiCreateApplicationRequest() # ApiCreateApplicationRequest | 

try:
    # Create creates the given application.
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiCreateApplicationRequest**](ApiCreateApplicationRequest.md)|  | 

### Return type

[**ApiCreateApplicationResponse**](ApiCreateApplicationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_http_integration**
> ApiEmptyResponse create_http_integration(id, body)

CreateHTTPIntegration creates an HTTP application-integration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
id = 'id_example' # str | 
body = swagger_client.ApiHTTPIntegration() # ApiHTTPIntegration | 

try:
    # CreateHTTPIntegration creates an HTTP application-integration.
    api_response = api_instance.create_http_integration(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->create_http_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**ApiHTTPIntegration**](ApiHTTPIntegration.md)|  | 

### Return type

[**ApiEmptyResponse**](ApiEmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> ApiDeleteApplicationResponse delete(id)

Delete deletes the given application.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
id = 'id_example' # str | 

try:
    # Delete deletes the given application.
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApiDeleteApplicationResponse**](ApiDeleteApplicationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_http_integration**
> ApiEmptyResponse delete_http_integration(id)

DeleteIntegration deletes the application-integration of the given type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
id = 'id_example' # str | 

try:
    # DeleteIntegration deletes the application-integration of the given type.
    api_response = api_instance.delete_http_integration(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->delete_http_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApiEmptyResponse**](ApiEmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> ApiEmptyApplicationUserResponse delete_user(id, user_id)

DeleteUser deletes the user's access to the associated application.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
id = 'id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # DeleteUser deletes the user's access to the associated application.
    api_response = api_instance.delete_user(id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**ApiEmptyApplicationUserResponse**](ApiEmptyApplicationUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ApiGetApplicationResponse get(id)

Get returns the requested application.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
id = 'id_example' # str | 

try:
    # Get returns the requested application.
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApiGetApplicationResponse**](ApiGetApplicationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_http_integration**
> ApiHTTPIntegration get_http_integration(id)

GetHTTPIntegration returns the HTTP application-itegration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
id = 'id_example' # str | 

try:
    # GetHTTPIntegration returns the HTTP application-itegration.
    api_response = api_instance.get_http_integration(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_http_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApiHTTPIntegration**](ApiHTTPIntegration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> ApiGetApplicationUserResponse get_user(id, user_id)

GetUser gets the user that is associated with the application.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
id = 'id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # GetUser gets the user that is associated with the application.
    api_response = api_instance.get_user(id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**ApiGetApplicationUserResponse**](ApiGetApplicationUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ApiListApplicationResponse list(limit=limit, offset=offset, organization_id=organization_id)

List lists the available applications.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
limit = 'limit_example' # str | Max number of applications to return in the result-test. (optional)
offset = 'offset_example' # str | Offset in the result-set (for pagination). (optional)
organization_id = 'organization_id_example' # str | ID of the organization to filter on. (optional)

try:
    # List lists the available applications.
    api_response = api_instance.list(limit=limit, offset=offset, organization_id=organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| Max number of applications to return in the result-test. | [optional] 
 **offset** | **str**| Offset in the result-set (for pagination). | [optional] 
 **organization_id** | **str**| ID of the organization to filter on. | [optional] 

### Return type

[**ApiListApplicationResponse**](ApiListApplicationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_integrations**
> ApiListIntegrationResponse list_integrations(id)

ListIntegrations lists all configured integrations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
id = 'id_example' # str | 

try:
    # ListIntegrations lists all configured integrations.
    api_response = api_instance.list_integrations(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->list_integrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApiListIntegrationResponse**](ApiListIntegrationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> ApiListApplicationUsersResponse list_users(id, limit=limit, offset=offset)

ListUsers lists the users for an application.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
id = 'id_example' # str | 
limit = 'limit_example' # str | Max number of applications to return in the result-test. (optional)
offset = 'offset_example' # str | Offset in the result-set (for pagination). (optional)

try:
    # ListUsers lists the users for an application.
    api_response = api_instance.list_users(id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **str**| Max number of applications to return in the result-test. | [optional] 
 **offset** | **str**| Offset in the result-set (for pagination). | [optional] 

### Return type

[**ApiListApplicationUsersResponse**](ApiListApplicationUsersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ApiUpdateApplicationResponse update(id, body)

Update updates the given application.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
id = 'id_example' # str | 
body = swagger_client.ApiUpdateApplicationRequest() # ApiUpdateApplicationRequest | 

try:
    # Update updates the given application.
    api_response = api_instance.update(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**ApiUpdateApplicationRequest**](ApiUpdateApplicationRequest.md)|  | 

### Return type

[**ApiUpdateApplicationResponse**](ApiUpdateApplicationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_http_integration**
> ApiEmptyResponse update_http_integration(id, body)

UpdateHTTPIntegration updates the HTTP application-integration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
id = 'id_example' # str | 
body = swagger_client.ApiHTTPIntegration() # ApiHTTPIntegration | 

try:
    # UpdateHTTPIntegration updates the HTTP application-integration.
    api_response = api_instance.update_http_integration(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->update_http_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**ApiHTTPIntegration**](ApiHTTPIntegration.md)|  | 

### Return type

[**ApiEmptyResponse**](ApiEmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> ApiEmptyApplicationUserResponse update_user(id, user_id, body)

UpdateUser sets the user's access to the associated application.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
id = 'id_example' # str | 
user_id = 'user_id_example' # str | 
body = swagger_client.ApiUpdateApplicationUserRequest() # ApiUpdateApplicationUserRequest | 

try:
    # UpdateUser sets the user's access to the associated application.
    api_response = api_instance.update_user(id, user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **user_id** | **str**|  | 
 **body** | [**ApiUpdateApplicationUserRequest**](ApiUpdateApplicationUserRequest.md)|  | 

### Return type

[**ApiEmptyApplicationUserResponse**](ApiEmptyApplicationUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

