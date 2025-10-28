# AuthenticateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**expires_at** | **str** |  | 

## Example

```python
from vouchsafe_python.models.authenticate_response import AuthenticateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticateResponse from a JSON string
authenticate_response_instance = AuthenticateResponse.from_json(json)
# print the JSON string representation of the object
print(AuthenticateResponse.to_json())

# convert the object into a dict
authenticate_response_dict = authenticate_response_instance.to_dict()
# create an instance of AuthenticateResponse from a dict
authenticate_response_from_dict = AuthenticateResponse.from_dict(authenticate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


