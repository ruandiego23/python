from datetime import date, datetime
import string


def date_hour():
    today = date.today()
    print('Hoje é:', today)
    print('Partes da data é', today.day, today.month, today.year)
    print('Número do dia da semana:', today.weekday())
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
