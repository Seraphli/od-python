# od_python.DistributionsApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**distributions_get**](DistributionsApi.md#distributions_get) | **GET** /distributions | GET /distributions


# **distributions_get**
> InlineResponse20018 distributions_get()

GET /distributions

Distributions of MMR data by bracket and country

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.DistributionsApi()

try: 
    # GET /distributions
    api_response = api_instance.distributions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionsApi->distributions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

