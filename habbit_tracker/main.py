# I am using pixela to create the graph or like a sheet to see the data.....
""" note pixels is a japan based api so we use its color name in japanese"""
# https://pixe.la/v1/users/raghav9650/graphs/graph1.html this link will view the graph of data and remember we can ru it everday and stroe the data



import requests,os
from dotenv import load_dotenv
from datetime import datetime,timedelta

pixela_endpoint="https://pixe.la/v1/users"

load_dotenv()
USERNAME=os.environ("USERNAME")
TOKEN=os.environ("TOKEN")
graph_id="graph1"

user_params={
    "token":"raj123vusre23feh4$ew",
    "username":"raghav9650",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config={
    "id":graph_id,
    "name":"Cycling Graph",
    "unit":"km",
    "type":"float",
    "color":"shibafu"
}
headers={
    "X-USER-TOKEN":TOKEN
}
# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)
today=datetime.now()
pixel_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":"8"
}

response=requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
print(response.text)
# yesterday=today - timedelta(days=1)
# new_data={
#     "quantity":"5.0"
#     }

# response=requests.put(url=f"{pixel_creation_endpoint}/{yesterday.strftime("%Y%m%d")}",json=new_data,headers=headers)
# print(response.text)

"""for deleting the pixel"""

# delete_endpoint=f"{pixel_creation_endpoint}/{day.strftime("%Y%m%d")}" day can be anythiing
# response=requests.delete(url=delete_endpoint,headeres=headers)
# print(requests.get)