# Team


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The client ID of the team, as shown in the dashboard | 
**name** | **str** | The name of the team | 
**public_name** | **str** | The public name of the team, shown in end-user facing screens and communications. If set, overrides the name. | 
**plan** | **str** | Which plan is the team on? | 
**logo_url** | **str** | Path to the team&#39;s logo image | 
**updated_at** | **str** | When the team&#39;s details were last changed, formatted as an ISO 8601 string | 
**created_at** | **str** | When the team was created, formatted as an ISO 8601 string | 

## Example

```python
from vouchsafe_python.models.team import Team

# TODO update the JSON string below
json = "{}"
# create an instance of Team from a JSON string
team_instance = Team.from_json(json)
# print the JSON string representation of the object
print(Team.to_json())

# convert the object into a dict
team_dict = team_instance.to_dict()
# create an instance of Team from a dict
team_from_dict = Team.from_dict(team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


