from datetime import datetime, timedelta
def solution(someTime, leavingTime):
    
    some_dt = datetime.strptime(someTime, "%Y-%m-%d %H:%M")
    leaving_dt = datetime.strptime(leavingTime, "%Y-%m-%d %H:%M")
    return datetime.strftime(some_dt - (leaving_dt - some_dt), "%Y-%m-%d %H:%M")

