import datetime


def get_diff_days(pdate, days):
    # 将传入的字符串日期变成datetime对象
    pdate_obj = datetime.datetime.strptime(pdate, '%Y-%m-%d')
    time_gap = datetime.timedelta(days=days)
    pdate_result = pdate_obj - time_gap
    return pdate_result.strftime('%Y-%m-%d')


print(get_diff_days('2023-9-7', 7))
print(get_diff_days('2023-9-7', 3))
print(get_diff_days('2023-4-28', 7))
print(get_diff_days('2023-04-01', 3))
# 中文年月日转时间戳
a = '2023年9月7日'
print(datetime.datetime.strptime(a, '%Y年%m月%d日'))
