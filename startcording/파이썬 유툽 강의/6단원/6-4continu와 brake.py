# absent = [2, 5]
# no_book = [7] 
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))



absent = [2, 5]
no_book = [7]

for i in range(1, 10):
    if i in absent:
        continue
    elif i in no_book:
        print("{}번 교무실로 따라와".format(i))
        break
    print("{}번 책 읽어봐".format(i))


    