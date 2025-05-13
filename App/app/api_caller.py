import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv('API_URL')

def generate_response(conversation):
    question = conversation[0]['parts'][0]['text']
    image_base64 = conversation[0]['parts'][1]['inline_data']['data']
    payload = {
        "questions": [question],
        "image_base64": image_base64
    }
    response = requests.post(url=f"{API_URL}/infer", json=payload)
    print(response)
    return response.json()['answers'][0]

