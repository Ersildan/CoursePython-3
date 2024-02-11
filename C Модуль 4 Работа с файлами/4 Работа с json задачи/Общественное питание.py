import json

with open('food_services.json', encoding='utf-8') as file:
    data = json.load(file)
    res, res_ = dict(), dict()

    for d in data:
        res[d['District']] = res.get(d['District'], 0) + 1
        if d['IsNetObject'] == 'да':
            res_[d['OperatingCompany']] = res_.get(d['OperatingCompany'], 0) + 1

    task_1 = max(res.items(), key=lambda x: x[1])
    task_2 = max(res_.items(), key=lambda x: x[1])

    print(f"{task_1[0]}: {task_1[1]}", f"{task_2[0]}: {task_2[1]}", sep='\n')
