import requests

USERNAME = "kyhuynh"
TOKEN = "token-test-123"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# Create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
