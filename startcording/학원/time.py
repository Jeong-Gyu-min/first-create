import time
import datetime



# print(time.time())

# print(time.ctime(time.time()))

# print(time.strftime("%Y-%m-%d %a %H:%M:%S"))

# time.sleep(1)

# wake = datetime.time(10, 48, 0)
# print(wake)

# today = datetime.datetime.now()
# print(today)
# print(today.year)
# print(today.month)
# print(today.day)
# print(today.hour)
# print(today.minute)
# print(today.second)

# yesterday = today - datetime.timedelta(days=1)
# tomorrow = today + datetime.timedelta(days=1)
# print(yesterday)

date1 = datetime.date(2020, 8, 25)
print(date1)

date2 = datetime.date(2020, 8, 26)
print(date2)

print(date2-date1)
print((date2-date1).total_seconds())

