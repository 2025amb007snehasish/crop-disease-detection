import os
import requests

API_KEY = os.getenv("API_KEY")
MODEL = os.getenv("MODEL")

def predict_disease(image_file):
    url = f"https://classify.roboflow.com/{MODEL}?api_key={API_KEY}"

    response = requests.post(
        url,
        files={"file": image_file}
    )

    result = response.json()
    return result["predictions"][0]["class"]
