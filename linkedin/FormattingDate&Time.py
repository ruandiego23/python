
from datetime import datetime


# %y%Y - year, %a%A - Dia da semana, %b%B - Mês, %d - day of the month

# % c - date and hour from locality, % x - date from locality, % X - hour from locality

# %I%H - 12/24, %M - minute, %S - seconds, %p - AM/PM

def DateAndHour():
    today = datetime.now()
    print(today.strftime('O ano é: %Y'))
    print(today.strftime('Date and hour local: %c'))
    print(today.strftime('The current time is: %I:%M:%S %p'))
    print(today.strftime('The current time is: %H:%M:%S'))


DateAndHour()

