import requests


def get_image_details(image_data):
    subscription_key = "ca22d05f88ff4261ac3e4138a44472ce"
    endpoint = "https://eastus.api.cognitive.microsoft.com/"
    analyze_url = endpoint + "vision/v3.0/analyze"

    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
               'Content-Type': 'application/octet-stream'}
    params = {'visualFeatures': 'Categories,Description,Color'}
    response = requests.post(
        analyze_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()
    return response.json()
