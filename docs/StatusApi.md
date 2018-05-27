# od_python.StatusApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_api_metrics_get**](StatusApi.md#admin_api_metrics_get) | **GET** /admin/apiMetrics | GET /admin/apiMetrics
[**status_get**](StatusApi.md#status_get) | **GET** /status | GET /status


# **admin_api_metrics_get**
> object admin_api_metrics_get()

GET /admin/apiMetrics

Get API request metrics

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.StatusApi()

try: 
    # GET /admin/apiMetrics
    api_response = api_instance.admin_api_metrics_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->admin_api_metrics_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_get**
> object status_get()

GET /status

Get current service statistics

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.StatusApi()

try: 
    # GET /status
    api_response = api_instance.status_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->status_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

