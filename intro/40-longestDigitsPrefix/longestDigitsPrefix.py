def solution(inputString):
    numbers = ""
    for i in inputString:
        if i.isdigit():
            numbers += i
        else:
            return numbers
    return numbers