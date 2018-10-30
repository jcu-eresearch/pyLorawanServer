# ApiDownlinkQueueItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmed** | **bool** | Is an ACK required from the node. | [optional] 
**data** | **str** | Base64 encoded data. | [optional] 
**dev_eui** | **str** | Hex encoded DevEUI of the node. | [optional] 
**f_port** | **int** | FPort used (must be &gt;0). | [optional] 
**id** | **str** | ID of the queue item. | [optional] 
**pending** | **bool** | Transmission is pending (waiting for an ack). | [optional] 
**reference** | **str** | Random reference (used on ack notification). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


