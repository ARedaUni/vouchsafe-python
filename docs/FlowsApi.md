# vouchsafe_python.FlowsApi

All URIs are relative to *https://app.vouchsafe.id/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_flow**](FlowsApi.md#get_flow) | **GET** /flows/{id} | 
[**list_flows**](FlowsApi.md#list_flows) | **GET** /flows | 


# **get_flow**
> Flow get_flow(id)


Get a specific verification flow.

Use an ID from one of these flows to request verifications with the  [`POST /verifications` endpoint](https://localhost:3000/docs/operations/RequestVerification).

> This endpoint supports sandbox mode. [See how sandbox mode works](https://help.vouchsafe.id/en/articles/11979598-how-does-sandbox-mode-work).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import vouchsafe_python
from vouchsafe_python.models.flow import Flow
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
    api_instance = vouchsafe_python.FlowsApi(api_client)
    id = 'id_example' # str | The ID of the flow to retrieve.

    try:
        api_response = api_instance.get_flow(id)
        print("The response of FlowsApi->get_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->get_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the flow to retrieve. | 

### Return type

[**Flow**](Flow.md)

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_flows**
> List[Flow] list_flows()


Get a list of all the currently published verification flows.

Use an ID from one of these flows to request verifications with the  [`POST /verifications` endpoint](https://localhost:3000/docs/operations/RequestVerification).

Referee-specific verification flows cannot be started independently, so are not returned by this endpoint.

> This endpoint supports sandbox mode. [See how sandbox mode works](https://help.vouchsafe.id/en/articles/11979598-how-does-sandbox-mode-work).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import vouchsafe_python
from vouchsafe_python.models.flow import Flow
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
    api_instance = vouchsafe_python.FlowsApi(api_client)

    try:
        api_response = api_instance.list_flows()
        print("The response of FlowsApi->list_flows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->list_flows: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Flow]**](Flow.md)

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

