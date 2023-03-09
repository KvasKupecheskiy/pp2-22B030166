import datetime

now_date = datetime.date.today()
five_day_earlier = now_date - datetime.timedelta(days=5)

print(five_day_earlier)