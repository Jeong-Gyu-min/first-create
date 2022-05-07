# 시간 출력

hour, min = map(int, input().split())
time = int(input())

hour += time // 60
min += time % 60

if min >= 60:
    min -= 60
    hour += 1
if hour >= 24:
    hour -= 0

print(hour, min)


