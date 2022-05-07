import csv

with open("C:/Users/wjdrb/OneDrive/바탕 화면/PythonWorkspace/학원/section13/output/차량관리_01.csv", "r", newline="") as file:
    csv_reader = csv.reader(file, delimiter=",", quotechar="\"")
    for line in csv_reader:
        print(line)