def solution(n, firstNumber):
    for i in range(int(n/2)):
        if firstNumber < (n-1):
            firstNumber += 1
        else:
            firstNumber = firstNumber - (n - 1)
            
    return firstNumber
