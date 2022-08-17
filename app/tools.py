
import json

ACCESS_FILE_PATH = "./app/data/access.json"

def get_access_data(service_name: str) -> str:
    with open(ACCESS_FILE_PATH, "r") as f:
        data = json.load(f)
    return data.get(service_name)