import calendar


def Month():
    for month in calendar.month_name:
        print(month)
    print()

    print('Days of the week')
    for day in calendar.day_name:
        print(day, end=' ')


Month()
