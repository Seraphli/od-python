# InlineResponse2004

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_id** | **int** | Match ID | [optional] 
**player_slot** | **int** | Which slot the player is in. 0-127 are Radiant, 128-255 are Dire | [optional] 
**radiant_win** | **bool** | Boolean indicating whether Radiant won the match | [optional] 
**duration** | **int** | Duration of the game in seconds | [optional] 
**game_mode** | **int** | Integer corresponding to game mode played. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/game_mode.json | [optional] 
**lobby_type** | **int** | Integer corresponding to lobby type of match. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/lobby_type.json | [optional] 
**hero_id** | **int** |  | [optional] 
**start_time** | **int** | Time the game started in seconds since 1970 | [optional] 
**version** | **int** | version | [optional] 
**kills** | **int** | Total kills the player had at the end of the game | [optional] 
**deaths** | **int** | Total deaths the player had at the end of the game | [optional] 
**assists** | **int** | Total assists the player had at the end of the game | [optional] 
**skill** | **int** | Skill bracket assigned by Valve (Normal, High, Very High) | [optional] 
**party_size** | **int** | Size of the player&#39;s party | [optional] 
**heroes** | [**PlayersaccountIdmatchesHeroes**](PlayersaccountIdmatchesHeroes.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


