import json
import random
import time
import base64
import os
import requests

class Text2ImageAPI:

    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }

    def get_model(self):
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']

    def generate(self, prompt, model, images=1, width=1024, height=1024):
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {
                "query": f"{prompt}"
            }
        }

        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']

    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']

            attempts -= 1
            time.sleep(delay)

client = Text2ImageAPI("https://api-key.fusionbrain.ai/", os.environ.get("KADINSKY_KEY"), os.environ.get("KADINSKY_SECRET"))
image_dir = "images"

def generate_asset(project_name: str, project_id: int, project_desc: str, map_description: str, appearance: str):
    promt = f"Game name: {project_name}.\nGame description: {project_desc}.\nCharacter appearance: {appearance}.\nAsset description: {map_description}.\nGenerate asset for this game in pixel style.Background part of image should all be black.\n"
    
    model_id = client.get_model()
    uuid = client.generate(promt, model_id, width=512, height=512)
    images = client.check_generation(uuid)
    image_data = base64.b64decode(images[0])
    generated_image_name = str(project_id) + str(random.randint(1, 100)) + ".png"
    generated_image_filepath = os.path.join(image_dir, generated_image_name)
    with open(generated_image_filepath, "wb+") as file:
        file.write(image_data)
        
    return generated_image_name

