import requests
import json

url = "https://dogapi.dog/api/v2/breeds"

response = requests.get(url)

# data es un diccionario
data_dict = json.loads(response.content)
next_url = data_dict["links"]["next"]

print(next_url)

response_2 = requests.get(next_url)

# data es un diccionario
data_dict_2 = json.loads(response_2.content)
print(json.dumps(data_dict_2, indent=2))
