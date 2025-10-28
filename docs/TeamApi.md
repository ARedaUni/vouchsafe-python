# vouchsafe_python.TeamApi

All URIs are relative to *https://app.vouchsafe.id/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_team**](TeamApi.md#create_team) | **POST** /team | 
[**get_team**](TeamApi.md#get_team) | **GET** /team | 


# **create_team**
> CreateTeamResponse create_team(x_partner_token, create_team_input)

Create a new team (Partners only).

Creates a new team with the specified configuration and admin users.

Vouchsafe will respond with:

- a unique team ID for tracking
- the team name and public-facing name
- client credentials to authenticate team API requests
- creation timestamp (ISO 8601 format)

The provided admin emails will be granted administrative access to manage the team's settings and workflows.

**Note:** This endpoint requires a valid partner token in the `X-Partner-Token` header.

### Example


```python
import vouchsafe_python
from vouchsafe_python.models.create_team_input import CreateTeamInput
from vouchsafe_python.models.create_team_response import CreateTeamResponse
from vouchsafe_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.vouchsafe.id/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = vouchsafe_python.Configuration(
    host = "https://app.vouchsafe.id/api/v1"
)


# Enter a context with an instance of the API client
with vouchsafe_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vouchsafe_python.TeamApi(api_client)
    x_partner_token = 'x_partner_token_example' # str | 
    create_team_input = vouchsafe_python.CreateTeamInput() # CreateTeamInput | 

    try:
        api_response = api_instance.create_team(x_partner_token, create_team_input)
        print("The response of TeamApi->create_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->create_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_partner_token** | **str**|  | 
 **create_team_input** | [**CreateTeamInput**](CreateTeamInput.md)|  | 

### Return type

[**CreateTeamResponse**](CreateTeamResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorised |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team**
> Team get_team()


Get the currently authenticated team.

Helpful for testing, especially when managing multiple client IDs and secrets.

> This endpoint supports sandbox mode. [See how sandbox mode works](https://help.vouchsafe.id/en/articles/11979598-how-does-sandbox-mode-work).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import vouchsafe_python
from vouchsafe_python.models.team import Team
from vouchsafe_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.vouchsafe.id/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = vouchsafe_python.Configuration(
    host = "https://app.vouchsafe.id/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = vouchsafe_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with vouchsafe_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vouchsafe_python.TeamApi(api_client)

    try:
        api_response = api_instance.get_team()
        print("The response of TeamApi->get_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->get_team: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Team**](Team.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorised |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

