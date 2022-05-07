# class Candy:
#     def set_info(self, shape, color):
#         self.shape = shape
#         self.color = color

# satang = Candy()
# satang.set_info("circle", "brown")

# # 생성자
# class Candy:
#     def __init__(self, shape, color):
#         self.shape = shape
#         self.color = color
        

# satang = Candy("circle", "brown")

# 소멸자
class Sample:
    def __del__(self):
        print("인스턴스가 소멸됩니다")

sample = Sample()
del sample