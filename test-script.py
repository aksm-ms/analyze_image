import requests

url = "https://akimageanalysishack.azurewebsites.net/analyze"

files = [
  ('file', open('C:\\ak\hackathon\YOLO-code\YOLO-Object-Detection\images\horses.jpg','rb'))
]

response = requests.request("POST", url, files = files)

print(response.text.encode('utf8'))
