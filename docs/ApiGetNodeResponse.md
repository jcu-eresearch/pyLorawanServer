# ApiGetNodeResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adr_interval** | **int** | Interval (in frames) in which the ADR engine may adapt the data-rate of the node (0 &#x3D; disabled). | [optional] 
**app_eui** | **str** | Hex encoded AppEUI. | [optional] 
**app_key** | **str** | Hex encoded AppKey. | [optional] 
**application_id** | **str** | ID of the application owning the node. | [optional] 
**description** | **str** | Description of the node. | [optional] 
**dev_eui** | **str** | Hex encoded DevEUI. | [optional] 
**installation_margin** | **float** | Installation-margin to use for ADR calculation. | [optional] 
**is_abp** | **bool** | Node is activated by ABP. | [optional] 
**is_class_c** | **bool** | Node operates in Class-C. | [optional] 
**name** | **str** | Name of the node. | [optional] 
**relax_f_cnt** | **bool** | Relax frame-counter mode is enabled. | [optional] 
**rx1_dr_offset** | **int** | RX1 data-rate offset. | [optional] 
**rx2_dr** | **int** | Data-rate to use for RX2. | [optional] 
**rx_delay** | **int** | RX delay. | [optional] 
**rx_window** | [**ApiRXWindow**](ApiRXWindow.md) | RX window to use. | [optional] 
**use_application_settings** | **bool** | When set to true, the application settings will be used to populate the node network settings. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


