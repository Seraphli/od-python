# od_python.HeroesApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**heroes_get**](HeroesApi.md#heroes_get) | **GET** /heroes | GET /heroes
[**heroes_hero_id_durations_get**](HeroesApi.md#heroes_hero_id_durations_get) | **GET** /heroes/{hero_id}/durations | GET /heroes/{hero_id}/durations
[**heroes_hero_id_matches_get**](HeroesApi.md#heroes_hero_id_matches_get) | **GET** /heroes/{hero_id}/matches | GET /heroes/{hero_id}/matches
[**heroes_hero_id_matchups_get**](HeroesApi.md#heroes_hero_id_matchups_get) | **GET** /heroes/{hero_id}/matchups | GET /heroes/{hero_id}/matchups
[**heroes_hero_id_players_get**](HeroesApi.md#heroes_hero_id_players_get) | **GET** /heroes/{hero_id}/players | GET /heroes/{hero_id}/players


# **heroes_get**
> list[InlineResponse20021] heroes_get()

GET /heroes

Get hero data

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.HeroesApi()

try: 
    # GET /heroes
    api_response = api_instance.heroes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeroesApi->heroes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse20021]**](InlineResponse20021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heroes_hero_id_durations_get**
> list[InlineResponse20023] heroes_hero_id_durations_get()

GET /heroes/{hero_id}/durations

Get hero performance over a range of match durations

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.HeroesApi()

try: 
    # GET /heroes/{hero_id}/durations
    api_response = api_instance.heroes_hero_id_durations_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeroesApi->heroes_hero_id_durations_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse20023]**](InlineResponse20023.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heroes_hero_id_matches_get**
> list[InlineResponse20014] heroes_hero_id_matches_get()

GET /heroes/{hero_id}/matches

Get recent matches with a hero

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.HeroesApi()

try: 
    # GET /heroes/{hero_id}/matches
    api_response = api_instance.heroes_hero_id_matches_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeroesApi->heroes_hero_id_matches_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse20014]**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heroes_hero_id_matchups_get**
> list[InlineResponse20021] heroes_hero_id_matchups_get()

GET /heroes/{hero_id}/matchups

Get results against other heroes for a hero

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.HeroesApi()

try: 
    # GET /heroes/{hero_id}/matchups
    api_response = api_instance.heroes_hero_id_matchups_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeroesApi->heroes_hero_id_matchups_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse20021]**](InlineResponse20021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heroes_hero_id_players_get**
> list[list[object]] heroes_hero_id_players_get()

GET /heroes/{hero_id}/players

Get players who have played this hero

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.HeroesApi()

try: 
    # GET /heroes/{hero_id}/players
    api_response = api_instance.heroes_hero_id_players_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeroesApi->heroes_hero_id_players_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[list[object]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

