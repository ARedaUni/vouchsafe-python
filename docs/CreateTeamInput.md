# CreateTeamInput

Input for creating a new team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the team. | 
**public_name** | **str** | The public name of the team, shown in end-user facing screens and communications. If set, overrides the name. | [optional] 
**logo_url** | **str** | Path to the team&#39;s logo image. | [optional] 
**team_admin_emails** | **List[str]** | Email addresses of users to add as team administrators. | 
**flow_template** | [**FlowTemplate**](FlowTemplate.md) |  | [optional] 

## Example

```python
from vouchsafe_python.models.create_team_input import CreateTeamInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTeamInput from a JSON string
create_team_input_instance = CreateTeamInput.from_json(json)
# print the JSON string representation of the object
print(CreateTeamInput.to_json())

# convert the object into a dict
create_team_input_dict = create_team_input_instance.to_dict()
# create an instance of CreateTeamInput from a dict
create_team_input_from_dict = CreateTeamInput.from_dict(create_team_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


