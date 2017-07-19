# swagger_client.RequestApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_job_id_get**](RequestApi.md#request_job_id_get) | **GET** /request/{jobId} | GET /request/{jobId}
[**request_match_id_post**](RequestApi.md#request_match_id_post) | **POST** /request/{match_id} | POST /request/{match_id}


# **request_job_id_get**
> object request_job_id_get(job_id)

GET /request/{jobId}

Get parse request state

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RequestApi()
job_id = 'job_id_example' # str | The job ID to query.

try: 
    # GET /request/{jobId}
    api_response = api_instance.request_job_id_get(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequestApi->request_job_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID to query. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_match_id_post**
> object request_match_id_post(match_id)

POST /request/{match_id}

Submit a new parse request

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RequestApi()
match_id = 56 # int | 

try: 
    # POST /request/{match_id}
    api_response = api_instance.request_match_id_post(match_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequestApi->request_match_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

