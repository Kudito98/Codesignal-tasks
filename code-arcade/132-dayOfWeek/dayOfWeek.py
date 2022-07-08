from calendar import isleap, weekday
def solution(birthdayDate):
    month, day, year = map(int, birthdayDate.split("-"))
    
    dayOfWeek = weekday(year, month, day)
    nextYear = year 
    nextBirthday = 7
    
    if isleap(year) and day == 29 and month == 2:
        while dayOfWeek != nextBirthday:
            nextYear += 4
            if isleap(nextYear):
                nextBirthday = weekday(nextYear, month, day)
        return nextYear - year
    else:
        while dayOfWeek != nextBirthday:
            nextYear += 1
            nextBirthday = weekday(nextYear, month, day)
        return nextYear - year   
