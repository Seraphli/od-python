# od_python.MatchesApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**matches_match_id_get**](MatchesApi.md#matches_match_id_get) | **GET** /matches/{match_id} | GET /matches/{match_id}


# **matches_match_id_get**
> InlineResponse200 matches_match_id_get(match_id)

GET /matches/{match_id}

Match data

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.MatchesApi()
match_id = 56 # int | 

try: 
    # GET /matches/{match_id}
    api_response = api_instance.matches_match_id_get(match_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchesApi->matches_match_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

