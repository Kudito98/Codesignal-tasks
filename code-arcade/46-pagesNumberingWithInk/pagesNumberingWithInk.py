import math
def solution(current, numberOfDigits):
    while numberOfDigits >= 0:
        numberOfDigits -= math.ceil(math.log10(current+1))
        current += 1
    return current - 2
