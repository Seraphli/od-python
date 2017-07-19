# od_python.MetadataApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metadata_get**](MetadataApi.md#metadata_get) | **GET** /metadata | GET /metadata


# **metadata_get**
> InlineResponse20017 metadata_get()

GET /metadata

Site metadata

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.MetadataApi()

try: 
    # GET /metadata
    api_response = api_instance.metadata_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->metadata_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

