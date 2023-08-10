import os
import requests
from datetime import *

TOKEN = os.environ.get("AUTH_TOKEN")
USERNAME = os.environ.get("USER_IDENTIFICATION")

GRAPH_ID = "graph-2"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Programing Graph",
    "unit": "contributions",
    "type": "int",
    "color": "kuro",
    "timezone": "Poland",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

POST_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_config['id']}"

date = datetime.now()
date_formatted = date.strftime("%Y%m%d")

pixel_data = {
    "date": date_formatted,
    "quantity": input("How many contributions have you submitted today?"),
    # "optionalData": "",
}

response = requests.post(url=POST_PIXEL_ENDPOINT, json=pixel_data, headers=headers)
print(response.text)

PUT_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date_formatted}"

pixel_update = {
    "quantity": "3"
}

# response = requests.put(url=PUT_PIXEL_ENDPOINT, json=pixel_update, headers=headers)
# print(response.text)

DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date_formatted}"

# response = requests.delete(url=PUT_PIXEL_ENDPOINT, headers=headers)
# print(response.text)

