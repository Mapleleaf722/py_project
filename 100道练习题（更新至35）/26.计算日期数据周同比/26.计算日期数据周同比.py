import datetime

date_sale = {}
# 设置一个开关，不读取第一行的数据
is_first_line = True
with open('date_sale_data.txt', encoding='utf-8') as f:
    for line in f:
        if is_first_line:
            is_first_line = False
            continue
        line = line[:-1]
        date, sales = line.split('\t')
        date_sale[date] = int(sales)
print(date_sale)


# 返回7天前的日期
def get_diff_days(date, days):
    curr_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    timedelta = datetime.timedelta(days=days)
    return (curr_date - timedelta).strftime('%Y-%m-%d')


for date, sales in date_sale.items():
    date7 = get_diff_days(date, 7)
    # 返回date7的值，如果键不在字典中则返回0
    sale7 = date_sale.get(date7, 0)
    if sale7 == 0:
        print(date, sales, 0)
    else:
        week_diff = (sales - sale7) / sale7
        print(date, sales, date7, sale7, round(week_diff, 2))
