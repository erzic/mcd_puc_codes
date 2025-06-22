import requests
import json


breed_id = "68f47c5a-5115-47cd-9849-e45d3c378f12"
url = f"https://dogapi.dog/api/v2/breeds/{breed_id}"

response = requests.get(url)

# data es un diccionario
data_dict = json.loads(response.content)

print(json.dumps(data_dict, indent=2))
