# vouchsafe_python.SmartLookupsApi

All URIs are relative to *https://app.vouchsafe.id/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**perform_smart_lookup**](SmartLookupsApi.md#perform_smart_lookup) | **POST** /smart-lookups | 
[**search_postcode**](SmartLookupsApi.md#search_postcode) | **GET** /smart-lookups/postcode | 


# **perform_smart_lookup**
> GetSmartLookupResponse perform_smart_lookup(smart_lookup_input)

> This feature is currently experimental, so the only supported check is `Address` via the electoral roll. Other checks coming soon.

Run quick [background checks](https://help.vouchsafe.id/en/articles/11075009-how-background-checks-work) on a user's details.

Provide the user's details and the check or checks to run and receive the report.

First line of address should be taken from the results returned by the [`GET /postcode` endpoint](https://localhost:3000/docs/operations/SearchPostcode).

> This endpoint supports sandbox mode. [See how sandbox mode works](https://help.vouchsafe.id/en/articles/11979598-how-does-sandbox-mode-work).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import vouchsafe_python
from vouchsafe_python.models.get_smart_lookup_response import GetSmartLookupResponse
from vouchsafe_python.models.smart_lookup_input import SmartLookupInput
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
    api_instance = vouchsafe_python.SmartLookupsApi(api_client)
    smart_lookup_input = vouchsafe_python.SmartLookupInput() # SmartLookupInput | 

    try:
        api_response = api_instance.perform_smart_lookup(smart_lookup_input)
        print("The response of SmartLookupsApi->perform_smart_lookup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartLookupsApi->perform_smart_lookup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_lookup_input** | [**SmartLookupInput**](SmartLookupInput.md)|  | 

### Return type

[**GetSmartLookupResponse**](GetSmartLookupResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Performed successfully, report available |  -  |
**400** | Bad request |  -  |
**401** | Unauthorised |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_postcode**
> PostcodeResponse search_postcode(postcode)

Look up all addresses for a given UK postcode in the Post Office Address File.

Useful for guaranteeing that a user's address is recognised before onboarding.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import vouchsafe_python
from vouchsafe_python.models.postcode_response import PostcodeResponse
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
    api_instance = vouchsafe_python.SmartLookupsApi(api_client)
    postcode = 'postcode_example' # str | UK postcode to search for. Example: `SW1A 2AA` Can be with or without space. Case insensitive.

    try:
        api_response = api_instance.search_postcode(postcode)
        print("The response of SmartLookupsApi->search_postcode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartLookupsApi->search_postcode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **postcode** | **str**| UK postcode to search for. Example: &#x60;SW1A 2AA&#x60; Can be with or without space. Case insensitive. | 

### Return type

[**PostcodeResponse**](PostcodeResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of matching addresses |  -  |
**400** | Malformed or non-existent postcode |  -  |
**401** | Unauthorised |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

