# Flow

The core feature of Vouchsafe is the verification flow.  It is a customisable set of steps that:  - collects and validates evidence from your end user - runs background checks on that evidence and returns a result  You can make as many verification flows as you like for different business purposes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the flow, useful when requesting verifications | 
**name** | **str** | The human-readable name of the flow | 
**updated_at** | **str** | When the flow was last modified, formatted as an ISO 8601 string | 
**created_at** | **str** | When the flow was created, formatted as an ISO 8601 string | 
**tokens_per_verification** | **float** | How many tokens the flow uses per completed verification. [What are tokens?](https://help.vouchsafe.id/en/articles/11075413-what-are-tokens) | 

## Example

```python
from vouchsafe_python.models.flow import Flow

# TODO update the JSON string below
json = "{}"
# create an instance of Flow from a JSON string
flow_instance = Flow.from_json(json)
# print the JSON string representation of the object
print(Flow.to_json())

# convert the object into a dict
flow_dict = flow_instance.to_dict()
# create an instance of Flow from a dict
flow_from_dict = Flow.from_dict(flow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


