from datetime import datetime, date

day = datetime.today().strftime('%d/%m/%Y')

day1 = date.today()
if day == '01/01/2024':
    print("Happy New Year")

else:
    print("Happy New Year later", day)
