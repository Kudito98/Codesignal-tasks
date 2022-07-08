def solution(time):
    h = time[0:2]
    m = time[3:5]
    if int(h) < 24 and int(m) < 60:
        return True
    else:
        return False
