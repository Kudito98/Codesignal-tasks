from math import sqrt
from collections import Counter
def solution(s):
    res = -1
    strlen = len(s)
    start = int(sqrt(10**(strlen - 1))) + 1 - strlen % 2
    end = int(sqrt(10**(strlen))) + strlen % 2
    pattern = sorted(Counter(s).values())
    for i in range(start, end):
        if sorted(Counter(str(i**2)).values()) == pattern:
            res = i**2
            
    return res
        

