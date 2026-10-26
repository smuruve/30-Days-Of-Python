import datetime

# 1
from datetime import datetime
now = datetime.now()
print(now)

# 2
formatted_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print(formatted_time)

# 3
today = "5 December, 2019" # date string
today_converted = datetime.strptime(today, "%d %B, %Y")
print(today_converted) # date object

# 4
this_day = datetime(year = 2026, month = 10, day = 26, hour = 20)
new_year = datetime(year = 2027, month = 1, day = 1, hour = 0)

before_new_year = new_year - this_day
print(f"The time between today and the new year is {before_new_year} hours")

# 5
unix = datetime(year = 1970, month = 1, day = 1, hour = 0, minute = 0, second = 0)
time_since_unix = now - unix

print(f"{time_since_unix} has passed since the unix epoch")