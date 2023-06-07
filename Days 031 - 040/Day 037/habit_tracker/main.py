import requests as rq
import os
from datetime import datetime

USERNAME = "kaestoja"
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = "graph2"

today = datetime.now().strftime("%Y%m%d")

PIXELA_ENDPOINT_USER = "https://pixe.la/v1/users"
PIXELA_ENDPOINT_GRAPH = f"{PIXELA_ENDPOINT_USER}/{USERNAME}/graphs"
PIXELA_ENDPOINT_PIXEL = f"{PIXELA_ENDPOINT_GRAPH}/{GRAPH_ID}"
PIXELA_ENDPOINT_CHANGE_DELETE = f"{PIXELA_ENDPOINT_PIXEL}/{today}"

user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
}
graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "kuro"
}
pixel_params = {
    "date": today,
    "quantity": "15.48",
}
change_params = {
    "quantity": "18.57",
}
headers = {
    "X-USER-TOKEN": TOKEN
}


# response = rq.post(url=PIXELA_ENDPOINT_USER, json=user_params)
# response = rq.post(url=PIXELA_ENDPOINT_GRAPH, json=graph_params, headers=headers)
# response = rq.post(url=PIXELA_ENDPOINT_PIXEL, json=pixel_params, headers=headers)
# response = rq.put(url=PIXELA_ENDPOINT_CHANGE_DELETE, json=change_params, headers=headers)
response = rq.delete(url=PIXELA_ENDPOINT_CHANGE_DELETE, headers=headers)

print(response.text)
