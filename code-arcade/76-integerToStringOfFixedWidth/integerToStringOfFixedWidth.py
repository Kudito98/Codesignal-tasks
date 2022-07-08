def solution(number, width):
    numberStr = str(number)[::-1]
    newNumber = ""
    for i in range(width):
        if len(numberStr) > i:
            newNumber += numberStr[i]
        else:
            newNumber += "0"
    return newNumber[::-1]