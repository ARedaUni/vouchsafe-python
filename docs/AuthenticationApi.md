# vouchsafe_python.AuthenticationApi

All URIs are relative to *https://app.vouchsafe.id/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate**](AuthenticationApi.md#authenticate) | **POST** /authenticate | 


# **authenticate**
> AuthenticateResponse authenticate(authenticate_input)

Get the access token, needed for all other API requests.

You will need your client ID and secret from the **API Integration** tab of the Vouchsafe dashboard.

Each access token is valid for 24 hours, after which you will need to re-authenticate.

Once you have an access token, pass it in future requests as a [Bearer token](https://workos.com/blog/understanding-bearer-tokens) in an `Authorization` header.

Use an [SDK or library](https://help.vouchsafe.id/en/articles/12026847-vouchsafe-sdks-and-libraries) to simplify handling tokens

> This endpoint supports sandbox mode. [See how sandbox mode works](https://help.vouchsafe.id/en/articles/11979598-how-does-sandbox-mode-work).

### Example


```python
import vouchsafe_python
from vouchsafe_python.models.authenticate_input import AuthenticateInput
from vouchsafe_python.models.authenticate_response import AuthenticateResponse
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
    api_instance = vouchsafe_python.AuthenticationApi(api_client)
    authenticate_input = vouchsafe_python.AuthenticateInput() # AuthenticateInput | 

    try:
        api_response = api_instance.authenticate(authenticate_input)
        print("The response of AuthenticationApi->authenticate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authenticate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticate_input** | [**AuthenticateInput**](AuthenticateInput.md)|  | 

### Return type

[**AuthenticateResponse**](AuthenticateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Token created successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorised |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

