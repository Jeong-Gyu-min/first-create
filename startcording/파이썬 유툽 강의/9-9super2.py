class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        #super().__init__() # super로 상속받을 경우는 맨 앞에 있는 클래스로부터만 상속을 받음(Unit)
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()