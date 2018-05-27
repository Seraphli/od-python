# od_python.LiveApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**live_get**](LiveApi.md#live_get) | **GET** /live | GET /live


# **live_get**
> list[object] live_get()

GET /live

Get top currently ongoing live games

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.LiveApi()

try: 
    # GET /live
    api_response = api_instance.live_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveApi->live_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

