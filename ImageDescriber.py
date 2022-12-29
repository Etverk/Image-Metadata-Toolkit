import requests
import json

file = open('./Data.txt')
content = file.readlines()
OcpKey = content[7].replace("\n", "")
imageUrl = content[8].replace("\n", "")

header = {"Ocp-Apim-Subscription-Key": OcpKey}
data = {"url": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Dhaulagiri_mountain.jpg"}

response = requests.post(imageUrl, headers=header, json=data)
responseDict = json.loads(str(response.text))
responseDescription = responseDict["description"]["captions"][0]["text"]
responseTitle = responseDescription.capitalize() + " - Generative AI"
print(responseTitle)
