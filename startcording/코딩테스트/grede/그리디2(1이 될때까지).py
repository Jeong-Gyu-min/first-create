# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 합니다. 단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있습니다.
# 1. N에서 1을 뺍니다
# 2. N을 K로 나눕니다.
# 예를 들어 N이 17, K가 4라고 가정합시다. 이때 1번의 과정을 한번 수행하면 N은 16이 됩니다. 이우에 2번의 과정을 두번 수행하면 N은 1이 됩니다.
# 결과적으로 이 경우 전체 과정을 실행한 횟수는 3이 됩니다. 이는 N을 1로 만드는 최소 횟수입니다.

n, k = map(int, input().split())

result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break

    result += 1
    n //= k
    
result += -1
print(result)