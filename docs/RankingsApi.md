# od_python.RankingsApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rankings_get**](RankingsApi.md#rankings_get) | **GET** /rankings | GET /rankings


# **rankings_get**
> InlineResponse20019 rankings_get(hero_id)

GET /rankings

Top players by hero

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.RankingsApi()
hero_id = 'hero_id_example' # str | Hero ID

try: 
    # GET /rankings
    api_response = api_instance.rankings_get(hero_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankingsApi->rankings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hero_id** | **str**| Hero ID | 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

