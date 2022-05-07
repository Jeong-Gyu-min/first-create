class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # super를 쓰게 되면 괄호를 붙이고 뒤에 괄호 안에 self를 넣지 않음
        self.lication = location
        print("{0} : {1} 체력으로 {2}에 위치한다.".format(name, hp, location))

BuildingUnit("서플라이 디폿", 500, 0)