import json


def user_data():
    with open("candidates.json", "r", encoding="UTF-8") as file:
        data = json.load(file)
        users = {}
        for i in data:
            users[i["id"]] = i
    return users
