# swagger_client.SchemaApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schema_get**](SchemaApi.md#schema_get) | **GET** /schema | GET /schema


# **schema_get**
> list[InlineResponse20027] schema_get()

GET /schema

Get database schema

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SchemaApi()

try: 
    # GET /schema
    api_response = api_instance.schema_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaApi->schema_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse20027]**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

