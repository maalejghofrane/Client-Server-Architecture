import json
import requests
from requests.api import head

## constants 
USER_ID = "1229189739863068673"
NAME = "frostByte"
SCREEN_NAME = "MrabetChouaib"
BEARER = "AAAAAAAAAAAAAAAAAAAAAHkAWAEAAAAAeY2cd581sWENnwbXtkzjYBGCXOg%3DlrQuD2lQrRqhKviSlNRcntSJursTmn0XJ3gjvWbiMbppgUumP5"
REQ = f"https://api.twitter.com/1.1/users/show.json?screen_name={SCREEN_NAME}"
HEADERS = {"authorization": f"Bearer {BEARER}"}

profile_info = requests.get(REQ,headers=HEADERS)
# from json object to python object
profile_info_deserialized = json.loads(profile_info.text) 
print(profile_info_deserialized['id'])
print(profile_info_deserialized["friends_count"])
print(profile_info_deserialized["followers_count"])

# REQ2 = f'https://api.twitter.com/1.1/friends/list.json?screen_name={SCREEN_NAME}'

## Friends for one user  
# friends_info = requests.get(REQ2,headers=HEADERS)
# # from json object to python object
# graph = {f"{SCREEN_NAME}":[]}
# friends_deserialized = json.loads(friends_info.text) 

# print(friends_deserialized)
# for users in friends_deserialized['users']:
#     graph[f"{SCREEN_NAME}"].append(users['screen_name'])
#     print(users['screen_name'])

## graph of friends of a given screen_name
REQG = f'https://api.twitter.com/1.1/friends/list.json?screen_name={SCREEN_NAME}'
friends_info = requests.get(REQG,headers=HEADERS)
friends_deserialized = json.loads(friends_info.text) 
# from json object to python object
graph = {f"{SCREEN_NAME}":[]}
for users in friends_deserialized['users']:
    graph[f"{SCREEN_NAME}"].append(users['screen_name'])
for friend in graph[f'{SCREEN_NAME}']:
    SCREEN_NAME = friend
    REQN = f'https://api.twitter.com/1.1/friends/list.json?screen_name={SCREEN_NAME}'
    friends_info2 = requests.get(REQN,headers=HEADERS)
    friends_deserialized2 = json.loads(friends_info2.text) 
    graph2 = {f"{SCREEN_NAME}":[]}
    for users in friends_deserialized2['users']:
        if users in friends_deserialized['users']:
            graph2[f"{SCREEN_NAME}"].append(users['screen_name'])
    graph.update(graph2)
print(graph)
