# 2

nation = ["그리스", "아테네", "독일", "베를린", "러시아", "모스크바", "미국", "워싱턴"]

file = open("C:/Users/wjdrb/OneDrive/바탕 화면/PythonWorkspace/학원/section13/output/nation.txt", "wt")
for i in range(0, len(nation), 2):
    s = "{}-{}".format(nation[i], nation[i+1])
    # print(s)
    file.write(s)
file.close()
   
print("생성된 nation.txt 파일의 내용은 다음과 같습니다.")
file = open("C:/Users/wjdrb/OneDrive/바탕 화면/PythonWorkspace/학원/section13/output/nation.txt", "rt")
line_list = file.readlines()
for line in line_list:
    print(line, end=" ")
file.close

