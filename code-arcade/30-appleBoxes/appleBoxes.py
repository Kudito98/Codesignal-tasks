def solution(k):
    redApples = 0
    yellowApples = 0
    for i in range(2, (k+1)):
        if i % 2 == 0:
            redApples += i*i
        else:
            yellowApples += i*i
    return (redApples - (yellowApples + 1))