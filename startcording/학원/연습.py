hour, min = map(int, input().split())
time = int(input())

new_min = min + time


hour += ((min+new_min) // 60)

print(hour)