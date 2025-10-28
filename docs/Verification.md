# Verification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID for tracking a verification session over time | 
**status** | [**Status**](Status.md) |  | 
**created_at** | **str** | When it was originally requested or begun | 
**expires_at** | **str** | When the user will stop getting reminders | 
**email** | **str** | The originally supplied email address | 
**redirect_url** | **str** | Where to send the user upon success. If null, the verification flow default will be used. | 
**workflow_id** | **str** | The verification flow it belongs to | 
**external_id** | **str** | An identifier from your own systems, to avoid needing to store Vouchsafe&#39;s own ID. Provided at request time. | 

## Example

```python
from vouchsafe_python.models.verification import Verification

# TODO update the JSON string below
json = "{}"
# create an instance of Verification from a JSON string
verification_instance = Verification.from_json(json)
# print the JSON string representation of the object
print(Verification.to_json())

# convert the object into a dict
verification_dict = verification_instance.to_dict()
# create an instance of Verification from a dict
verification_from_dict = Verification.from_dict(verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


