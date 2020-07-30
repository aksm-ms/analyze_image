import requests

url = "https://akimageanalysishack.azurewebsites.net/analyze"

files = [
  ('file', open('<your image file>','rb'))
]

response = requests.request("POST", url, files = files)

print(response.text.encode('utf8'))
