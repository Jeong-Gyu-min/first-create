import json

with open("C:/Users/wjdrb/OneDrive/바탕 화면/PythonWorkspace/학원/section13/input/cctv.json", "r", encoding="utf-8") as file:
    json_reader = file.read()
    dict_list = json.loads(json_reader)
    # print(dict_list)
cctv_purpose = set()

for dic in dict_list:
    print(dic["설치목적구분"])
    cctv_purpose.add(dic["설치목적구분"])

print(cctv_purpose)
