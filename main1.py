import json

with open('sample_data.json') as file:
    json_data = file.read()
data_list = json.loads(json_data)

# print(data_list["parametersList"])
for item in data_list["parametersList"]:
    if "sparkList" in item:
        print("true")
        li = []
        for each_item in item["sparkList"]:
            if isinstance(each_item, float):
                li.append(each_item)
        print(max(li))
    else:
        print('false')

