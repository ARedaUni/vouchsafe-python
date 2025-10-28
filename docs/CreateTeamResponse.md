# CreateTeamResponse

Response from creating a new team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the created team | 
**name** | **str** | The name of the team. | 
**public_name** | **str** | The public name of the team, shown in end-user facing screens and communications. If set, overrides the name. | [optional] 
**created_at** | **str** | ISO 8601 timestamp of team creation | 
**credentials** | [**CreateTeamResponseCredentials**](CreateTeamResponseCredentials.md) |  | 

## Example

```python
from vouchsafe_python.models.create_team_response import CreateTeamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTeamResponse from a JSON string
create_team_response_instance = CreateTeamResponse.from_json(json)
# print the JSON string representation of the object
print(CreateTeamResponse.to_json())

# convert the object into a dict
create_team_response_dict = create_team_response_instance.to_dict()
# create an instance of CreateTeamResponse from a dict
create_team_response_from_dict = CreateTeamResponse.from_dict(create_team_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


