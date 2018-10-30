# ApiAddUserRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | [**list[ApiAddUserApplication]**](ApiAddUserApplication.md) | Add the user to the following applications. | [optional] 
**is_active** | **bool** | If the user is active. | [optional] 
**is_admin** | **bool** | If the user is a system-wide admin. | [optional] 
**organizations** | [**list[ApiAddUserOrganization]**](ApiAddUserOrganization.md) | Add the user to the following organizations. | [optional] 
**password** | **str** | Passowrd of the user. | [optional] 
**session_ttl** | **int** | The session timeout, in minutes. | [optional] 
**username** | **str** | Username of the user. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


