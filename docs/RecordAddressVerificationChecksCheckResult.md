# RecordAddressVerificationChecksCheckResult

Construct a type with a set of properties K of type T

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postcode_exists** | [**CheckResult**](CheckResult.md) |  | 
**address_exists** | [**CheckResult**](CheckResult.md) |  | 
**person_lives_at_address** | [**CheckResult**](CheckResult.md) |  | 

## Example

```python
from vouchsafe_python.models.record_address_verification_checks_check_result import RecordAddressVerificationChecksCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of RecordAddressVerificationChecksCheckResult from a JSON string
record_address_verification_checks_check_result_instance = RecordAddressVerificationChecksCheckResult.from_json(json)
# print the JSON string representation of the object
print(RecordAddressVerificationChecksCheckResult.to_json())

# convert the object into a dict
record_address_verification_checks_check_result_dict = record_address_verification_checks_check_result_instance.to_dict()
# create an instance of RecordAddressVerificationChecksCheckResult from a dict
record_address_verification_checks_check_result_from_dict = RecordAddressVerificationChecksCheckResult.from_dict(record_address_verification_checks_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


