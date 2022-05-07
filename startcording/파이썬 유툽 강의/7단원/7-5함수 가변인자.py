# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") #뒤에 엔드를 붙여서 빈칸을 넣어주면 같은줄 출력
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20, "파이썬", "자바", "C+", "C++", "C")

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") #뒤에 엔드를 붙여서 빈칸을 넣어주면 같은줄 출력
    for lang in language:
        print(lang, end=" ")
    print() #줄바꿈 (의미없음)

profile("유재석", 20, "파이썬", "자바", "11", "C++", "C+")


