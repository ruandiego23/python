import calendar


def calendar_in_text():
    calendar_text = calendar.TextCalendar(calendar.SUNDAY)
    txt_calendar = calendar_text.formatmonth(2024, 6)
    print(txt_calendar)


calendar_in_text()


def calendar_in_html():
    calendar_html = calendar.HTMLCalendar(calendar.SUNDAY)
    html_calendar = calendar_html.formatmonth(2024, 6)
    print(html_calendar)


calendar_in_html()
