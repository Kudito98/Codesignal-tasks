def solution(inputString):
    normalString = inputString.casefold()
    reverseString = normalString[::-1]
    
    if normalString == reverseString:
        return True
    else:
        return False