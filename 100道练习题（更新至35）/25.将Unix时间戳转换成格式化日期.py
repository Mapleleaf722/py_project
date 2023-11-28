# Unix 时间戳是从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数，不考虑闰秒
import datetime

unix_time = 1620747224

datetime_obj = datetime.datetime.fromtimestamp(unix_time)
datetime_str = datetime_obj.strftime('%Y年%m月%d日 %H时%M分%S秒')
print(datetime_str)