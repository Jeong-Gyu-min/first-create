import json

with open("C:/Users/wjdrb/OneDrive/바탕 화면/PythonWorkspace/학원/section13/output/dictList_02.json", "r") as file:
    json_reader = file.read()
    dict_list = json.loads(json_reader)
    print(dict_list)

for dic in dict_list:
    print("이름: {}".format(dic["name"]))
    print("이름: {}".format(dic["age"]))
    print("이름: {}".format(dic["spec"][0]))
    print("이름: {}".format(dic["spec"][1]))

    print()
    