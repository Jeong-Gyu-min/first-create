# student_list = []
# with open("C:/Users/wjdrb/OneDrive/바탕 화면/PythonWorkspace/학원/section13/input/학생명단.csv", "rt") as file:
#     file.readline()
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         student = line.split(",")
#         student_list.append(student)
# print(student_list)


member_list = []
with open("C:/Users/wjdrb/OneDrive/바탕 화면/PythonWorkspace/학원/section13/input/회원명단.csv", "rt") as file:
    file.readline()
    while True:
        line = file.readline()
        if not line:
            break
        member = line.split(",")
        member[0] = member[0].strip("\"")
        member_list.append(member)
print(member_list)