def solution(inputArray):
    sumHouses = 0
    for i in inputArray:
        if i == 0:
            return sumHouses
        else:
            sumHouses += i
