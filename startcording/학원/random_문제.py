import random
from datetime import *


random = random.randint(1, 100)
print("UpDown게임을 시작합니다.")

start = datetime.now()

running = True
while running:
    answer = int(input("어떤 값일까요? >>> "))
    if answer == random:
        print("정답입니다.")
        running = False
    elif answer > random:
        print("Down")
    else:
        print("Up")

end = datetime.now()

elapse = end - start
elapse = elapse.total_seconds()
print("총 {}초가 소요되었습니다.".format(elapse))
