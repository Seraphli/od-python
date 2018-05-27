# od_python.ScenariosApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scenarios_item_timings_get**](ScenariosApi.md#scenarios_item_timings_get) | **GET** /scenarios/itemTimings | GET /scenarios/itemTimings
[**scenarios_lane_roles_get**](ScenariosApi.md#scenarios_lane_roles_get) | **GET** /scenarios/laneRoles | GET /scenarios/laneRoles
[**scenarios_misc_get**](ScenariosApi.md#scenarios_misc_get) | **GET** /scenarios/misc | GET /scenarios/misc


# **scenarios_item_timings_get**
> list[InlineResponse20030] scenarios_item_timings_get(item=item, hero_id=hero_id)

GET /scenarios/itemTimings

Win rates for certain item timings on a hero for items that cost at least 1400 gold

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.ScenariosApi()
item = 'item_example' # str | Filter by item name e.g. \"spirit_vessel\" (optional)
hero_id = 56 # int | Hero ID (optional)

try: 
    # GET /scenarios/itemTimings
    api_response = api_instance.scenarios_item_timings_get(item=item, hero_id=hero_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScenariosApi->scenarios_item_timings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item** | **str**| Filter by item name e.g. \&quot;spirit_vessel\&quot; | [optional] 
 **hero_id** | **int**| Hero ID | [optional] 

### Return type

[**list[InlineResponse20030]**](InlineResponse20030.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scenarios_lane_roles_get**
> list[InlineResponse20031] scenarios_lane_roles_get(lane_role=lane_role, hero_id=hero_id)

GET /scenarios/laneRoles

Win rates for heroes in certain lane roles

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.ScenariosApi()
lane_role = 'lane_role_example' # str | Filter by lane role 1-4 (Safe, Mid, Off, Jungle) (optional)
hero_id = 56 # int | Hero ID (optional)

try: 
    # GET /scenarios/laneRoles
    api_response = api_instance.scenarios_lane_roles_get(lane_role=lane_role, hero_id=hero_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScenariosApi->scenarios_lane_roles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lane_role** | **str**| Filter by lane role 1-4 (Safe, Mid, Off, Jungle) | [optional] 
 **hero_id** | **int**| Hero ID | [optional] 

### Return type

[**list[InlineResponse20031]**](InlineResponse20031.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scenarios_misc_get**
> list[InlineResponse20032] scenarios_misc_get(scenario=scenario)

GET /scenarios/misc

Miscellaneous team scenarios

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.ScenariosApi()
scenario = 'scenario_example' # str | pos_chat_1min,neg_chat_1min,courier_kill,first_blood (optional)

try: 
    # GET /scenarios/misc
    api_response = api_instance.scenarios_misc_get(scenario=scenario)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScenariosApi->scenarios_misc_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenario** | **str**| pos_chat_1min,neg_chat_1min,courier_kill,first_blood | [optional] 

### Return type

[**list[InlineResponse20032]**](InlineResponse20032.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

