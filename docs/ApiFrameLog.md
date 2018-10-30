# ApiFrameLog

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | Timestamp of when the frame was logged. | [optional] 
**phy_payload_json** | **str** | LoRaWAN PHYPayload as a JSON string. | [optional] 
**rx_info_set** | [**list[ApiRXInfo]**](ApiRXInfo.md) | RX-info set (in case of an uplink). | [optional] 
**tx_info** | [**ApiTXInfo**](ApiTXInfo.md) | TX-info (in case of a downlink). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


