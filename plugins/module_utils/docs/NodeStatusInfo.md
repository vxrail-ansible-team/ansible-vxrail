# NodeStatusInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of node | 
**model** | **str** | mode of node | 
**serial_number** | **str** | Serial number of node | 
**system_version** | [**NodeVersionInfo**](NodeVersionInfo.md) |  | 
**appliance_id** | **str** | Appliance ID of node | 
**psnt** | **str** | PSNT of node | 
**compatible_status** | **str** | Node compatibility result after pre-check | 
**compatible_messages** | **list[str]** | Incompatible details | 
**incompatible_components** | [**list[IncompatibleComponentsInfo]**](IncompatibleComponentsInfo.md) | Incompatible components | 
**error_message** | **str** | Error message, for example node not found | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
