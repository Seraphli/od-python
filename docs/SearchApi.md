# swagger_client.SearchApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_get**](SearchApi.md#search_get) | **GET** /search | GET /search


# **search_get**
> list[InlineResponse20019] search_get(q, similarity=similarity)

GET /search

Search players by personaname. Default similarity is 0.51

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
q = 'q_example' # str | Search string
similarity = 3.4 # float | Minimum similarity threshold, between 0 and 1 (optional)

try: 
    # GET /search
    api_response = api_instance.search_get(q, similarity=similarity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Search string | 
 **similarity** | **float**| Minimum similarity threshold, between 0 and 1 | [optional] 

### Return type

[**list[InlineResponse20019]**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

