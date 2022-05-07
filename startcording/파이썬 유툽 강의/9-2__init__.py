class Unit: 
    def __init__(self, name, hp, damage): # 파이썬에서 쓰이는 생성자 셀프를 제외하고 나머지 값 3개는 항상 생성자에 포함되어야 함
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# marine3 = Unit("마린") # 이렇게 한가지나 두가지 요구조건만 넣고 출력하면 오류가 뜸 항상 3개의 내용을 다 넣어야 됨