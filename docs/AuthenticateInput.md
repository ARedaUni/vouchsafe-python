# AuthenticateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**client_secret** | **str** |  | 

## Example

```python
from vouchsafe_python.models.authenticate_input import AuthenticateInput

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticateInput from a JSON string
authenticate_input_instance = AuthenticateInput.from_json(json)
# print the JSON string representation of the object
print(AuthenticateInput.to_json())

# convert the object into a dict
authenticate_input_dict = authenticate_input_instance.to_dict()
# create an instance of AuthenticateInput from a dict
authenticate_input_from_dict = AuthenticateInput.from_dict(authenticate_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


