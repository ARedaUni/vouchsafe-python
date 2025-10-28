# SmartLookupInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_line_of_address** | **str** | Should be taken from GET /postcode endpoint | 
**postcode** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**checks** | **List[str]** | Experimental, other checks coming soon | 

## Example

```python
from vouchsafe_python.models.smart_lookup_input import SmartLookupInput

# TODO update the JSON string below
json = "{}"
# create an instance of SmartLookupInput from a JSON string
smart_lookup_input_instance = SmartLookupInput.from_json(json)
# print the JSON string representation of the object
print(SmartLookupInput.to_json())

# convert the object into a dict
smart_lookup_input_dict = smart_lookup_input_instance.to_dict()
# create an instance of SmartLookupInput from a dict
smart_lookup_input_from_dict = SmartLookupInput.from_dict(smart_lookup_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


