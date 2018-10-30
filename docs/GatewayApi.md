# swagger_client.GatewayApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](GatewayApi.md#create) | **POST** /api/gateways | Create creates the given gateway.
[**create_channel_configuration**](GatewayApi.md#create_channel_configuration) | **POST** /api/gateways/channelconfigurations | CreateChannelConfiguration creates the given channel-configuration.
[**create_extra_channel**](GatewayApi.md#create_extra_channel) | **POST** /api/gateways/extrachannels | CreateExtraChannel creates the given extra channel.
[**delete**](GatewayApi.md#delete) | **DELETE** /api/gateways/{mac} | Delete deletes the gateway matching the given mac address.
[**delete_channel_configuration**](GatewayApi.md#delete_channel_configuration) | **DELETE** /api/gateways/channelconfigurations/{id} | DeleteChannelConfiguration deletes the channel-configuration matching the given ID.
[**delete_extra_channel**](GatewayApi.md#delete_extra_channel) | **DELETE** /api/gateways/extrachannels/{id} | DeleteExtraChannel deletes the extra channel matching the given id.
[**generate_token**](GatewayApi.md#generate_token) | **POST** /api/gateways/{mac}/token | GenerateToken issues a JWT token which can be used by the gateway for authentication.
[**get**](GatewayApi.md#get) | **GET** /api/gateways/{mac} | Get returns the gateway for the requested mac address.
[**get_channel_configuration**](GatewayApi.md#get_channel_configuration) | **GET** /api/gateways/channelconfigurations/{id} | GetChannelConfiguration returns the channel-configuration for the given ID.
[**get_extra_channels_for_channel_configuration_id**](GatewayApi.md#get_extra_channels_for_channel_configuration_id) | **GET** /api/gateways/channelconfigurations/{id}/extrachannels | GetExtraChannelsForChannelConfigurationID returns the extra channels for the given channel-configuration id.
[**get_last_ping**](GatewayApi.md#get_last_ping) | **GET** /api/gateways/{mac}/pings/last | GetLastPing returns the last emitted ping and gateways receiving this ping.
[**get_stats**](GatewayApi.md#get_stats) | **GET** /api/gateways/{mac}/stats | GetStats lists the gateway stats given the query parameters.
[**list**](GatewayApi.md#list) | **GET** /api/gateways | List lists the gateways.
[**list_channel_configurations**](GatewayApi.md#list_channel_configurations) | **GET** /api/gateways/channelconfigurations | ListChannelConfigurations returns all channel-configurations.
[**update**](GatewayApi.md#update) | **PUT** /api/gateways/{mac} | Update updates the gateway matching the given mac address.
[**update_channel_configuration**](GatewayApi.md#update_channel_configuration) | **PUT** /api/gateways/channelconfigurations/{id} | UpdateChannelConfiguration updates the given channel-configuration.
[**update_extra_channel**](GatewayApi.md#update_extra_channel) | **PUT** /api/gateways/extrachannels/{id} | UpdateExtraChannel updates the given extra channel.


# **create**
> ApiCreateGatewayResponse create(body)

Create creates the given gateway.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GatewayApi()
body = swagger_client.ApiCreateGatewayRequest() # ApiCreateGatewayRequest | 

try:
    # Create creates the given gateway.
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiCreateGatewayRequest**](ApiCreateGatewayRequest.md)|  | 

### Return type

[**ApiCreateGatewayResponse**](ApiCreateGatewayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_channel_configuration**
> ApiCreateChannelConfigurationResponse create_channel_configuration(body)

CreateChannelConfiguration creates the given channel-configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GatewayApi()
body = swagger_client.ApiCreateChannelConfigurationRequest() # ApiCreateChannelConfigurationRequest | 

try:
    # CreateChannelConfiguration creates the given channel-configuration.
    api_response = api_instance.create_channel_configuration(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayApi->create_channel_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiCreateChannelConfigurationRequest**](ApiCreateChannelConfigurationRequest.md)|  | 

### Return type

[**ApiCreateChannelConfigurationResponse**](ApiCreateChannelConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_extra_channel**
> ApiCreateExtraChannelResponse create_extra_channel(body)

CreateExtraChannel creates the given extra channel.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GatewayApi()
body = swagger_client.ApiCreateExtraChannelRequest() # ApiCreateExtraChannelRequest | 

try:
    # CreateExtraChannel creates the given extra channel.
    api_response = api_instance.create_extra_channel(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayApi->create_extra_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiCreateExtraChannelRequest**](ApiCreateExtraChannelRequest.md)|  | 

### Return type

[**ApiCreateExtraChannelResponse**](ApiCreateExtraChannelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> ApiDeleteGatewayResponse delete(mac)

Delete deletes the gateway matching the given mac address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GatewayApi()
mac = 'mac_example' # str | 

try:
    # Delete deletes the gateway matching the given mac address.
    api_response = api_instance.delete(mac)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mac** | **str**|  | 

### Return type

[**ApiDeleteGatewayResponse**](ApiDeleteGatewayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_channel_configuration**
> ApiDeleteChannelConfigurationResponse delete_channel_configuration(id)

DeleteChannelConfiguration deletes the channel-configuration matching the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GatewayApi()
id = 'id_example' # str | 

try:
    # DeleteChannelConfiguration deletes the channel-configuration matching the given ID.
    api_response = api_instance.delete_channel_configuration(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayApi->delete_channel_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApiDeleteChannelConfigurationResponse**](ApiDeleteChannelConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_extra_channel**
> ApiDeleteExtraChannelResponse delete_extra_channel(id)

DeleteExtraChannel deletes the extra channel matching the given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GatewayApi()
id = 'id_example' # str | 

try:
    # DeleteExtraChannel deletes the extra channel matching the given id.
    api_response = api_instance.delete_extra_channel(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayApi->delete_extra_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApiDeleteExtraChannelResponse**](ApiDeleteExtraChannelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_token**
> ApiGenerateGatewayTokenResponse generate_token(mac)

GenerateToken issues a JWT token which can be used by the gateway for authentication.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GatewayApi()
mac = 'mac_example' # str | 

try:
    # GenerateToken issues a JWT token which can be used by the gateway for authentication.
    api_response = api_instance.generate_token(mac)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayApi->generate_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mac** | **str**|  | 

### Return type

[**ApiGenerateGatewayTokenResponse**](ApiGenerateGatewayTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ApiGetGatewayResponse get(mac)

Get returns the gateway for the requested mac address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GatewayApi()
mac = 'mac_example' # str | 

try:
    # Get returns the gateway for the requested mac address.
    api_response = api_instance.get(mac)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mac** | **str**|  | 

### Return type

[**ApiGetGatewayResponse**](ApiGetGatewayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_configuration**
> ApiGetChannelConfigurationResponse get_channel_configuration(id)

GetChannelConfiguration returns the channel-configuration for the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GatewayApi()
id = 'id_example' # str | 

try:
    # GetChannelConfiguration returns the channel-configuration for the given ID.
    api_response = api_instance.get_channel_configuration(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayApi->get_channel_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApiGetChannelConfigurationResponse**](ApiGetChannelConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extra_channels_for_channel_configuration_id**
> ApiGetExtraChannelsForChannelConfigurationIDResponse get_extra_channels_for_channel_configuration_id(id)

GetExtraChannelsForChannelConfigurationID returns the extra channels for the given channel-configuration id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GatewayApi()
id = 'id_example' # str | 

try:
    # GetExtraChannelsForChannelConfigurationID returns the extra channels for the given channel-configuration id.
    api_response = api_instance.get_extra_channels_for_channel_configuration_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayApi->get_extra_channels_for_channel_configuration_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApiGetExtraChannelsForChannelConfigurationIDResponse**](ApiGetExtraChannelsForChannelConfigurationIDResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_ping**
> ApiGetLastPingResponse get_last_ping(mac)

GetLastPing returns the last emitted ping and gateways receiving this ping.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GatewayApi()
mac = 'mac_example' # str | 

try:
    # GetLastPing returns the last emitted ping and gateways receiving this ping.
    api_response = api_instance.get_last_ping(mac)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayApi->get_last_ping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mac** | **str**|  | 

### Return type

[**ApiGetLastPingResponse**](ApiGetLastPingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats**
> ApiGetGatewayStatsResponse get_stats(mac, interval=interval, start_timestamp=start_timestamp, end_timestamp=end_timestamp)

GetStats lists the gateway stats given the query parameters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GatewayApi()
mac = 'mac_example' # str | 
interval = 'interval_example' # str | Aggregation interval.  One of \"second\", \"minute\", \"hour\", \"day\", \"week\", \"month\", \"quarter\", \"year\".  Case insensitive. (optional)
start_timestamp = 'start_timestamp_example' # str | Timestamp to start from. (optional)
end_timestamp = 'end_timestamp_example' # str | Timestamp until to get from. (optional)

try:
    # GetStats lists the gateway stats given the query parameters.
    api_response = api_instance.get_stats(mac, interval=interval, start_timestamp=start_timestamp, end_timestamp=end_timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayApi->get_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mac** | **str**|  | 
 **interval** | **str**| Aggregation interval.  One of \&quot;second\&quot;, \&quot;minute\&quot;, \&quot;hour\&quot;, \&quot;day\&quot;, \&quot;week\&quot;, \&quot;month\&quot;, \&quot;quarter\&quot;, \&quot;year\&quot;.  Case insensitive. | [optional] 
 **start_timestamp** | **str**| Timestamp to start from. | [optional] 
 **end_timestamp** | **str**| Timestamp until to get from. | [optional] 

### Return type

[**ApiGetGatewayStatsResponse**](ApiGetGatewayStatsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ApiListGatewayResponse list(limit=limit, offset=offset, organization_id=organization_id)

List lists the gateways.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GatewayApi()
limit = 56 # int | Max number of nodes to return in the result-set. (optional)
offset = 56 # int | Offset of the result-set (for pagination). (optional)
organization_id = 'organization_id_example' # str | ID of the organization for which to filter on, when left blank the response will return all gateways to which the user has access to. (optional)

try:
    # List lists the gateways.
    api_response = api_instance.list(limit=limit, offset=offset, organization_id=organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max number of nodes to return in the result-set. | [optional] 
 **offset** | **int**| Offset of the result-set (for pagination). | [optional] 
 **organization_id** | **str**| ID of the organization for which to filter on, when left blank the response will return all gateways to which the user has access to. | [optional] 

### Return type

[**ApiListGatewayResponse**](ApiListGatewayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_channel_configurations**
> ApiListChannelConfigurationsResponse list_channel_configurations()

ListChannelConfigurations returns all channel-configurations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GatewayApi()

try:
    # ListChannelConfigurations returns all channel-configurations.
    api_response = api_instance.list_channel_configurations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayApi->list_channel_configurations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiListChannelConfigurationsResponse**](ApiListChannelConfigurationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ApiUpdateGatewayResponse update(mac, body)

Update updates the gateway matching the given mac address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GatewayApi()
mac = 'mac_example' # str | 
body = swagger_client.ApiUpdateGatewayRequest() # ApiUpdateGatewayRequest | 

try:
    # Update updates the gateway matching the given mac address.
    api_response = api_instance.update(mac, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mac** | **str**|  | 
 **body** | [**ApiUpdateGatewayRequest**](ApiUpdateGatewayRequest.md)|  | 

### Return type

[**ApiUpdateGatewayResponse**](ApiUpdateGatewayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_channel_configuration**
> ApiUpdateChannelConfigurationResponse update_channel_configuration(id, body)

UpdateChannelConfiguration updates the given channel-configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GatewayApi()
id = 'id_example' # str | 
body = swagger_client.ApiUpdateChannelConfigurationRequest() # ApiUpdateChannelConfigurationRequest | 

try:
    # UpdateChannelConfiguration updates the given channel-configuration.
    api_response = api_instance.update_channel_configuration(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayApi->update_channel_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**ApiUpdateChannelConfigurationRequest**](ApiUpdateChannelConfigurationRequest.md)|  | 

### Return type

[**ApiUpdateChannelConfigurationResponse**](ApiUpdateChannelConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_extra_channel**
> ApiUpdateExtraChannelResponse update_extra_channel(id, body)

UpdateExtraChannel updates the given extra channel.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GatewayApi()
id = 'id_example' # str | 
body = swagger_client.ApiUpdateExtraChannelRequest() # ApiUpdateExtraChannelRequest | 

try:
    # UpdateExtraChannel updates the given extra channel.
    api_response = api_instance.update_extra_channel(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayApi->update_extra_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**ApiUpdateExtraChannelRequest**](ApiUpdateExtraChannelRequest.md)|  | 

### Return type

[**ApiUpdateExtraChannelResponse**](ApiUpdateExtraChannelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

