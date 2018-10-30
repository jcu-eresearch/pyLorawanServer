# ApiUpdateApplicationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adr_interval** | **int** | Interval (in frames) in which the ADR engine may adapt the data-rate of the node (0 &#x3D; disabled). | [optional] 
**description** | **str** | Description of the application. | [optional] 
**id** | **str** | ID of the application to update. | [optional] 
**installation_margin** | **float** | Installation-margin to use for ADR calculation. | [optional] 
**is_abp** | **bool** | Node is activated by ABP. | [optional] 
**is_class_c** | **bool** | Node operates in Class-C. | [optional] 
**name** | **str** | Name of the application (must be unique). | [optional] 
**organization_id** | **str** | ID of the organization to which the application belongs. | [optional] 
**relax_f_cnt** | **bool** | Relax frame-counter mode is enabled. | [optional] 
**rx1_dr_offset** | **int** | RX1 data-rate offset. | [optional] 
**rx2_dr** | **int** | Data-rate to use for RX2. | [optional] 
**rx_delay** | **int** | RX delay. | [optional] 
**rx_window** | [**ApiRXWindow**](ApiRXWindow.md) | RX window to use. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


