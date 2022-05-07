# import csv

# with open("C:/Users/wjdrb/OneDrive/바탕 화면/PythonWorkspace/학원/section13/input/cctv.csv", "r") as file:
#     line_list = file.readline()
#     print(line_list)
#     csv_reader = csv.reader(file, delimiter=",")
#     count = 0
#     for line in csv_reader:
#         count += 1

# print("서울특별시 마포구에 설치된 CCTV는 총 {}대 입니다.".format(count))

import csv

with open("C:/Users/wjdrb/OneDrive/바탕 화면/PythonWorkspace/학원/section13/input/cctv.csv", "r") as file:
    total = 0
    csv_reader = csv.reader(file, delimiter=",", quotechar = "\"")
    for idx, line in enumerate(csv_reader):
        if (idx != 0):
            total += int(line[4])

print("서울특별시 마포구에 설치된 CCTV는 총 {}대 입니다.".format(total))     