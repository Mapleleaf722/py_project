# 输入：
# 开始日期，例如2021-04-28
# 结束日期，例如2021-05-03
# 输出：
#     [
#         2021-04-28，2021-04-29，2021-04-30，
#         2021-05-01，2021-05-02，2021-05-03
#     ]

import datetime


def all_days_between_two(start_day, end_day):
    # 格式化为时间戳
    start_day_obj = datetime.datetime.strptime(start_day, '%Y-%m-%d')
    end_day_obj = datetime.datetime.strptime(end_day, '%Y-%m-%d')
    result = []
    while start_day_obj <= end_day_obj:
        result.append(start_day_obj.strftime('%Y-%m-%d'))
        start_day_obj += datetime.timedelta(days=1)
    return result


print(all_days_between_two('2021-04-28', '2021-05-03'))
