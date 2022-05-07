# 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다.
# 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 
# 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 
# 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 
# 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

m = int(input())
time = []

for i in range(m):
    a, b = map(int, input().split())
    time.append((a, b))

# 가장 빨리 끝나는 회의 먼저 배정하고, 똑같은 시간에 끝나는 회의라면 먼저 시작하는 회의를 우선순위로 둔다
time = sorted(time, key = lambda x: (x[1], x[0]))

count = 1
prev = time[0][1]

for sch in time[1:]:
    if prev <= sch[0]:
        prev = sch[1]
        count += 1

print(count)



