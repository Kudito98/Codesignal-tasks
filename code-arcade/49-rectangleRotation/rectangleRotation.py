import math
def solution(a, b):
    n = int(math.floor(a/math.sqrt(2)))
    m = int(math.floor(b/math.sqrt(2)))
    p1 = (n + 1 - n % 2)*(m + 1 - m % 2)
    
    n = n - 1
    m = m - 1
    p2 = (n + 2 - n % 2)*(m + 2 - m % 2)
    
    return p1 + p2
