file = open("C:/Users/wjdrb/OneDrive/바탕 화면/PythonWorkspace/학원/section13/output/hello.txt", "wt")

file.write("안녕하세요.")
file.write("\n")
file.write("반갑습니다.")
file.write("\n")
print("hello.txt 파일이 생성되었습니다.")

file.close()

file = open("C:/Users/wjdrb/OneDrive/바탕 화면/PythonWorkspace/학원/section13/output/hello.txt", "at")

file.write("Hello.\n")
file.write("Nice to meet you.\n")
print("hello.txt 파일에 새로운 내용이 추가되었습니다.")

file.close()

# 한글 이름 파일 / utf-8로 문서 작성하기
import codecs
file = codecs.open("C:/Users/wjdrb/OneDrive/바탕 화면/PythonWorkspace/학원/section13/output/hello.txt", "w", "utf-8")
file.write("오늘 나는 학교에 갔습니다.")
file.close()

