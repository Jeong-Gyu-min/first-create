import random

# def introduce(name, age):
#     print("내 이름은 {}이고, 나이는 {}살 입니다.".format(name, age))

# introduce("james", 25)

# def show(*args):
#     for item in args:
#         print(item)

# show("Python")
# show("happy", "birthday")

# def greet(message = "안녕하세요"):
#     print(message)
# greet("반갑습니다")
# greet()

# 디폴트 매개변수가 있는 경우 뒤로 배치
# def greet(name, message = "안녕하세요"):
#     print(f"{name}님 {message}.")

# greet("김철수")

# def adder(*args):
#     print("{}의 합은 {}입니다".format(args, sum(args)))

# adder(1, 2)
# adder(1, 2, 3)
# adder(1, 2, 3, 4)

# def calculator(*args):
#     return sum(args), sum(args)/len(args), max(args), min(args)

# a, b, c, d = calculator(1, 2, 3, 4, 5)
# print("합계", a)

