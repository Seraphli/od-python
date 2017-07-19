# swagger_client.ExplorerApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**explorer_get**](ExplorerApi.md#explorer_get) | **GET** /explorer | GET /explorer


# **explorer_get**
> object explorer_get(sql=sql)

GET /explorer

Submit arbitrary SQL queries to the database

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExplorerApi()
sql = 'sql_example' # str | The PostgreSQL query as percent-encoded string. (optional)

try: 
    # GET /explorer
    api_response = api_instance.explorer_get(sql=sql)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExplorerApi->explorer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sql** | **str**| The PostgreSQL query as percent-encoded string. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

