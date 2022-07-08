def solution(time):
    hour = time[0:2]
    mins = time[3:5]
    if int(hour) < 24 and int(mins) < 60:
        return True
    else:
        return False