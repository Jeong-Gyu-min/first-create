# class Person: #슈퍼클래스

#     def __init__(self, name):
#         self.name = name

#     def eat(self, food):
#         print(self.name + "가 " + food + "를 먹습니다.")

# class Student(Person): # 서브클래스

#     def __init__(self, name, school):
#         super().__init__(name)
#         self.school = school

#     def study(self):
#         print(self.name + "는 " + self.school + "에서 공부를 합니다.")

# potter = Student("해리포터", "호그와트")
# potter.eat("감자")
# potter.study()

# class Computer:

#     def __init__(self):
#         print("슈퍼 클래스의 생성자가 실행되었습니다.")

# class NoteBook(Computer):

#     def __init__(self):
#         super().__init__()
#         print("서브 클래스의 생성자가 실행되었습니다.")

# NoteBook()


class Coffee:

    def __init__(self, bean):
        self.bean = bean

    def coffee_info(self):
        print("원두 : {}".format(self.bean))

class Espresso(Coffee):
    def __init__(self, bean, water):
        super().__init__(bean)
        self.water = water

    def espresso_info(self):
        super().coffee_info()
        print("물 {}ml".format(self.water))

class Americano(Espresso):
    def __init__(self, bean, water, more_water):
        super().__init__(bean, water)
        # Espresso.__init__(self, bean, water)
        self.more_water = more_water

    def americano_info(self):
        super().espresso_info()
        print("물 더: {}ml".format(self.more_water))



# coffee = Espresso("콜롬비아", 30)
# coffee.espresso_info()

coffee = Americano("파나마", 20, 200)
coffee.americano_info()

