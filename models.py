from flask import  json


def load_data(path="./data.json"):
    data = None
    with open("data.json", "r") as f:
        data = json.load(f)
    return data
