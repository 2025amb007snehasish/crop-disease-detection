import requests

API_KEY = "OAHW4TaGIhsegImZQid4"
MODEL = "plant-disease-classification-dvfsj/1"

def predict_disease(image_file):
    url = f"https://classify.roboflow.com/{MODEL}?api_key={API_KEY}"

    response = requests.post(
        url,
        files={"file": image_file}
    )

    result = response.json()

    # Safety check
    if "predictions" not in result or len(result["predictions"]) == 0:
        return "No disease detected"

    return result["predictions"][0]["class"]
