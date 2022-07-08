import math

def solution(a):
    almostRes = []
    for num in a:
        temp = []
        for digit in str(num):
            temp.append(int(digit))
        almostRes.append(temp)
    
    res = []
    for p in almostRes:
        c = math.prod(p)
        res.append(c)
    
    return len(set(res))