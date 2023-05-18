import json

f = open('sample_data.json')
data = json.load(f)
# f.close()
#
# print(type(data))
# final_json = {}
# for item in data['parametersList']:
#
#     result = {
#         "max": item['max'],
#         "min": item['min'],
#         "avg": item['avg']
#     }
#     parameterName = item['parameterName']
#     final_json[parameterName] = result
#
# print(final_json)
final_result = []
for item in data['parametersList']:
    dictionary = {
        "parameterName": item['parameterName'],
        "max": item['max'],
        "min": item['min'],
        "avg": item['avg']
    }
    final_result.append(dictionary)
    print(final_result)
f.close()
