# od_python.ProPlayersApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pro_players_get**](ProPlayersApi.md#pro_players_get) | **GET** /proPlayers | GET /proPlayers


# **pro_players_get**
> list[InlineResponse20013] pro_players_get()

GET /proPlayers

Get list of pro players

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.ProPlayersApi()

try: 
    # GET /proPlayers
    api_response = api_instance.pro_players_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProPlayersApi->pro_players_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse20013]**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

