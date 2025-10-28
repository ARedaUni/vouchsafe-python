# CreateTeamResponseCredentials

Production API credentials for this team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_secret** | **str** | Client secret for API authentication | 
**client_id** | **str** | Client ID for API authentication | 
**environment** | [**Model36EnumsEnvironment**](Model36EnumsEnvironment.md) |  | 
**name** | **str** | Name of the API key | 

## Example

```python
from vouchsafe_python.models.create_team_response_credentials import CreateTeamResponseCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTeamResponseCredentials from a JSON string
create_team_response_credentials_instance = CreateTeamResponseCredentials.from_json(json)
# print the JSON string representation of the object
print(CreateTeamResponseCredentials.to_json())

# convert the object into a dict
create_team_response_credentials_dict = create_team_response_credentials_instance.to_dict()
# create an instance of CreateTeamResponseCredentials from a dict
create_team_response_credentials_from_dict = CreateTeamResponseCredentials.from_dict(create_team_response_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


