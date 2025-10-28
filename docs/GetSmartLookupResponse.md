# GetSmartLookupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**team_id** | **str** |  | 
**checks** | [**List[Model36EnumsBackgroundCheck]**](Model36EnumsBackgroundCheck.md) |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**first_line_of_address** | **str** |  | 
**postcode** | **str** |  | 
**address_verification_report** | [**Report**](Report.md) | Whether the overall check and its sub-checks passed, failed or somethng else. | 
**metadata** | **object** | Extra information to aid debugging. May change without notice. | 
**created_at** | **str** |  | 

## Example

```python
from vouchsafe_python.models.get_smart_lookup_response import GetSmartLookupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSmartLookupResponse from a JSON string
get_smart_lookup_response_instance = GetSmartLookupResponse.from_json(json)
# print the JSON string representation of the object
print(GetSmartLookupResponse.to_json())

# convert the object into a dict
get_smart_lookup_response_dict = get_smart_lookup_response_instance.to_dict()
# create an instance of GetSmartLookupResponse from a dict
get_smart_lookup_response_from_dict = GetSmartLookupResponse.from_dict(get_smart_lookup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


