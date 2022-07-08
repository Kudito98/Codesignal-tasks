import calendar
def solution(year, daysOfTheWeek, holidays):
    stayAfter = 0
    for date in holidays:
        month, day = map(int, date.split("-"))
        y = year
        y += month < 8
        stayAfter += calendar.weekday(y, month, day) + 1 in daysOfTheWeek
    return stayAfter
