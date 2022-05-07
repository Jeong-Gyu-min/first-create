# cabinet = {3: "유재석", 100: "김태호"}
# print(cabinet[3])

# print(cabinet.get(3))
# print(cabinet.get(5, "사용 가능"))
# print(cabinet.get(5)) # get 같은 경우에 해당 값이 없으면 None이라는 결과값을 반환하지만 아무것도 적지 않으면 에러가 뜸
# print(cabinet[5]) # 에러가 뜸
# print("hi")

# print(3 in cabinet) # True

cabinet  = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

del cabinet["B-100"]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()
print(cabinet)