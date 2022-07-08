def solution(inputString):
    s = inputString.lower().replace(' ', '')
    return s==s[::-1]
