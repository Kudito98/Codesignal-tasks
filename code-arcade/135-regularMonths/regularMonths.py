import calendar
def solution(currMonth):
    m, y = map(int, currMonth.split("-"))
    m += 1
    if m == 13:
        m = 1
        y += 1
    while calendar.weekday(y, m, 1):
        m += 1
        if m == 13:
            m = 1
            y += 1
    return "{:02d}-{:04d}".format(m, y)

                   
    