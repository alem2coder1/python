from datetime import datetime, timedelta
# 剪去五天
tody = datetime.now().date()
y = tody - timedelta(days=5)
print(y)
# 今天，明天，后天
x = tody + timedelta(days=1)
z = tody - timedelta(days=1)
print(z,x,tody)
# 删除毫秒
current_time = datetime.now()
print(current_time)
microseconds = current_time.replace(microsecond=0)
print(microseconds)
# 删除两个星期的秒差
date_format = "%Y-%m-%d %H:%M:%S"
date1 = datetime.strptime("2024-02-10 00:00:00", date_format)
date2 = datetime.strptime("2024-02-10 23:59:59", date_format)
seconds = (date1 - date2).total_seconds()
print(abs(seconds))