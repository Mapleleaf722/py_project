import datetime

birthday = '1996-03-06'
# 将字符串的日期格式化为datetime.datetime对象
birthday_date = datetime.datetime.strptime(birthday, '%Y-%m-%d')
print(birthday_date, type(birthday_date))

current_datetime = datetime.datetime.now()
# 两个datetime.datetime对象相减返回的是datetime.timedelta对象
minus_datetime = current_datetime - birthday_date
print(minus_datetime, type(minus_datetime))
