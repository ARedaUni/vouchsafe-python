# RequestVerificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | A unique URL to redirect the user to or embed in an iframe | 
**id** | **str** | A unique ID for the verification session, for you to track progress | 
**workflow_id** | **str** | The flow it belongs to | [optional] 
**expires_at** | **str** | When the user will stop getting reminders | 

## Example

```python
from vouchsafe_python.models.request_verification_response import RequestVerificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RequestVerificationResponse from a JSON string
request_verification_response_instance = RequestVerificationResponse.from_json(json)
# print the JSON string representation of the object
print(RequestVerificationResponse.to_json())

# convert the object into a dict
request_verification_response_dict = request_verification_response_instance.to_dict()
# create an instance of RequestVerificationResponse from a dict
request_verification_response_from_dict = RequestVerificationResponse.from_dict(request_verification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


