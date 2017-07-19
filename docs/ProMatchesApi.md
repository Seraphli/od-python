# swagger_client.ProMatchesApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pro_matches_get**](ProMatchesApi.md#pro_matches_get) | **GET** /proMatches | GET /proMatches


# **pro_matches_get**
> list[InlineResponse20014] pro_matches_get(less_than_match_id=less_than_match_id)

GET /proMatches

Get list of pro matches

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProMatchesApi()
less_than_match_id = 56 # int | Get matches with a match ID lower than this value (optional)

try: 
    # GET /proMatches
    api_response = api_instance.pro_matches_get(less_than_match_id=less_than_match_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProMatchesApi->pro_matches_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **less_than_match_id** | **int**| Get matches with a match ID lower than this value | [optional] 

### Return type

[**list[InlineResponse20014]**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

