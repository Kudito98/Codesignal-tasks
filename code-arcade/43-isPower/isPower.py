import math
def solution(n):   
    i = 2;
    while(math.pow(n, 1 / i) >= 2):
        if (math.ceil(math.pow(round(math.pow(n, 1 / i)), i) == n)):
            return True
        i += 1
    return n == 1