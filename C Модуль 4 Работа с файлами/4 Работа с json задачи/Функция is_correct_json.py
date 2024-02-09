import json


def is_correct_json(string):
    try:
        json.loads(string)
        return True
    except:
        return False


print(is_correct_json('number = 17'))



