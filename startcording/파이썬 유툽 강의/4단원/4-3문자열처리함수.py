python = "Python is Amazing"
# print(python.lower()) # 소문자
# print(python.upper()) # 대문자
# print(python[0].isupper()) # python의 문자열 첫번째가 대문자냐? True
# print(len(python))
# print(python.replace("Python", "Java")) # python의 문자 Python을 Java로 바꿔줌

index = python.index("n")
print(index)
index = python.index("n", index + 1) # index+1을 함으로써 첫번째 n자리에서 +1자리부터 찾기때문에 두번째 n을 찾게됨
print(index)

print(python.find("n"))
print(python.find("Java")) # 내가 원하는 값이 없으면 -1이 나옴
# print(python.index("Java")) # 내가 원하는 값이 없으면 오류가 나오면서 프로그램 종료
print(python.count("n")) # n의 갯수
