import json

dataDict = {
    "sampleString": "Its a great automation framework",
    "sampleList": ["good", "better", "best"],
    "sampleTuple": ("Python", "Pytest", "Automation"),
    "sampleObj": {"platform": "udemy", "valuable": True},
    "sampleInteger": 89,
    "booleanValue": True,
    "noneValue": None
}

print("Covert py dic to Json")
resultJson = json.dumps(dataDict, sort_keys=True, indent=4)  # to format
print(resultJson)
print(type(resultJson) == str)

print("Covert string in dic")
data_dict = json.loads(resultJson)
print(type(data_dict))

with open("example.json", "r") as file:
    data = json.load(file)
    print(type(data))
    print(data.keys())  # print the keys of the json
    print(data['address'])  # print the all data in the key
    #  read a transverse dictionary
    for key, value in data.items():
        print(key, ":", value)


#  how validate json
def validateJson(jsonStr):
    try:
        json.loads(jsonStr)
    except ValueError as err:
        return False
    return True


JsonString = """{'country': 'Brazil', 'state': 'RS', 'city': 'Sao Leopoldo', 'phone': '99999999999'}
"""
isValid = validateJson(JsonString)
print("Json string passed is valid??", isValid)
