import requests

file = open('./info.txt')
content = file.readlines()
client_secret = content[1]
client_secret = client_secret.replace(" ", "")
client_secret = client_secret.replace("\n", "")
client_id = content[2]
client_id = client_id.replace(" ", "")
client_id = client_id.replace("\n", "")

params = {'num_keywords': 15}
keywords = requests.get('https://api.everypixel.com/v1/keywords', params=params, auth=(client_id, client_secret)).json()

with open('image2.png','rb') as image:
    data = {'data': image}
    keywords = requests.post('https://api.everypixel.com/v1/keywords', files=data, auth=(client_id, client_secret)).json()



for i in keywords["keywords"]:
    print(i["keyword"])
print(len(keywords["keywords"]))