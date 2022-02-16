import requests
import datetime as dt
import random

USERNAME = "kyhuynh"
TOKEN = "token-test-123"
GRAPH_ID = "walkinggraph"

pixela_endpoint = "https://pixe.la/v1/users"

# Create user
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#Create Graph
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_params = {
#     "id": GRAPH_ID,
#     "name": "Walking Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "momiji"
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# respons = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

#Add Pixel

headers = {
     "X-USER-TOKEN": TOKEN
}
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = dt.date.today()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": str(random.uniform(0, 9))
}
response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)