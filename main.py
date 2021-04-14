import requests
import os
from datetime import datetime

USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = "graph1"


# ---------------------------- CREATE ACCOUNT ------------------------------- #

pixel_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixel_endpoint, json=user_params)
# print(response.text)


# ---------------------------- CREATE GRAPH ------------------------------- #

graph_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs"

header = {
    "X-USER-TOKEN": TOKEN
}

# graph_config = {
#     "id": "graph1",
#     "name": "Coding graph",
#     "unit": "Hour",
#     "type": "float",
#     "color": "ajisai"
# }
#
# response = requests.post(url=graph_endpoint, headers=header, json=graph_config)
# print(response.text)


# ---------------------------- ADD PIXEL ------------------------------- #

post_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

# today = datetime(year=2021, month=2, day=13)
today = datetime.now()
format_date = today.strftime("%Y%m%d")

pixel_config = {
    "date": format_date,
    "quantity": input("How many hour do you work today?: "),
}

response = requests.post(url=post_pixel_endpoint, headers=header, json=pixel_config)
print(response.text)


# ---------------------------- UPDATE PIXEL ------------------------------- #

update_pixel_endpoint = f"{post_pixel_endpoint}/{format_date}"

update_pixel = {
    "quantity": "1"
}

# response = requests.put(url=update_pixel_endpoint, headers=header, json=update_pixel)
# print(response.text)


# ---------------------------- DELETE PIXEL ------------------------------- #

# response = requests.delete(url=update_pixel_endpoint, headers=header, json=update_pixel)
# print(response.text)
