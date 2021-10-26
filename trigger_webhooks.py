import requests
import os

sample_input = os.environ['sample_input']
print(str(sample_input))

url = "https://ennzbpev4mlci.x.pipedream.net/"

payload = ""
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
