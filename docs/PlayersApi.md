# od_python.PlayersApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**players_account_id_counts_get**](PlayersApi.md#players_account_id_counts_get) | **GET** /players/{account_id}/counts | GET /players/{account_id}/counts
[**players_account_id_get**](PlayersApi.md#players_account_id_get) | **GET** /players/{account_id} | GET /players/{account_id}
[**players_account_id_heroes_get**](PlayersApi.md#players_account_id_heroes_get) | **GET** /players/{account_id}/heroes | GET /players/{account_id}/heroes
[**players_account_id_histograms_field_get**](PlayersApi.md#players_account_id_histograms_field_get) | **GET** /players/{account_id}/histograms/{field} | GET /players/{account_id}/histograms
[**players_account_id_matches_get**](PlayersApi.md#players_account_id_matches_get) | **GET** /players/{account_id}/matches | GET /players/{account_id}/matches
[**players_account_id_peers_get**](PlayersApi.md#players_account_id_peers_get) | **GET** /players/{account_id}/peers | GET /players/{account_id}/peers
[**players_account_id_pros_get**](PlayersApi.md#players_account_id_pros_get) | **GET** /players/{account_id}/pros | GET /players/{account_id}/pros
[**players_account_id_rankings_get**](PlayersApi.md#players_account_id_rankings_get) | **GET** /players/{account_id}/rankings | GET /players/{account_id}/rankings
[**players_account_id_ratings_get**](PlayersApi.md#players_account_id_ratings_get) | **GET** /players/{account_id}/ratings | GET /players/{account_id}/ratings
[**players_account_id_recent_matches_get**](PlayersApi.md#players_account_id_recent_matches_get) | **GET** /players/{account_id}/recentMatches | GET /players/{account_id}/recentMatches
[**players_account_id_refresh_post**](PlayersApi.md#players_account_id_refresh_post) | **POST** /players/{account_id}/refresh | POST /players/{account_id}/refresh
[**players_account_id_totals_get**](PlayersApi.md#players_account_id_totals_get) | **GET** /players/{account_id}/totals | GET /players/{account_id}/totals
[**players_account_id_wardmap_get**](PlayersApi.md#players_account_id_wardmap_get) | **GET** /players/{account_id}/wardmap | GET /players/{account_id}/wardmap
[**players_account_id_wl_get**](PlayersApi.md#players_account_id_wl_get) | **GET** /players/{account_id}/wl | GET /players/{account_id}/wl
[**players_account_id_wordcloud_get**](PlayersApi.md#players_account_id_wordcloud_get) | **GET** /players/{account_id}/wordcloud | GET /players/{account_id}/wordcloud


# **players_account_id_counts_get**
> InlineResponse2009 players_account_id_counts_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)

GET /players/{account_id}/counts

Counts in categories

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.PlayersApi()
account_id = 56 # int | Steam32 account ID
limit = 56 # int | Number of matches to limit to (optional)
offset = 56 # int | Number of matches to offset start by (optional)
win = 56 # int | Whether the player won (optional)
patch = 56 # int | Patch ID (optional)
game_mode = 56 # int | Game Mode ID (optional)
lobby_type = 56 # int | Lobby type ID (optional)
region = 56 # int | Region ID (optional)
date = 56 # int | Days previous (optional)
lane_role = 56 # int | Lane Role ID (optional)
hero_id = 56 # int | Hero ID (optional)
is_radiant = 56 # int | Whether the player was radiant (optional)
included_account_id = 56 # int | Account IDs in the match (array) (optional)
excluded_account_id = 56 # int | Account IDs not in the match (array) (optional)
with_hero_id = 56 # int | Hero IDs on the player's team (array) (optional)
against_hero_id = 56 # int | Hero IDs against the player's team (array) (optional)
significant = 56 # int | Whether the match was significant for aggregation purposes (optional)
having = 56 # int | The minimum number of games played, for filtering hero stats (optional)
sort = 'sort_example' # str | The field to return matches sorted by in descending order (optional)

try: 
    # GET /players/{account_id}/counts
    api_response = api_instance.players_account_id_counts_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->players_account_id_counts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID | 
 **limit** | **int**| Number of matches to limit to | [optional] 
 **offset** | **int**| Number of matches to offset start by | [optional] 
 **win** | **int**| Whether the player won | [optional] 
 **patch** | **int**| Patch ID | [optional] 
 **game_mode** | **int**| Game Mode ID | [optional] 
 **lobby_type** | **int**| Lobby type ID | [optional] 
 **region** | **int**| Region ID | [optional] 
 **date** | **int**| Days previous | [optional] 
 **lane_role** | **int**| Lane Role ID | [optional] 
 **hero_id** | **int**| Hero ID | [optional] 
 **is_radiant** | **int**| Whether the player was radiant | [optional] 
 **included_account_id** | **int**| Account IDs in the match (array) | [optional] 
 **excluded_account_id** | **int**| Account IDs not in the match (array) | [optional] 
 **with_hero_id** | **int**| Hero IDs on the player&#39;s team (array) | [optional] 
 **against_hero_id** | **int**| Hero IDs against the player&#39;s team (array) | [optional] 
 **significant** | **int**| Whether the match was significant for aggregation purposes | [optional] 
 **having** | **int**| The minimum number of games played, for filtering hero stats | [optional] 
 **sort** | **str**| The field to return matches sorted by in descending order | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **players_account_id_get**
> InlineResponse2001 players_account_id_get(account_id)

GET /players/{account_id}

Player data

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.PlayersApi()
account_id = 56 # int | Steam32 account ID

try: 
    # GET /players/{account_id}
    api_response = api_instance.players_account_id_get(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->players_account_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **players_account_id_heroes_get**
> list[InlineResponse2005] players_account_id_heroes_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)

GET /players/{account_id}/heroes

Heroes played

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.PlayersApi()
account_id = 56 # int | Steam32 account ID
limit = 56 # int | Number of matches to limit to (optional)
offset = 56 # int | Number of matches to offset start by (optional)
win = 56 # int | Whether the player won (optional)
patch = 56 # int | Patch ID (optional)
game_mode = 56 # int | Game Mode ID (optional)
lobby_type = 56 # int | Lobby type ID (optional)
region = 56 # int | Region ID (optional)
date = 56 # int | Days previous (optional)
lane_role = 56 # int | Lane Role ID (optional)
hero_id = 56 # int | Hero ID (optional)
is_radiant = 56 # int | Whether the player was radiant (optional)
included_account_id = 56 # int | Account IDs in the match (array) (optional)
excluded_account_id = 56 # int | Account IDs not in the match (array) (optional)
with_hero_id = 56 # int | Hero IDs on the player's team (array) (optional)
against_hero_id = 56 # int | Hero IDs against the player's team (array) (optional)
significant = 56 # int | Whether the match was significant for aggregation purposes (optional)
having = 56 # int | The minimum number of games played, for filtering hero stats (optional)
sort = 'sort_example' # str | The field to return matches sorted by in descending order (optional)

try: 
    # GET /players/{account_id}/heroes
    api_response = api_instance.players_account_id_heroes_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->players_account_id_heroes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID | 
 **limit** | **int**| Number of matches to limit to | [optional] 
 **offset** | **int**| Number of matches to offset start by | [optional] 
 **win** | **int**| Whether the player won | [optional] 
 **patch** | **int**| Patch ID | [optional] 
 **game_mode** | **int**| Game Mode ID | [optional] 
 **lobby_type** | **int**| Lobby type ID | [optional] 
 **region** | **int**| Region ID | [optional] 
 **date** | **int**| Days previous | [optional] 
 **lane_role** | **int**| Lane Role ID | [optional] 
 **hero_id** | **int**| Hero ID | [optional] 
 **is_radiant** | **int**| Whether the player was radiant | [optional] 
 **included_account_id** | **int**| Account IDs in the match (array) | [optional] 
 **excluded_account_id** | **int**| Account IDs not in the match (array) | [optional] 
 **with_hero_id** | **int**| Hero IDs on the player&#39;s team (array) | [optional] 
 **against_hero_id** | **int**| Hero IDs against the player&#39;s team (array) | [optional] 
 **significant** | **int**| Whether the match was significant for aggregation purposes | [optional] 
 **having** | **int**| The minimum number of games played, for filtering hero stats | [optional] 
 **sort** | **str**| The field to return matches sorted by in descending order | [optional] 

### Return type

[**list[InlineResponse2005]**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **players_account_id_histograms_field_get**
> list[object] players_account_id_histograms_field_get(account_id, field, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)

GET /players/{account_id}/histograms

Distribution of matches in a single stat

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.PlayersApi()
account_id = 56 # int | Steam32 account ID
field = 'field_example' # str | Field to aggregate on
limit = 56 # int | Number of matches to limit to (optional)
offset = 56 # int | Number of matches to offset start by (optional)
win = 56 # int | Whether the player won (optional)
patch = 56 # int | Patch ID (optional)
game_mode = 56 # int | Game Mode ID (optional)
lobby_type = 56 # int | Lobby type ID (optional)
region = 56 # int | Region ID (optional)
date = 56 # int | Days previous (optional)
lane_role = 56 # int | Lane Role ID (optional)
hero_id = 56 # int | Hero ID (optional)
is_radiant = 56 # int | Whether the player was radiant (optional)
included_account_id = 56 # int | Account IDs in the match (array) (optional)
excluded_account_id = 56 # int | Account IDs not in the match (array) (optional)
with_hero_id = 56 # int | Hero IDs on the player's team (array) (optional)
against_hero_id = 56 # int | Hero IDs against the player's team (array) (optional)
significant = 56 # int | Whether the match was significant for aggregation purposes (optional)
having = 56 # int | The minimum number of games played, for filtering hero stats (optional)
sort = 'sort_example' # str | The field to return matches sorted by in descending order (optional)

try: 
    # GET /players/{account_id}/histograms
    api_response = api_instance.players_account_id_histograms_field_get(account_id, field, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->players_account_id_histograms_field_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID | 
 **field** | **str**| Field to aggregate on | 
 **limit** | **int**| Number of matches to limit to | [optional] 
 **offset** | **int**| Number of matches to offset start by | [optional] 
 **win** | **int**| Whether the player won | [optional] 
 **patch** | **int**| Patch ID | [optional] 
 **game_mode** | **int**| Game Mode ID | [optional] 
 **lobby_type** | **int**| Lobby type ID | [optional] 
 **region** | **int**| Region ID | [optional] 
 **date** | **int**| Days previous | [optional] 
 **lane_role** | **int**| Lane Role ID | [optional] 
 **hero_id** | **int**| Hero ID | [optional] 
 **is_radiant** | **int**| Whether the player was radiant | [optional] 
 **included_account_id** | **int**| Account IDs in the match (array) | [optional] 
 **excluded_account_id** | **int**| Account IDs not in the match (array) | [optional] 
 **with_hero_id** | **int**| Hero IDs on the player&#39;s team (array) | [optional] 
 **against_hero_id** | **int**| Hero IDs against the player&#39;s team (array) | [optional] 
 **significant** | **int**| Whether the match was significant for aggregation purposes | [optional] 
 **having** | **int**| The minimum number of games played, for filtering hero stats | [optional] 
 **sort** | **str**| The field to return matches sorted by in descending order | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **players_account_id_matches_get**
> list[InlineResponse2004] players_account_id_matches_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort, project=project)

GET /players/{account_id}/matches

Matches played

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.PlayersApi()
account_id = 56 # int | Steam32 account ID
limit = 56 # int | Number of matches to limit to (optional)
offset = 56 # int | Number of matches to offset start by (optional)
win = 56 # int | Whether the player won (optional)
patch = 56 # int | Patch ID (optional)
game_mode = 56 # int | Game Mode ID (optional)
lobby_type = 56 # int | Lobby type ID (optional)
region = 56 # int | Region ID (optional)
date = 56 # int | Days previous (optional)
lane_role = 56 # int | Lane Role ID (optional)
hero_id = 56 # int | Hero ID (optional)
is_radiant = 56 # int | Whether the player was radiant (optional)
included_account_id = 56 # int | Account IDs in the match (array) (optional)
excluded_account_id = 56 # int | Account IDs not in the match (array) (optional)
with_hero_id = 56 # int | Hero IDs on the player's team (array) (optional)
against_hero_id = 56 # int | Hero IDs against the player's team (array) (optional)
significant = 56 # int | Whether the match was significant for aggregation purposes (optional)
having = 56 # int | The minimum number of games played, for filtering hero stats (optional)
sort = 'sort_example' # str | The field to return matches sorted by in descending order (optional)
project = 'project_example' # str | Fields to project (array) (optional)

try: 
    # GET /players/{account_id}/matches
    api_response = api_instance.players_account_id_matches_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->players_account_id_matches_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID | 
 **limit** | **int**| Number of matches to limit to | [optional] 
 **offset** | **int**| Number of matches to offset start by | [optional] 
 **win** | **int**| Whether the player won | [optional] 
 **patch** | **int**| Patch ID | [optional] 
 **game_mode** | **int**| Game Mode ID | [optional] 
 **lobby_type** | **int**| Lobby type ID | [optional] 
 **region** | **int**| Region ID | [optional] 
 **date** | **int**| Days previous | [optional] 
 **lane_role** | **int**| Lane Role ID | [optional] 
 **hero_id** | **int**| Hero ID | [optional] 
 **is_radiant** | **int**| Whether the player was radiant | [optional] 
 **included_account_id** | **int**| Account IDs in the match (array) | [optional] 
 **excluded_account_id** | **int**| Account IDs not in the match (array) | [optional] 
 **with_hero_id** | **int**| Hero IDs on the player&#39;s team (array) | [optional] 
 **against_hero_id** | **int**| Hero IDs against the player&#39;s team (array) | [optional] 
 **significant** | **int**| Whether the match was significant for aggregation purposes | [optional] 
 **having** | **int**| The minimum number of games played, for filtering hero stats | [optional] 
 **sort** | **str**| The field to return matches sorted by in descending order | [optional] 
 **project** | **str**| Fields to project (array) | [optional] 

### Return type

[**list[InlineResponse2004]**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **players_account_id_peers_get**
> list[InlineResponse2006] players_account_id_peers_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)

GET /players/{account_id}/peers

Players played with

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.PlayersApi()
account_id = 56 # int | Steam32 account ID
limit = 56 # int | Number of matches to limit to (optional)
offset = 56 # int | Number of matches to offset start by (optional)
win = 56 # int | Whether the player won (optional)
patch = 56 # int | Patch ID (optional)
game_mode = 56 # int | Game Mode ID (optional)
lobby_type = 56 # int | Lobby type ID (optional)
region = 56 # int | Region ID (optional)
date = 56 # int | Days previous (optional)
lane_role = 56 # int | Lane Role ID (optional)
hero_id = 56 # int | Hero ID (optional)
is_radiant = 56 # int | Whether the player was radiant (optional)
included_account_id = 56 # int | Account IDs in the match (array) (optional)
excluded_account_id = 56 # int | Account IDs not in the match (array) (optional)
with_hero_id = 56 # int | Hero IDs on the player's team (array) (optional)
against_hero_id = 56 # int | Hero IDs against the player's team (array) (optional)
significant = 56 # int | Whether the match was significant for aggregation purposes (optional)
having = 56 # int | The minimum number of games played, for filtering hero stats (optional)
sort = 'sort_example' # str | The field to return matches sorted by in descending order (optional)

try: 
    # GET /players/{account_id}/peers
    api_response = api_instance.players_account_id_peers_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->players_account_id_peers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID | 
 **limit** | **int**| Number of matches to limit to | [optional] 
 **offset** | **int**| Number of matches to offset start by | [optional] 
 **win** | **int**| Whether the player won | [optional] 
 **patch** | **int**| Patch ID | [optional] 
 **game_mode** | **int**| Game Mode ID | [optional] 
 **lobby_type** | **int**| Lobby type ID | [optional] 
 **region** | **int**| Region ID | [optional] 
 **date** | **int**| Days previous | [optional] 
 **lane_role** | **int**| Lane Role ID | [optional] 
 **hero_id** | **int**| Hero ID | [optional] 
 **is_radiant** | **int**| Whether the player was radiant | [optional] 
 **included_account_id** | **int**| Account IDs in the match (array) | [optional] 
 **excluded_account_id** | **int**| Account IDs not in the match (array) | [optional] 
 **with_hero_id** | **int**| Hero IDs on the player&#39;s team (array) | [optional] 
 **against_hero_id** | **int**| Hero IDs against the player&#39;s team (array) | [optional] 
 **significant** | **int**| Whether the match was significant for aggregation purposes | [optional] 
 **having** | **int**| The minimum number of games played, for filtering hero stats | [optional] 
 **sort** | **str**| The field to return matches sorted by in descending order | [optional] 

### Return type

[**list[InlineResponse2006]**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **players_account_id_pros_get**
> list[InlineResponse2007] players_account_id_pros_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)

GET /players/{account_id}/pros

Pro players played with

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.PlayersApi()
account_id = 56 # int | Steam32 account ID
limit = 56 # int | Number of matches to limit to (optional)
offset = 56 # int | Number of matches to offset start by (optional)
win = 56 # int | Whether the player won (optional)
patch = 56 # int | Patch ID (optional)
game_mode = 56 # int | Game Mode ID (optional)
lobby_type = 56 # int | Lobby type ID (optional)
region = 56 # int | Region ID (optional)
date = 56 # int | Days previous (optional)
lane_role = 56 # int | Lane Role ID (optional)
hero_id = 56 # int | Hero ID (optional)
is_radiant = 56 # int | Whether the player was radiant (optional)
included_account_id = 56 # int | Account IDs in the match (array) (optional)
excluded_account_id = 56 # int | Account IDs not in the match (array) (optional)
with_hero_id = 56 # int | Hero IDs on the player's team (array) (optional)
against_hero_id = 56 # int | Hero IDs against the player's team (array) (optional)
significant = 56 # int | Whether the match was significant for aggregation purposes (optional)
having = 56 # int | The minimum number of games played, for filtering hero stats (optional)
sort = 'sort_example' # str | The field to return matches sorted by in descending order (optional)

try: 
    # GET /players/{account_id}/pros
    api_response = api_instance.players_account_id_pros_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->players_account_id_pros_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID | 
 **limit** | **int**| Number of matches to limit to | [optional] 
 **offset** | **int**| Number of matches to offset start by | [optional] 
 **win** | **int**| Whether the player won | [optional] 
 **patch** | **int**| Patch ID | [optional] 
 **game_mode** | **int**| Game Mode ID | [optional] 
 **lobby_type** | **int**| Lobby type ID | [optional] 
 **region** | **int**| Region ID | [optional] 
 **date** | **int**| Days previous | [optional] 
 **lane_role** | **int**| Lane Role ID | [optional] 
 **hero_id** | **int**| Hero ID | [optional] 
 **is_radiant** | **int**| Whether the player was radiant | [optional] 
 **included_account_id** | **int**| Account IDs in the match (array) | [optional] 
 **excluded_account_id** | **int**| Account IDs not in the match (array) | [optional] 
 **with_hero_id** | **int**| Hero IDs on the player&#39;s team (array) | [optional] 
 **against_hero_id** | **int**| Hero IDs against the player&#39;s team (array) | [optional] 
 **significant** | **int**| Whether the match was significant for aggregation purposes | [optional] 
 **having** | **int**| The minimum number of games played, for filtering hero stats | [optional] 
 **sort** | **str**| The field to return matches sorted by in descending order | [optional] 

### Return type

[**list[InlineResponse2007]**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **players_account_id_rankings_get**
> list[object] players_account_id_rankings_get(account_id)

GET /players/{account_id}/rankings

Player hero rankings

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.PlayersApi()
account_id = 56 # int | Steam32 account ID

try: 
    # GET /players/{account_id}/rankings
    api_response = api_instance.players_account_id_rankings_get(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->players_account_id_rankings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **players_account_id_ratings_get**
> list[InlineResponse20012] players_account_id_ratings_get(account_id)

GET /players/{account_id}/ratings

Player rating history

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.PlayersApi()
account_id = 56 # int | Steam32 account ID

try: 
    # GET /players/{account_id}/ratings
    api_response = api_instance.players_account_id_ratings_get(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->players_account_id_ratings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID | 

### Return type

[**list[InlineResponse20012]**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **players_account_id_recent_matches_get**
> list[InlineResponse2003] players_account_id_recent_matches_get()

GET /players/{account_id}/recentMatches

Recent matches played

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.PlayersApi()

try: 
    # GET /players/{account_id}/recentMatches
    api_response = api_instance.players_account_id_recent_matches_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->players_account_id_recent_matches_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse2003]**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **players_account_id_refresh_post**
> object players_account_id_refresh_post(account_id)

POST /players/{account_id}/refresh

Refresh player match history

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.PlayersApi()
account_id = 56 # int | Steam32 account ID

try: 
    # POST /players/{account_id}/refresh
    api_response = api_instance.players_account_id_refresh_post(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->players_account_id_refresh_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **players_account_id_totals_get**
> list[InlineResponse2008] players_account_id_totals_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)

GET /players/{account_id}/totals

Totals in stats

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.PlayersApi()
account_id = 56 # int | Steam32 account ID
limit = 56 # int | Number of matches to limit to (optional)
offset = 56 # int | Number of matches to offset start by (optional)
win = 56 # int | Whether the player won (optional)
patch = 56 # int | Patch ID (optional)
game_mode = 56 # int | Game Mode ID (optional)
lobby_type = 56 # int | Lobby type ID (optional)
region = 56 # int | Region ID (optional)
date = 56 # int | Days previous (optional)
lane_role = 56 # int | Lane Role ID (optional)
hero_id = 56 # int | Hero ID (optional)
is_radiant = 56 # int | Whether the player was radiant (optional)
included_account_id = 56 # int | Account IDs in the match (array) (optional)
excluded_account_id = 56 # int | Account IDs not in the match (array) (optional)
with_hero_id = 56 # int | Hero IDs on the player's team (array) (optional)
against_hero_id = 56 # int | Hero IDs against the player's team (array) (optional)
significant = 56 # int | Whether the match was significant for aggregation purposes (optional)
having = 56 # int | The minimum number of games played, for filtering hero stats (optional)
sort = 'sort_example' # str | The field to return matches sorted by in descending order (optional)

try: 
    # GET /players/{account_id}/totals
    api_response = api_instance.players_account_id_totals_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->players_account_id_totals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID | 
 **limit** | **int**| Number of matches to limit to | [optional] 
 **offset** | **int**| Number of matches to offset start by | [optional] 
 **win** | **int**| Whether the player won | [optional] 
 **patch** | **int**| Patch ID | [optional] 
 **game_mode** | **int**| Game Mode ID | [optional] 
 **lobby_type** | **int**| Lobby type ID | [optional] 
 **region** | **int**| Region ID | [optional] 
 **date** | **int**| Days previous | [optional] 
 **lane_role** | **int**| Lane Role ID | [optional] 
 **hero_id** | **int**| Hero ID | [optional] 
 **is_radiant** | **int**| Whether the player was radiant | [optional] 
 **included_account_id** | **int**| Account IDs in the match (array) | [optional] 
 **excluded_account_id** | **int**| Account IDs not in the match (array) | [optional] 
 **with_hero_id** | **int**| Hero IDs on the player&#39;s team (array) | [optional] 
 **against_hero_id** | **int**| Hero IDs against the player&#39;s team (array) | [optional] 
 **significant** | **int**| Whether the match was significant for aggregation purposes | [optional] 
 **having** | **int**| The minimum number of games played, for filtering hero stats | [optional] 
 **sort** | **str**| The field to return matches sorted by in descending order | [optional] 

### Return type

[**list[InlineResponse2008]**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **players_account_id_wardmap_get**
> InlineResponse20010 players_account_id_wardmap_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)

GET /players/{account_id}/wardmap

Wards placed in matches played

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.PlayersApi()
account_id = 56 # int | Steam32 account ID
limit = 56 # int | Number of matches to limit to (optional)
offset = 56 # int | Number of matches to offset start by (optional)
win = 56 # int | Whether the player won (optional)
patch = 56 # int | Patch ID (optional)
game_mode = 56 # int | Game Mode ID (optional)
lobby_type = 56 # int | Lobby type ID (optional)
region = 56 # int | Region ID (optional)
date = 56 # int | Days previous (optional)
lane_role = 56 # int | Lane Role ID (optional)
hero_id = 56 # int | Hero ID (optional)
is_radiant = 56 # int | Whether the player was radiant (optional)
included_account_id = 56 # int | Account IDs in the match (array) (optional)
excluded_account_id = 56 # int | Account IDs not in the match (array) (optional)
with_hero_id = 56 # int | Hero IDs on the player's team (array) (optional)
against_hero_id = 56 # int | Hero IDs against the player's team (array) (optional)
significant = 56 # int | Whether the match was significant for aggregation purposes (optional)
having = 56 # int | The minimum number of games played, for filtering hero stats (optional)
sort = 'sort_example' # str | The field to return matches sorted by in descending order (optional)

try: 
    # GET /players/{account_id}/wardmap
    api_response = api_instance.players_account_id_wardmap_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->players_account_id_wardmap_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID | 
 **limit** | **int**| Number of matches to limit to | [optional] 
 **offset** | **int**| Number of matches to offset start by | [optional] 
 **win** | **int**| Whether the player won | [optional] 
 **patch** | **int**| Patch ID | [optional] 
 **game_mode** | **int**| Game Mode ID | [optional] 
 **lobby_type** | **int**| Lobby type ID | [optional] 
 **region** | **int**| Region ID | [optional] 
 **date** | **int**| Days previous | [optional] 
 **lane_role** | **int**| Lane Role ID | [optional] 
 **hero_id** | **int**| Hero ID | [optional] 
 **is_radiant** | **int**| Whether the player was radiant | [optional] 
 **included_account_id** | **int**| Account IDs in the match (array) | [optional] 
 **excluded_account_id** | **int**| Account IDs not in the match (array) | [optional] 
 **with_hero_id** | **int**| Hero IDs on the player&#39;s team (array) | [optional] 
 **against_hero_id** | **int**| Hero IDs against the player&#39;s team (array) | [optional] 
 **significant** | **int**| Whether the match was significant for aggregation purposes | [optional] 
 **having** | **int**| The minimum number of games played, for filtering hero stats | [optional] 
 **sort** | **str**| The field to return matches sorted by in descending order | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **players_account_id_wl_get**
> InlineResponse2002 players_account_id_wl_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)

GET /players/{account_id}/wl

Win/Loss count

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.PlayersApi()
account_id = 56 # int | Steam32 account ID
limit = 56 # int | Number of matches to limit to (optional)
offset = 56 # int | Number of matches to offset start by (optional)
win = 56 # int | Whether the player won (optional)
patch = 56 # int | Patch ID (optional)
game_mode = 56 # int | Game Mode ID (optional)
lobby_type = 56 # int | Lobby type ID (optional)
region = 56 # int | Region ID (optional)
date = 56 # int | Days previous (optional)
lane_role = 56 # int | Lane Role ID (optional)
hero_id = 56 # int | Hero ID (optional)
is_radiant = 56 # int | Whether the player was radiant (optional)
included_account_id = 56 # int | Account IDs in the match (array) (optional)
excluded_account_id = 56 # int | Account IDs not in the match (array) (optional)
with_hero_id = 56 # int | Hero IDs on the player's team (array) (optional)
against_hero_id = 56 # int | Hero IDs against the player's team (array) (optional)
significant = 56 # int | Whether the match was significant for aggregation purposes (optional)
having = 56 # int | The minimum number of games played, for filtering hero stats (optional)
sort = 'sort_example' # str | The field to return matches sorted by in descending order (optional)

try: 
    # GET /players/{account_id}/wl
    api_response = api_instance.players_account_id_wl_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->players_account_id_wl_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID | 
 **limit** | **int**| Number of matches to limit to | [optional] 
 **offset** | **int**| Number of matches to offset start by | [optional] 
 **win** | **int**| Whether the player won | [optional] 
 **patch** | **int**| Patch ID | [optional] 
 **game_mode** | **int**| Game Mode ID | [optional] 
 **lobby_type** | **int**| Lobby type ID | [optional] 
 **region** | **int**| Region ID | [optional] 
 **date** | **int**| Days previous | [optional] 
 **lane_role** | **int**| Lane Role ID | [optional] 
 **hero_id** | **int**| Hero ID | [optional] 
 **is_radiant** | **int**| Whether the player was radiant | [optional] 
 **included_account_id** | **int**| Account IDs in the match (array) | [optional] 
 **excluded_account_id** | **int**| Account IDs not in the match (array) | [optional] 
 **with_hero_id** | **int**| Hero IDs on the player&#39;s team (array) | [optional] 
 **against_hero_id** | **int**| Hero IDs against the player&#39;s team (array) | [optional] 
 **significant** | **int**| Whether the match was significant for aggregation purposes | [optional] 
 **having** | **int**| The minimum number of games played, for filtering hero stats | [optional] 
 **sort** | **str**| The field to return matches sorted by in descending order | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **players_account_id_wordcloud_get**
> InlineResponse20011 players_account_id_wordcloud_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)

GET /players/{account_id}/wordcloud

Words said/read in matches played

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.PlayersApi()
account_id = 56 # int | Steam32 account ID
limit = 56 # int | Number of matches to limit to (optional)
offset = 56 # int | Number of matches to offset start by (optional)
win = 56 # int | Whether the player won (optional)
patch = 56 # int | Patch ID (optional)
game_mode = 56 # int | Game Mode ID (optional)
lobby_type = 56 # int | Lobby type ID (optional)
region = 56 # int | Region ID (optional)
date = 56 # int | Days previous (optional)
lane_role = 56 # int | Lane Role ID (optional)
hero_id = 56 # int | Hero ID (optional)
is_radiant = 56 # int | Whether the player was radiant (optional)
included_account_id = 56 # int | Account IDs in the match (array) (optional)
excluded_account_id = 56 # int | Account IDs not in the match (array) (optional)
with_hero_id = 56 # int | Hero IDs on the player's team (array) (optional)
against_hero_id = 56 # int | Hero IDs against the player's team (array) (optional)
significant = 56 # int | Whether the match was significant for aggregation purposes (optional)
having = 56 # int | The minimum number of games played, for filtering hero stats (optional)
sort = 'sort_example' # str | The field to return matches sorted by in descending order (optional)

try: 
    # GET /players/{account_id}/wordcloud
    api_response = api_instance.players_account_id_wordcloud_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->players_account_id_wordcloud_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID | 
 **limit** | **int**| Number of matches to limit to | [optional] 
 **offset** | **int**| Number of matches to offset start by | [optional] 
 **win** | **int**| Whether the player won | [optional] 
 **patch** | **int**| Patch ID | [optional] 
 **game_mode** | **int**| Game Mode ID | [optional] 
 **lobby_type** | **int**| Lobby type ID | [optional] 
 **region** | **int**| Region ID | [optional] 
 **date** | **int**| Days previous | [optional] 
 **lane_role** | **int**| Lane Role ID | [optional] 
 **hero_id** | **int**| Hero ID | [optional] 
 **is_radiant** | **int**| Whether the player was radiant | [optional] 
 **included_account_id** | **int**| Account IDs in the match (array) | [optional] 
 **excluded_account_id** | **int**| Account IDs not in the match (array) | [optional] 
 **with_hero_id** | **int**| Hero IDs on the player&#39;s team (array) | [optional] 
 **against_hero_id** | **int**| Hero IDs against the player&#39;s team (array) | [optional] 
 **significant** | **int**| Whether the match was significant for aggregation purposes | [optional] 
 **having** | **int**| The minimum number of games played, for filtering hero stats | [optional] 
 **sort** | **str**| The field to return matches sorted by in descending order | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

