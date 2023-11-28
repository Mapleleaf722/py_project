# 怎样验证一个字符串是日期YYYY-MM-DD格式?
# 正则表达式:
# 一些由字符和特殊符号组成的字符串，
# 它们描述了重复模式，能够匹配多个字符串
import re


def date_is_right(date):
    return re.match('\d{4}-\d{2}-\d{2}', date)


date1 = '2021-05-20'
date2 = '202-05-20'
date3 = '2021/05-20'
date4 = '20210520'
print(date_is_right(date1))
print(date_is_right(date2))
print(date_is_right(date3))
print(date_is_right(date4))


