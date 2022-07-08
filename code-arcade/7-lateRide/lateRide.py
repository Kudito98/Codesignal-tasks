def solution(n):
    time = str(int(n/60)) + str(n % 60)
    sumtime = 0
    for i in time:
        sumtime = sumtime + int(i)
    
    return sumtime