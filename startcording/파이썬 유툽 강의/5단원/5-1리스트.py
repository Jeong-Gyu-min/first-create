subway = [10, 20 ,30]
print(subway)

subway= ["유재석", "조세호", "박명수"]
print(subway)
print(subway.index("조세호"))

subway.append("하하")
print(subway)

subway.insert(1, "정형돈")
print(subway)

# 값 빼기
print(subway.pop()) # pop 안에 아무것도 안집어 넣으면 맨 마지막 리스트를 빼고, 숫자를 넣으면 거기에 알맞는 값을 뺌
print(subway)

# 카운팅
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬, 역정렬
num_list = [5,4,3,2,1]
num_list.sort()
print(num_list)
subway.sort()
print(subway)
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

num_list = [5,4,3,2,1]
mix_list = ["조세호", 20, True]
num_list.extend(mix_list)
print(num_list)

print(3 in num_list)
