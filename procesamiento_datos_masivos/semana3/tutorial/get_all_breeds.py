import requests
import json

url = "https://dogapi.dog/api/v2/breeds"

response = requests.get(url)

# data es un diccionario
data_dict = json.loads(response.content)

print(json.dumps(data_dict, indent=2))
# print(data_dict["data"][0])
# print(data_dict["data"][0]["attributes"]["name"])
