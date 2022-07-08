import datetime
def solution(takeOffTime, minutes):
    if int(takeOffTime[:2])==4 and int(takeOffTime[3:5])<=40:
        takeOffTime='2000-01-01 '+takeOffTime
    if int(takeOffTime[:2])<=3:
        takeOffTime='2000-01-01 '+takeOffTime
    else:
        takeOffTime='1999-12-31 '+takeOffTime
    takeOffTime=datetime.datetime.strptime(takeOffTime, '%Y-%m-%d %H:%M')
    c=0
    midNight=datetime.datetime(year=2000, month=1, day=1, hour=0)
    p1=takeOffTime
    if p1<=midNight and minutes==[]:
        return(1)
    for i in range(len(minutes)):
        x=datetime.timedelta(minutes = minutes[i])
        timeZone=datetime.timedelta(minutes = 60)
        p2=takeOffTime+x-timeZone*i
        if p1<=midNight and p2>=midNight:
            c+=1
        p1=p2-timeZone
    if p2-timeZone<=midNight:
        c+=1
    return(c)