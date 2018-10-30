# lorawan_client.InternalApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**branding**](InternalApi.md#branding) | **GET** /api/internal/branding | Get the branding for the UI
[**login**](InternalApi.md#login) | **POST** /api/internal/login | Log in a user
[**profile**](InternalApi.md#profile) | **GET** /api/internal/profile | Get the current user&#39;s profile


# **branding**
> ApiBrandingResponse branding()

Get the branding for the UI

### Example
```python
from __future__ import print_function
import time
import lorawan_client
from lorawan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lorawan_client.InternalApi()

try:
    # Get the branding for the UI
    api_response = api_instance.branding()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->branding: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiBrandingResponse**](ApiBrandingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> ApiLoginResponse login(body)

Log in a user

### Example
```python
from __future__ import print_function
import time
import lorawan_client
from lorawan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lorawan_client.InternalApi()
body = lorawan_client.ApiLoginRequest() # ApiLoginRequest | 

try:
    # Log in a user
    api_response = api_instance.login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiLoginRequest**](ApiLoginRequest.md)|  | 

### Return type

[**ApiLoginResponse**](ApiLoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile**
> ApiProfileResponse profile()

Get the current user's profile

### Example
```python
from __future__ import print_function
import time
import lorawan_client
from lorawan_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lorawan_client.InternalApi()

try:
    # Get the current user's profile
    api_response = api_instance.profile()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->profile: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiProfileResponse**](ApiProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

