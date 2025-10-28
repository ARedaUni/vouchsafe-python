# RequestVerificationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The user&#39;s email address | 
**first_name** | **str** | The user&#39;s first name, if you have it | [optional] 
**last_name** | **str** | The user&#39;s last name, if you have it | [optional] 
**street_address** | **str** | The user&#39;s street address, if you have it | [optional] 
**postcode** | **str** | The user&#39;s postcode, if you have it | [optional] 
**date_of_birth** | **str** | The user&#39;s date of birth, if you have it | [optional] 
**workflow_id** | **str** | Which verification flow to use.  Get the flow ID from the URL of the builder page.  For example: &#x60;/admin/teams/abc123/builder/[workflow_id]&#x60;  If not provided, the last published flow is used instead. | [optional] 
**external_id** | **str** | An identifier from your own systems, to avoid needing to store Vouchsafe&#39;s own ID | [optional] 
**redirect_url** | **str** | A generic or unique URL to send the user back to upon success.  If not provided, the verification flow default will be used. | [optional] 
**expires_at** | **str** | When will the verification session expire and the user cease getting reminders?  If not provided, the verification flow default will be used. | [optional] 

## Example

```python
from vouchsafe_python.models.request_verification_input import RequestVerificationInput

# TODO update the JSON string below
json = "{}"
# create an instance of RequestVerificationInput from a JSON string
request_verification_input_instance = RequestVerificationInput.from_json(json)
# print the JSON string representation of the object
print(RequestVerificationInput.to_json())

# convert the object into a dict
request_verification_input_dict = request_verification_input_instance.to_dict()
# create an instance of RequestVerificationInput from a dict
request_verification_input_from_dict = RequestVerificationInput.from_dict(request_verification_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


