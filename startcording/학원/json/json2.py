import json

dict_list = [
    {
        "name" : "james",
        "age" : 20,
        "spec" : [
            175.5,
            70.5
        ]
    },
    {
        "name" : "alice",
        "age" : 22,
        "spec" : [
            168.5,
            70.5
        ]
    }
]

json_string = json.dumps(dict_list, indent=4)

with open("C:/Users/wjdrb/OneDrive/바탕 화면/PythonWorkspace/학원/section13/output/dictList_02.json", "w") as file:
    file.write(json_string)

print("dictList.json 파일이 생성되었습니다.")