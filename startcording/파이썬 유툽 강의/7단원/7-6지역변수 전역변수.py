# 글로벌로 바깥에 있는 건을 def 안으로 들이던가 13으로 가서
# gun = 10

# def checkpoint(soldiers):
#         global gun # 전역 공간에 있는 gun 사용
#         gun = gun - soldiers
#         print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))

#return 으로 gun을 해서 빼오던가
gun = 10

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))