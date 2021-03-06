# LoRAWAN Server - REST Client
 For more information about the usage of the LoRa App Server (REST) API, see [https://docs.loraserver.io/lora-app-server/api/](https://docs.loraserver.io/lora-app-server/api/). 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
- Spec file: https://lorawan-server.sensor-cloud.io:8443/swagger/api.swagger.json
- Generate Command: java -jar modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate -i api.swagger.json -l python -o ../pyLorawanServer

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import lorawan_server 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import lorawan_server
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import lorawan_server
from lorawan_server.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lorawan_server.ApplicationApi(lorawan_server.ApiClient(configuration))
id = 'id_example' # str | 
body = lorawan_server.ApiAddApplicationUserRequest() # ApiAddApplicationUserRequest | 

try:
    # AddUser adds a user to an application.
    api_response = api_instance.add_user(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->add_user: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApplicationApi* | [**add_user**](docs/ApplicationApi.md#add_user) | **POST** /api/applications/{id}/users | AddUser adds a user to an application.
*ApplicationApi* | [**create**](docs/ApplicationApi.md#create) | **POST** /api/applications | Create creates the given application.
*ApplicationApi* | [**create_http_integration**](docs/ApplicationApi.md#create_http_integration) | **POST** /api/applications/{id}/integrations/http | CreateHTTPIntegration creates an HTTP application-integration.
*ApplicationApi* | [**delete**](docs/ApplicationApi.md#delete) | **DELETE** /api/applications/{id} | Delete deletes the given application.
*ApplicationApi* | [**delete_http_integration**](docs/ApplicationApi.md#delete_http_integration) | **DELETE** /api/applications/{id}/integrations/http | DeleteIntegration deletes the application-integration of the given type.
*ApplicationApi* | [**delete_user**](docs/ApplicationApi.md#delete_user) | **DELETE** /api/applications/{id}/users/{userID} | DeleteUser deletes the user&#39;s access to the associated application.
*ApplicationApi* | [**get**](docs/ApplicationApi.md#get) | **GET** /api/applications/{id} | Get returns the requested application.
*ApplicationApi* | [**get_http_integration**](docs/ApplicationApi.md#get_http_integration) | **GET** /api/applications/{id}/integrations/http | GetHTTPIntegration returns the HTTP application-itegration.
*ApplicationApi* | [**get_user**](docs/ApplicationApi.md#get_user) | **GET** /api/applications/{id}/users/{userID} | GetUser gets the user that is associated with the application.
*ApplicationApi* | [**list**](docs/ApplicationApi.md#list) | **GET** /api/applications | List lists the available applications.
*ApplicationApi* | [**list_integrations**](docs/ApplicationApi.md#list_integrations) | **GET** /api/applications/{id}/integrations | ListIntegrations lists all configured integrations.
*ApplicationApi* | [**list_users**](docs/ApplicationApi.md#list_users) | **GET** /api/applications/{id}/users | ListUsers lists the users for an application.
*ApplicationApi* | [**update**](docs/ApplicationApi.md#update) | **PUT** /api/applications/{id} | Update updates the given application.
*ApplicationApi* | [**update_http_integration**](docs/ApplicationApi.md#update_http_integration) | **PUT** /api/applications/{id}/integrations/http | UpdateHTTPIntegration updates the HTTP application-integration.
*ApplicationApi* | [**update_user**](docs/ApplicationApi.md#update_user) | **PUT** /api/applications/{id}/users/{userID} | UpdateUser sets the user&#39;s access to the associated application.
*DownlinkQueueApi* | [**delete**](docs/DownlinkQueueApi.md#delete) | **DELETE** /api/nodes/{devEUI}/queue/{id} | Delete deletes an item from the queue.
*DownlinkQueueApi* | [**enqueue**](docs/DownlinkQueueApi.md#enqueue) | **POST** /api/nodes/{devEUI}/queue | Enqueue adds the given item to the queue. When the node operates in Class-C mode, the data will be pushed directly to the network-server.
*DownlinkQueueApi* | [**list**](docs/DownlinkQueueApi.md#list) | **GET** /api/nodes/{devEUI}/queue | List lists the items in the queue for the given node.
*GatewayApi* | [**create**](docs/GatewayApi.md#create) | **POST** /api/gateways | Create creates the given gateway.
*GatewayApi* | [**create_channel_configuration**](docs/GatewayApi.md#create_channel_configuration) | **POST** /api/gateways/channelconfigurations | CreateChannelConfiguration creates the given channel-configuration.
*GatewayApi* | [**create_extra_channel**](docs/GatewayApi.md#create_extra_channel) | **POST** /api/gateways/extrachannels | CreateExtraChannel creates the given extra channel.
*GatewayApi* | [**delete**](docs/GatewayApi.md#delete) | **DELETE** /api/gateways/{mac} | Delete deletes the gateway matching the given mac address.
*GatewayApi* | [**delete_channel_configuration**](docs/GatewayApi.md#delete_channel_configuration) | **DELETE** /api/gateways/channelconfigurations/{id} | DeleteChannelConfiguration deletes the channel-configuration matching the given ID.
*GatewayApi* | [**delete_extra_channel**](docs/GatewayApi.md#delete_extra_channel) | **DELETE** /api/gateways/extrachannels/{id} | DeleteExtraChannel deletes the extra channel matching the given id.
*GatewayApi* | [**generate_token**](docs/GatewayApi.md#generate_token) | **POST** /api/gateways/{mac}/token | GenerateToken issues a JWT token which can be used by the gateway for authentication.
*GatewayApi* | [**get**](docs/GatewayApi.md#get) | **GET** /api/gateways/{mac} | Get returns the gateway for the requested mac address.
*GatewayApi* | [**get_channel_configuration**](docs/GatewayApi.md#get_channel_configuration) | **GET** /api/gateways/channelconfigurations/{id} | GetChannelConfiguration returns the channel-configuration for the given ID.
*GatewayApi* | [**get_extra_channels_for_channel_configuration_id**](docs/GatewayApi.md#get_extra_channels_for_channel_configuration_id) | **GET** /api/gateways/channelconfigurations/{id}/extrachannels | GetExtraChannelsForChannelConfigurationID returns the extra channels for the given channel-configuration id.
*GatewayApi* | [**get_last_ping**](docs/GatewayApi.md#get_last_ping) | **GET** /api/gateways/{mac}/pings/last | GetLastPing returns the last emitted ping and gateways receiving this ping.
*GatewayApi* | [**get_stats**](docs/GatewayApi.md#get_stats) | **GET** /api/gateways/{mac}/stats | GetStats lists the gateway stats given the query parameters.
*GatewayApi* | [**list**](docs/GatewayApi.md#list) | **GET** /api/gateways | List lists the gateways.
*GatewayApi* | [**list_channel_configurations**](docs/GatewayApi.md#list_channel_configurations) | **GET** /api/gateways/channelconfigurations | ListChannelConfigurations returns all channel-configurations.
*GatewayApi* | [**update**](docs/GatewayApi.md#update) | **PUT** /api/gateways/{mac} | Update updates the gateway matching the given mac address.
*GatewayApi* | [**update_channel_configuration**](docs/GatewayApi.md#update_channel_configuration) | **PUT** /api/gateways/channelconfigurations/{id} | UpdateChannelConfiguration updates the given channel-configuration.
*GatewayApi* | [**update_extra_channel**](docs/GatewayApi.md#update_extra_channel) | **PUT** /api/gateways/extrachannels/{id} | UpdateExtraChannel updates the given extra channel.
*InternalApi* | [**branding**](docs/InternalApi.md#branding) | **GET** /api/internal/branding | Get the branding for the UI
*InternalApi* | [**login**](docs/InternalApi.md#login) | **POST** /api/internal/login | Log in a user
*InternalApi* | [**profile**](docs/InternalApi.md#profile) | **GET** /api/internal/profile | Get the current user&#39;s profile
*NodeApi* | [**activate**](docs/NodeApi.md#activate) | **POST** /api/nodes/{devEUI}/activation | Activate (re)activates the node (only when ABP is set to true).
*NodeApi* | [**create**](docs/NodeApi.md#create) | **POST** /api/nodes | Create creates the given node.
*NodeApi* | [**delete**](docs/NodeApi.md#delete) | **DELETE** /api/nodes/{devEUI} | Delete deletes the node matching the given DevEUI.
*NodeApi* | [**get**](docs/NodeApi.md#get) | **GET** /api/nodes/{devEUI} | Get returns the node for the requested DevEUI.
*NodeApi* | [**get_activation**](docs/NodeApi.md#get_activation) | **GET** /api/nodes/{devEUI}/activation | GetActivation returns the current activation details of the node (OTAA and ABP).
*NodeApi* | [**get_frame_logs**](docs/NodeApi.md#get_frame_logs) | **GET** /api/nodes/{devEUI}/frames | GetFrameLogs returns the uplink / downlink frame log for the given DevEUI.
*NodeApi* | [**get_random_dev_addr**](docs/NodeApi.md#get_random_dev_addr) | **POST** /api/nodes/getRandomDevAddr | GetRandomDevAddr returns a random DevAddr taking the NwkID prefix into account.
*NodeApi* | [**list_by_application_id**](docs/NodeApi.md#list_by_application_id) | **GET** /api/applications/{applicationID}/nodes | ListByApplicationID lists the nodes by the given application ID, sorted by the name of the node.
*NodeApi* | [**update**](docs/NodeApi.md#update) | **PUT** /api/nodes/{devEUI} | Update updates the node matching the given DevEUI.
*OrganizationApi* | [**add_user**](docs/OrganizationApi.md#add_user) | **POST** /api/organizations/{id}/users | Add a new user to an organization.
*OrganizationApi* | [**create**](docs/OrganizationApi.md#create) | **POST** /api/organizations | Create a new organization.
*OrganizationApi* | [**delete**](docs/OrganizationApi.md#delete) | **DELETE** /api/organizations/{id} | Delete an organization.
*OrganizationApi* | [**delete_user**](docs/OrganizationApi.md#delete_user) | **DELETE** /api/organizations/{id}/users/{userID} | Delete a user from an organization.
*OrganizationApi* | [**get**](docs/OrganizationApi.md#get) | **GET** /api/organizations/{id} | Get data for a particular organization.
*OrganizationApi* | [**get_user**](docs/OrganizationApi.md#get_user) | **GET** /api/organizations/{id}/users/{userID} | Get data for a particular organization user.
*OrganizationApi* | [**list**](docs/OrganizationApi.md#list) | **GET** /api/organizations | Get organization list.
*OrganizationApi* | [**list_users**](docs/OrganizationApi.md#list_users) | **GET** /api/organizations/{id}/users | Get organization&#39;s user list.
*OrganizationApi* | [**update**](docs/OrganizationApi.md#update) | **PUT** /api/organizations/{id} | Update an existing organization.
*OrganizationApi* | [**update_user**](docs/OrganizationApi.md#update_user) | **PUT** /api/organizations/{id}/users/{userID} | Update a user in an organization.
*UserApi* | [**create**](docs/UserApi.md#create) | **POST** /api/users | Create a new user.
*UserApi* | [**delete**](docs/UserApi.md#delete) | **DELETE** /api/users/{id} | Delete a user.
*UserApi* | [**get**](docs/UserApi.md#get) | **GET** /api/users/{id} | Get data for a particular user.
*UserApi* | [**list**](docs/UserApi.md#list) | **GET** /api/users | Get user list.
*UserApi* | [**update**](docs/UserApi.md#update) | **PUT** /api/users/{id} | Update an existing user.
*UserApi* | [**update_password**](docs/UserApi.md#update_password) | **PUT** /api/users/{id}/password | UpdatePassword updates a password.


## Documentation For Models

 - [ApiActivateNodeRequest](docs/ApiActivateNodeRequest.md)
 - [ApiActivateNodeResponse](docs/ApiActivateNodeResponse.md)
 - [ApiAddApplicationUserRequest](docs/ApiAddApplicationUserRequest.md)
 - [ApiAddUserApplication](docs/ApiAddUserApplication.md)
 - [ApiAddUserOrganization](docs/ApiAddUserOrganization.md)
 - [ApiAddUserRequest](docs/ApiAddUserRequest.md)
 - [ApiAddUserResponse](docs/ApiAddUserResponse.md)
 - [ApiApplicationLink](docs/ApiApplicationLink.md)
 - [ApiBrandingResponse](docs/ApiBrandingResponse.md)
 - [ApiCreateApplicationRequest](docs/ApiCreateApplicationRequest.md)
 - [ApiCreateApplicationResponse](docs/ApiCreateApplicationResponse.md)
 - [ApiCreateChannelConfigurationRequest](docs/ApiCreateChannelConfigurationRequest.md)
 - [ApiCreateChannelConfigurationResponse](docs/ApiCreateChannelConfigurationResponse.md)
 - [ApiCreateExtraChannelRequest](docs/ApiCreateExtraChannelRequest.md)
 - [ApiCreateExtraChannelResponse](docs/ApiCreateExtraChannelResponse.md)
 - [ApiCreateGatewayRequest](docs/ApiCreateGatewayRequest.md)
 - [ApiCreateGatewayResponse](docs/ApiCreateGatewayResponse.md)
 - [ApiCreateNodeRequest](docs/ApiCreateNodeRequest.md)
 - [ApiCreateNodeResponse](docs/ApiCreateNodeResponse.md)
 - [ApiCreateOrganizationRequest](docs/ApiCreateOrganizationRequest.md)
 - [ApiCreateOrganizationResponse](docs/ApiCreateOrganizationResponse.md)
 - [ApiDataRate](docs/ApiDataRate.md)
 - [ApiDeleteApplicationResponse](docs/ApiDeleteApplicationResponse.md)
 - [ApiDeleteChannelConfigurationResponse](docs/ApiDeleteChannelConfigurationResponse.md)
 - [ApiDeleteDownlinkQueueItemResponse](docs/ApiDeleteDownlinkQueueItemResponse.md)
 - [ApiDeleteExtraChannelResponse](docs/ApiDeleteExtraChannelResponse.md)
 - [ApiDeleteGatewayResponse](docs/ApiDeleteGatewayResponse.md)
 - [ApiDeleteNodeResponse](docs/ApiDeleteNodeResponse.md)
 - [ApiDownlinkQueueItem](docs/ApiDownlinkQueueItem.md)
 - [ApiEmptyApplicationUserResponse](docs/ApiEmptyApplicationUserResponse.md)
 - [ApiEmptyResponse](docs/ApiEmptyResponse.md)
 - [ApiEnqueueDownlinkQueueItemRequest](docs/ApiEnqueueDownlinkQueueItemRequest.md)
 - [ApiEnqueueDownlinkQueueItemResponse](docs/ApiEnqueueDownlinkQueueItemResponse.md)
 - [ApiFrameLog](docs/ApiFrameLog.md)
 - [ApiGatewayStats](docs/ApiGatewayStats.md)
 - [ApiGenerateGatewayTokenResponse](docs/ApiGenerateGatewayTokenResponse.md)
 - [ApiGetApplicationResponse](docs/ApiGetApplicationResponse.md)
 - [ApiGetApplicationUserResponse](docs/ApiGetApplicationUserResponse.md)
 - [ApiGetChannelConfigurationResponse](docs/ApiGetChannelConfigurationResponse.md)
 - [ApiGetExtraChannelResponse](docs/ApiGetExtraChannelResponse.md)
 - [ApiGetExtraChannelsForChannelConfigurationIDResponse](docs/ApiGetExtraChannelsForChannelConfigurationIDResponse.md)
 - [ApiGetFrameLogsResponse](docs/ApiGetFrameLogsResponse.md)
 - [ApiGetGatewayResponse](docs/ApiGetGatewayResponse.md)
 - [ApiGetGatewayStatsResponse](docs/ApiGetGatewayStatsResponse.md)
 - [ApiGetLastPingResponse](docs/ApiGetLastPingResponse.md)
 - [ApiGetNodeActivationResponse](docs/ApiGetNodeActivationResponse.md)
 - [ApiGetNodeResponse](docs/ApiGetNodeResponse.md)
 - [ApiGetOrganizationResponse](docs/ApiGetOrganizationResponse.md)
 - [ApiGetOrganizationUserResponse](docs/ApiGetOrganizationUserResponse.md)
 - [ApiGetRandomDevAddrResponse](docs/ApiGetRandomDevAddrResponse.md)
 - [ApiGetUserResponse](docs/ApiGetUserResponse.md)
 - [ApiHTTPIntegration](docs/ApiHTTPIntegration.md)
 - [ApiHTTPIntegrationHeader](docs/ApiHTTPIntegrationHeader.md)
 - [ApiIntegrationKind](docs/ApiIntegrationKind.md)
 - [ApiListApplicationResponse](docs/ApiListApplicationResponse.md)
 - [ApiListApplicationUsersResponse](docs/ApiListApplicationUsersResponse.md)
 - [ApiListChannelConfigurationsResponse](docs/ApiListChannelConfigurationsResponse.md)
 - [ApiListDownlinkQueueItemsResponse](docs/ApiListDownlinkQueueItemsResponse.md)
 - [ApiListGatewayItem](docs/ApiListGatewayItem.md)
 - [ApiListGatewayResponse](docs/ApiListGatewayResponse.md)
 - [ApiListIntegrationResponse](docs/ApiListIntegrationResponse.md)
 - [ApiListNodeResponse](docs/ApiListNodeResponse.md)
 - [ApiListOrganizationResponse](docs/ApiListOrganizationResponse.md)
 - [ApiListOrganizationUsersResponse](docs/ApiListOrganizationUsersResponse.md)
 - [ApiListUserResponse](docs/ApiListUserResponse.md)
 - [ApiLoginRequest](docs/ApiLoginRequest.md)
 - [ApiLoginResponse](docs/ApiLoginResponse.md)
 - [ApiModulation](docs/ApiModulation.md)
 - [ApiOrganizationEmptyResponse](docs/ApiOrganizationEmptyResponse.md)
 - [ApiOrganizationLink](docs/ApiOrganizationLink.md)
 - [ApiOrganizationUserRequest](docs/ApiOrganizationUserRequest.md)
 - [ApiPingRX](docs/ApiPingRX.md)
 - [ApiProfileResponse](docs/ApiProfileResponse.md)
 - [ApiProfileSettings](docs/ApiProfileSettings.md)
 - [ApiRXInfo](docs/ApiRXInfo.md)
 - [ApiRXWindow](docs/ApiRXWindow.md)
 - [ApiTXInfo](docs/ApiTXInfo.md)
 - [ApiUpdateApplicationRequest](docs/ApiUpdateApplicationRequest.md)
 - [ApiUpdateApplicationResponse](docs/ApiUpdateApplicationResponse.md)
 - [ApiUpdateApplicationUserRequest](docs/ApiUpdateApplicationUserRequest.md)
 - [ApiUpdateChannelConfigurationRequest](docs/ApiUpdateChannelConfigurationRequest.md)
 - [ApiUpdateChannelConfigurationResponse](docs/ApiUpdateChannelConfigurationResponse.md)
 - [ApiUpdateExtraChannelRequest](docs/ApiUpdateExtraChannelRequest.md)
 - [ApiUpdateExtraChannelResponse](docs/ApiUpdateExtraChannelResponse.md)
 - [ApiUpdateGatewayRequest](docs/ApiUpdateGatewayRequest.md)
 - [ApiUpdateGatewayResponse](docs/ApiUpdateGatewayResponse.md)
 - [ApiUpdateNodeRequest](docs/ApiUpdateNodeRequest.md)
 - [ApiUpdateNodeResponse](docs/ApiUpdateNodeResponse.md)
 - [ApiUpdateOrganizationRequest](docs/ApiUpdateOrganizationRequest.md)
 - [ApiUpdateUserPasswordRequest](docs/ApiUpdateUserPasswordRequest.md)
 - [ApiUpdateUserRequest](docs/ApiUpdateUserRequest.md)
 - [ApiUserEmptyResponse](docs/ApiUserEmptyResponse.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



