# score_file = open("score.txt", "w", encoding="utf8") # 오픈을 통해 파일을 열어주고, 첫번째는 파일 이름, 두번째 W는 쓰기위한 목적(write), utf8을 쓰는 이유는 한글을 썻을때 이상한 문자로 변경되는것을 방지
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close() # 파일을 열었으면 항상 닫는것까지 해줘야한다.

# score_file = open("score.txt", "a", encoding="utf8") # 여기서 w를 한번 더써주면 덮어쓰기가 되버림, a(append)는 이어쓰기
# score_file.write("과학 : 50") # write는 줄바꿈이 안됨
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read()) #가져오기
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) # 줄별로 일기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end = "")
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")

score_file.close