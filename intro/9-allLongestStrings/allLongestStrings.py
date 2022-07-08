def solution(inputArray):
    mw = len(max(inputArray, key=len))
    return [e for e in inputArray if len(e) == mw]