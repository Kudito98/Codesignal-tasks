import calendar

def solution(month, year):
    return calendar.HTMLCalendar().formatmonth(year, month).replace('\n', '')