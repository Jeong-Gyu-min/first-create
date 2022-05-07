# 인스턴스 메소드
# class Korean:
#     country = "한국"

#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address

# print(Korean.country)
# man = Korean("홍길동", 35, "서울")

# print(man.name)
# print(man.age)
# print(man.address)


# 클래스 메소드
# class Korean:
#     country = "한국"
#     @classmethod
#     def trip(cls, country):
#         if cls.country == country:
#             print("국내여행입니다.")
#         else:
#             print("해외여행입니다.")

# Korean.trip("한국")
# Korean.trip("미국")

# 정적 메소드
class Korean:
    country = "한국"
    @staticmethod
    def slogan():
        print("Imagine your Korea")

Korean.slogan()