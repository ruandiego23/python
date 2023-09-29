from datetime import timedelta, datetime


def delta_time():
    delta = timedelta(days=86, hours=8532, minutes=7645)
    print(delta)

    today = datetime.now()
    print('Date in the future:', today + delta)
    print('Date in the past:', today - delta)


delta_time()
