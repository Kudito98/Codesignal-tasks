import calendar
def solution(x, weekDay, month, yearNumber):
    m = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December").index(month) + 1
    d = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday").index(weekDay)
    
    days = [calendar.weekday(yearNumber, m, d) for d in range(1, calendar.monthrange(yearNumber, m)[1]+1)]
    
    z = 0
    for i, day in enumerate(days):
        if day == d:
            z += 1
            if z == x:
                return i+1
    return -1