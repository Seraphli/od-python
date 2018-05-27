# od_python.HeroStatsApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hero_stats_get**](HeroStatsApi.md#hero_stats_get) | **GET** /heroStats | GET /heroStats


# **hero_stats_get**
> list[InlineResponse20022] hero_stats_get()

GET /heroStats

Get stats about hero performance in recent matches

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.HeroStatsApi()

try: 
    # GET /heroStats
    api_response = api_instance.hero_stats_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeroStatsApi->hero_stats_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse20022]**](InlineResponse20022.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

