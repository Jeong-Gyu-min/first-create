class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("{0} : {1}시 방향으로 {2} 속도로 이동".format(self.name, location, self.speed))

class AttactUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        print("{0} 체력을 가지며 {1} 공격력을 가진 {2}가 {3} 속도로 이동한다.".format(self.hp, self.damage, self.name, self.speed))

    def damaged(self, damage):
            print("{0} : {1} 피해를 입었습니다.".format(self.name, self.damage))
            self.hp -= damage
            print("{0} : 체력이 {1} 남았습니다.".format(self.name, self.hp))
            if self.hp == 0:
                print("{0} : 파괴되었습니다.".format(self.name))


vulture = AttactUnit("벌쳐", 50, 15, 20)
vulture.damaged(20)
vulture.damaged(30)


