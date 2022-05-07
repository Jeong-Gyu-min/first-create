import csv

with open("C:/Users/wjdrb/OneDrive/바탕 화면/PythonWorkspace/학원/section13/output/차량관리_03.csv", "w", newline="") as file: #newline이 띄어쓰기를 생략
    csv_maker = csv.writer(file, delimiter=",")
    csv_maker.writerow([1, "08러1234", "2020-10-20,14:00"])
    csv_maker.writerow([2, "25다1234", "2020-10-20,14:10"])
    csv_maker.writerow([3, "28하1234", "2020-10-20,14:20"])
print("차량관리.csv 파일이 생성되었습니다.")
    