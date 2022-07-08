def solution(startPosition, speed):
    maxMeetings = -1
    meetingPoint = 0
    currentMeeting = -1
    
    for i in range(len(startPosition)):
        for j in range(i+1, len(startPosition)):
            if (speed[j] - speed[i]) == 0:
                meetingPoint = (startPosition[i] - startPosition[j]) / -1
            else:
                meetingPoint = (startPosition[i] - startPosition[j]) / (speed[j] - speed[i])
                if (meetingPoint >= 0):
                    currentMeeting = 2
                    for k in range(j+1,len(startPosition)):
                        if startPosition[i] + speed[i] * meetingPoint == startPosition[k] + speed[k] * meetingPoint:
                            currentMeeting += 1;

                    if (currentMeeting > maxMeetings):
                        maxMeetings = currentMeeting
  
    return maxMeetings

    
