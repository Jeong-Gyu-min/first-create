# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# print("Python", "Java", "JavaScript", sep= ",", end = "?") # sep는 각 문자 사이에 넣을 것을 지정, end는 줄바꿈을 하지 않음
# print("무엇이 더 재밌을까요?")

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

answer = input("아무 값이나 입력하세요 : ") #사용자가 문자를 입력하면 항상 문자열로 받음
print("입력하신 값은 " + answer + "입니다.") #그래서 answer 부분을 str으로 안감싸도 됨