import requests
from datetime import datetime

USERNAME = "piyush58"
TOKEN = "dfiu47iu49832hefhkjfkjndsf"
GRAPH_ID = "graph1"

# ----------------------- CREATE USER ACCOUNT ----------------------- #
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# ----------------------- CREATE GRAPH DEFINITION ----------------------- #
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Daily Commits",
    "unit": "commit",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# ----------------------- POST VALUE TO THE GRAPH ----------------------- #
value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now().strftime("%Y%m%d")

value_params = {
    "date": today,
    "quantity": input("HOW MANY COMMITS TODAY? : "),
}
response = requests.post(url=value_endpoint, json=value_params, headers=headers)
print(response.text)


# ----------------------- UPDATE PIXEL VALUE ----------------------- #
# put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
# put_params = {
#     "quantity": "2"
# }
# # response = requests.put(url=put_endpoint, json=put_params, headers=headers)
# # print(response.text)


# ----------------------- DELETE PIXEL ----------------------- #
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
#
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

