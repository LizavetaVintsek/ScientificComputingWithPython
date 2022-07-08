def print_working_days(date1, date2):
    import datetime
    day1 = datetime.date.fromisoformat (date1)
    day2 = datetime.date.fromisoformat (date2)
    while day1 < day2:
        if day1.weekday() < 5:
            print(day1.isoformat())
        day1 = day1 + datetime.timedelta(days = 1)
print(print_working_days('2022-03-31', '2022-04-06'))
