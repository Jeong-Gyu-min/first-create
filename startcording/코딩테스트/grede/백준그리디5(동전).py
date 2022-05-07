n, m = map(int, input().split())
moneys = []

for i in range(n):
  moneys.append(int(input()))

count = 0
moneys.sort(reverse=True)

    
for money in moneys:
    count += m // money
    print(count)
    m %= money

print(count)
