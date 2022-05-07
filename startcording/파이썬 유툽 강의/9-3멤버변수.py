# 멤버 변수 : 클래스 내에 정의된 변수고 그 변수를 사용 할수 있는것
class Unit: 
    def __init__(self, name, hp, damage): 
        self.name = name # 멤버변수
        self.hp = hp # 멤버변수
        self.damage = damage # 멤버변수
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}, 체력 : {2}".format(wraith1.name, wraith1.hp, wraith1.hp))
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True
if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name)) #레이스 2에만 적용이 되고 레이스 1에서는 이름,체력,데미지에 대한 변수만 있기 때문에 레이스 1로 할경우 에러가 나옴