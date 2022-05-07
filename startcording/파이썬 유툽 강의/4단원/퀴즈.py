a = "http://naver.com"
a1 = a[7:]
a2 = a1[:a1.index(".")]

print(a2[:3] + str(len(a2)) + str(a2.count("e")) + "!")


url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(password)