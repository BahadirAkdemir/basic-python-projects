from urllib import response
from wsgiref import headers
import requests
import json

endpoint = "https://pixe.la/v1/users"
USERNAME="zaphkielbach"
TOKEN="zaphkielbach1234"


"""params = {
    "token":"",
    "username":"",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

response = requests.post(url=endpoint, json=params)
print(response.text)"""

graph_endpoint = f"{endpoint}/{USERNAME}/graphs"

graph_params = {
    "id":"graph-1",
    "name":"Running Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}
headers = {
    "X-USER-TOKEN":TOKEN
}
send_params = {
    "date":"20220327",
    "quantity":"1.5"
}
put_params = {
    "X-USER-TOKEN":TOKEN,
    "quantity":"2.5"
}
delete_params = {
    "X-USER-TOKEN":TOKEN,
}
date="20220328"

send_endpoint = f"{graph_endpoint}/{graph_params['id']}"
put_endpoint = f"{graph_endpoint}/{graph_params['id']}/{date}"
delete_endpoint = f"{graph_endpoint}/{graph_params['id']}/{date}"
print(send_endpoint)
#response=requests.post(url=send_endpoint, json=send_params, headers=headers)
#response=requests.put(url=put_endpoint, json=put_params, headers=headers)
response=requests.delete(url=delete_endpoint, json=delete_params, headers=headers)
print(response.text)


