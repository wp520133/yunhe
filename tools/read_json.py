import json


def read_json(fileName):
    filepath = "C:/Users/17327/PycharmProjects/yunhe/data/" + fileName
    arr = []
    with open(filepath, "r", encoding="utf-8") as file:
        datas = json.load(file)
        for data in datas.values():
            arr.append(
                (data['username'], data['password'], data['sure_password'], data['success'])
            )
    return arr
