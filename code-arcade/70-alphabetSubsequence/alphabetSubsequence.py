def solution(s):
    currentValue = 0
    for i in s:
        if ord(i) > currentValue:
            currentValue = ord(i)
        else:
            return False
    return True
