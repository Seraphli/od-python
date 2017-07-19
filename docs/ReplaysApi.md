# swagger_client.ReplaysApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**replays_get**](ReplaysApi.md#replays_get) | **GET** /replays | GET /replays


# **replays_get**
> list[InlineResponse20025] replays_get(match_id)

GET /replays

Get data to construct a replay URL with

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReplaysApi()
match_id = 56 # int | Match IDs (array)

try: 
    # GET /replays
    api_response = api_instance.replays_get(match_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplaysApi->replays_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**| Match IDs (array) | 

### Return type

[**list[InlineResponse20025]**](InlineResponse20025.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

