from datetime import date, datetime
import string


def date_hour():
    today = date.today()
    print('Today is:', today)
    print('Parts of data are:', today.day, today.month, today.year)
    print('Number of the week days:', today.weekday() + 1)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    days_string = " ".join(days)
    days_upper = string.capwords(days_string)
    days = days_upper.split(" ")
    print(days)

    print('Name of the day of the week:', days[today.weekday()])

    date_time = datetime.now()
    print('Date and hour:', date_time)

    time_now = datetime.time(date_time)
    print('Currently hour:', time_now)


date_hour()
