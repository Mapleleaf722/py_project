import datetime

# datetime.datetime.now()返回一个'datetime.datetime'对象
current_datetime = datetime.datetime.now()
print(current_datetime, type(current_datetime))

# datetime to string
str_time = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
print(str_time)

print('year', current_datetime.year)
print('month', current_datetime.month)
print('day', current_datetime.day)
print('hour', current_datetime.hour)
print('minute', current_datetime.minute)
print('second', current_datetime.second)

