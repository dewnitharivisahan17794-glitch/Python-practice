import datetime

#DAY
b_day = datetime.date(1990, 5, 17)#don't enter month as 05 it can be only entered as 5
print(b_day)
today = datetime.date.today()
print(today)
now = datetime.datetime.now()
print(now)
age_by_days = (today - b_day).days
print(age_by_days)

#uses date style
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

#weekdays/isoweekdays
print(today.weekday())#0 is monday and 6 is sunday
print(today.isoweekday())#1 is monday and 7 is sunday

#TIME
b_time = datetime.time(12, 30, 45)
print(b_time)
print(b_time.hour)


#DATE&TIME
b_datetime = datetime.datetime(1990, 5, 17, 12, 30, 45)
print(b_datetime)
print(b_datetime.year)

today = datetime.datetime.today()
print(today)

#uses timedelta
t=datetime.timedelta(days=5, hours=3, minutes=30)
print(t)
print(today + t)



