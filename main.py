import requests
from datetime import datetime

# <<-- Necessary Details for Project -->>

TOKEN = "gggghhhhggg"
USERNAME = "heighter"
graph_id = "graph2"
headers = {
    "X-USER-TOKEN": TOKEN
}
# ---------------------------------

# <<-- Pixela Main Credentials for creating user -->>

pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response = requests.post(url=pixela_endpoint, json=user_parameters)
#print(response.text)
# ---------------------------------


# <<-- For making Graph Credentials-->>

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": graph_id,
    "name": "Walking Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(graph_response.text)
# ---------------------------------

# <<-- Posting Data into Pixela Graph Credentials -->>

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
today = datetime.now()
#print(today.strftime("%Y%m%d"))
post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Kilometers did you Walk: ")
}
post_response = requests.post(url=post_endpoint, json=post_config, headers=headers)
print(post_response.text)
# ---------------------------------

# <<-- Updating Data into Pixela Graph Credentials -->>

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"
update_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3.2"
}
update_response = requests.post(url=post_endpoint, json=update_config, headers=headers)
print(update_response.text)
# ---------------------------------

# <<-- Deleting Data into Pixela Graph Credentials -->>

'''
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"
delete_response = requests.delete(url=delete_endpoint,headers=headers)
print(delete_response.text) 
'''
