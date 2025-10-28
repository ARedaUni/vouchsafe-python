# vouchsafe_python.VerificationsApi

All URIs are relative to *https://app.vouchsafe.id/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_verification**](VerificationsApi.md#get_verification) | **GET** /verifications/{id} | 
[**list_verifications**](VerificationsApi.md#list_verifications) | **GET** /verifications | 
[**request_verification**](VerificationsApi.md#request_verification) | **POST** /verifications | 


# **get_verification**
> Verification get_verification(id)

Get a single verification by ID.

Returns the latest status and metadata for a verification you previously requested.

> This endpoint supports sandbox mode. [See how sandbox mode works](https://help.vouchsafe.id/en/articles/11979598-how-does-sandbox-mode-work).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import vouchsafe_python
from vouchsafe_python.models.verification import Verification
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
    api_instance = vouchsafe_python.VerificationsApi(api_client)
    id = 'id_example' # str | The verification ID returned when you requested it.

    try:
        api_response = api_instance.get_verification(id)
        print("The response of VerificationsApi->get_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerificationsApi->get_verification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The verification ID returned when you requested it. | 

### Return type

[**Verification**](Verification.md)

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

# **list_verifications**
> List[Verification] list_verifications(status=status)

List all verifications for your team.

This can be a long list, so filtering by status is recommended.

> This endpoint supports sandbox mode. [See how sandbox mode works](https://help.vouchsafe.id/en/articles/11979598-how-does-sandbox-mode-work).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import vouchsafe_python
from vouchsafe_python.models.status import Status
from vouchsafe_python.models.verification import Verification
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
    api_instance = vouchsafe_python.VerificationsApi(api_client)
    status = vouchsafe_python.Status() # Status | Optional status filter. (optional)

    try:
        api_response = api_instance.list_verifications(status=status)
        print("The response of VerificationsApi->list_verifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerificationsApi->list_verifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**Status**](.md)| Optional status filter. | [optional] 

### Return type

[**List[Verification]**](Verification.md)

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

# **request_verification**
> RequestVerificationResponse request_verification(request_verification_input)

Request a new verification.

Provide the user's email and the ID of one of your verification flows to send them through.

Vouchsafe will respond with:

- a URL to redirect to the user to
- a unique ID for you to track the verification

If you have enabled "On request creation" emails in your flow, this also sends them an email.

You can optionally provide more information/claims about the user, like their name, date of birth and address. Any that are provided will be checked against evidence the user gives, and mismatches will be flagged.

> This endpoint supports sandbox mode. [See how sandbox mode works](https://help.vouchsafe.id/en/articles/11979598-how-does-sandbox-mode-work).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import vouchsafe_python
from vouchsafe_python.models.request_verification_input import RequestVerificationInput
from vouchsafe_python.models.request_verification_response import RequestVerificationResponse
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
    api_instance = vouchsafe_python.VerificationsApi(api_client)
    request_verification_input = vouchsafe_python.RequestVerificationInput() # RequestVerificationInput | 

    try:
        api_response = api_instance.request_verification(request_verification_input)
        print("The response of VerificationsApi->request_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerificationsApi->request_verification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_verification_input** | [**RequestVerificationInput**](RequestVerificationInput.md)|  | 

### Return type

[**RequestVerificationResponse**](RequestVerificationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Verification created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorised |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

