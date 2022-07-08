def solution(commands):
    size = len(commands)
    deg = 0
    temp = 0
    for i in range(0,size):
        if commands[i] == 'L':
            deg += -90
        elif commands[i] == 'R':
            deg += 90
        elif commands[i] == 'A':
            deg += 180
        if deg % 180 == 0:
            temp += 1
            deg = 0
    return temp